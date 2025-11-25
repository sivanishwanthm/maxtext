import os
import re
import json
import requests
from urllib.parse import urlparse, urldefrag
import concurrent.futures

# --- Configuration ---
CONFIG_FILE = ".link_checker_config.json"

# Directories to exclude from the scan
EXCLUDED_DIRS = [
    "node_modules",
    ".git",
    "__pycache__",
    ".pytest_cache",
    ".mypy_cache",
    "dist",
    "build",
    "venv",
    ".nox",
]

# File extensions to check for links
SUPPORTED_EXTENSIONS = [
    ".md",
    ".mdx",
    ".html",
    ".json",
    ".yaml",
    ".yml",
    ".txt",
    ".py",
    ".js",
    ".ts",
    ".sh",
]

# Improved Regular expression to find URLs, avoiding trailing punctuation
URL_REGEX = r'(?:(?:https?|ftp):\/\/|www\.)(?:[a-zA-Z0-9\-]+\.)+[a-zA-Z]{2,}(?:[^\s"`\'<>()\[\]{}]+)'
MARKDOWN_RELATIVE_LINK_REGEX = r'\[[^\]]*\]\((?!https?:\/\/)([^)]+)\)'
HTML_RELATIVE_LINK_REGEX = r'href=["\'](?!https?:\/\/)([^"\']+)["\']'

def load_config():
    """Loads the configuration from the JSON file."""
    if os.path.exists(CONFIG_FILE):
        with open(CONFIG_FILE, "r") as f:
            return json.load(f)
    return {"ignore_patterns": []}

def is_ignored(link, ignore_patterns):
    """Checks if a link matches any of the ignore patterns."""
    for pattern in ignore_patterns:
        if re.search(pattern, link):
            return True
    return False

def find_text_files(start_path="."):
    """Recursively finds all text files in a directory, excluding specified directories."""
    text_files = []
    for root, dirs, files in os.walk(start_path):
        dirs[:] = [d for d in dirs if d not in EXCLUDED_DIRS]
        for file in files:
            if any(file.endswith(ext) for ext in SUPPORTED_EXTENSIONS):
                text_files.append(os.path.join(root, file))
    return text_files

def check_link(link, file_path):
    """Checks a single link and returns an error message if it's broken."""
    link_without_fragment, _ = urldefrag(link)
    if not link_without_fragment: # It's just an anchor
        return None

    if link_without_fragment.startswith("http"):
        try:
            response = requests.head(link_without_fragment, timeout=5, allow_redirects=True, headers={'User-Agent': 'Mozilla/5.0'})
            if response.status_code >= 400:
                return f"HTTP Error {response.status_code}"
        except requests.RequestException:
            return "Connection Error"
    else:
        # Internal link
        abs_path = os.path.abspath(os.path.join(os.path.dirname(file_path), link_without_fragment))
        if not os.path.exists(abs_path):
            return "File Not Found"
    return None

def process_file(file, ignore_patterns):
    """Processes a single file to find and check links."""
    try:
        with open(file, "r", encoding="utf-8", errors="ignore") as f:
            content = f.read()
    except Exception:
        return (file, [])

    links = set(re.findall(URL_REGEX, content)) | \
            set(re.findall(MARKDOWN_RELATIVE_LINK_REGEX, content)) | \
            set(re.findall(HTML_RELATIVE_LINK_REGEX, content))

    file_broken_links = []

    # Filter out ignored links before checking
    valid_links = [link for link in links if not is_ignored(link, ignore_patterns)]

    with concurrent.futures.ThreadPoolExecutor(max_workers=20) as executor:
        future_to_link = {executor.submit(check_link, link, file): link for link in valid_links}
        for future in concurrent.futures.as_completed(future_to_link):
            link = future_to_link[future]
            try:
                error = future.result()
                if error:
                    file_broken_links.append((link, error))
            except Exception as exc:
                file_broken_links.append((link, str(exc)))
    return (file, file_broken_links)

def main():
    """Main function to scan for and report broken links."""
    config = load_config()
    ignore_patterns = config.get("ignore_patterns", [])

    all_files = find_text_files()
    broken_links_report = {}

    print(f"Scanning {len(all_files)} files...")

    with concurrent.futures.ProcessPoolExecutor() as executor:
        # Pass ignore_patterns to process_file
        results = executor.map(process_file, all_files, [ignore_patterns] * len(all_files))
        for i, (file, file_broken_links) in enumerate(results):
            print(f"Progress: {i+1}/{len(all_files)} files scanned", end='\r')
            if file_broken_links:
                broken_links_report[file] = file_broken_links

    print("\nScan complete.")

    if broken_links_report:
        with open("broken_links_report.md", "w") as f:
            f.write("# Broken Links Report\n")
            for file, broken_links in sorted(broken_links_report.items()):
                f.write(f"\n## 📄 In File: `{file}`\n")
                for link, error in broken_links:
                    f.write(f"- **Broken Link:** `{link}`\n")
                    f.write(f"  - **Error:** {error}\n")
        print("Broken links found. Report saved to broken_links_report.md")
    else:
        with open("broken_links_report.md", "w") as f:
            f.write("# Broken Links Report\n\n✅ No broken links found!\n")
        print("✅ No broken links found!")

if __name__ == "__main__":
    main()
