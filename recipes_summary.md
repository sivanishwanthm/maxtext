# Recipe Extraction Technical Summary

| Recipe Name / Link | Workload Type | Accelerator | Accelerator Type | Software Stack | Chips | Topology |
|---|---|---|---|---|---|---|
| https://github.com/google/maxtext/blob/main/PREFLIGHT.md | Pre-training / Infrastructure Setup | TPU | TPU v4 / TPU v5p / TPU v6e | MaxText, JAX | 8 | 2x4* |
| https://github.com/google/maxtext/blob/main/benchmarks/Getting_Started_Benchmarking.md | Pre-training / Benchmarking | TPU | TPU v5p / TPU v6e | MaxText, JAX, XPK | 8 | 2x4* |
| https://github.com/google/maxtext/blob/main/benchmarks/api_server/README.md | Inference / Benchmarking | TPU | TPU v5e / TPU v6e | MaxText, JAX, FastAPI, vLLM | 8 | 2x4* |
| https://github.com/google/maxtext/blob/main/benchmarks/maxtest/getting_started.md | Pre-training / Benchmarking | TPU | TPU v5e / TPU v5p / TPU v6e | MaxText, JAX, maxtest | 8 | 2x4* |
| https://github.com/google/maxtext/blob/main/docs/guides/checkpointing_solutions/convert_checkpoint.md | Pre-training / Checkpoint Conversion | TPU / GPU | TPU v5p / TPU v6e / NVIDIA H100 | MaxText, JAX, PyTorch, Orbax | 8 | 2x4* |
| https://github.com/google/maxtext/blob/main/docs/guides/checkpointing_solutions/emergency_checkpointing.md | Pre-training / Checkpoint Management | TPU | TPU v5e / TPU v5p | MaxText, JAX, Orbax | 8 | 2x4* |
| https://github.com/google/maxtext/blob/main/docs/guides/checkpointing_solutions/multi_tier_checkpointing.md | Pre-training / Checkpoint Management | TPU | TPU v5p / TPU v6e | MaxText, JAX, Orbax | 8 | 2x4* |
| https://github.com/google/maxtext/blob/main/docs/guides/data_input_pipeline/data_input_megatron_mmap.md | Pre-training / Data Input Pipeline | TPU | TPU v5e / TPU v5p | MaxText, JAX, Megatron-LM | 8 | 2x4* |
| https://github.com/google/maxtext/blob/main/docs/guides/data_input_pipeline/olmo_grain.md | Pre-training / Data Input Pipeline | TPU | TPU v5e / TPU v5p | MaxText, JAX, Grain | 8 | 2x4* |
| https://github.com/google/maxtext/blob/main/docs/guides/lora_model_bringup.md | SFT / LoRA Bringup | TPU | TPU v5e / TPU v5p | MaxText, JAX, Orbax, Tunix | 8 | 2x4* |
| https://github.com/google/maxtext/blob/main/docs/guides/monitoring_and_debugging/features_and_diagnostics.md | Pre-training / Monitoring & Debugging | TPU | TPU v5e / TPU v5p | MaxText, JAX, TensorBoard | 8 | 2x4* |
| https://github.com/google/maxtext/blob/main/docs/guides/monitoring_and_debugging/ml_workload_diagnostics.md | Pre-training / Monitoring & Debugging | TPU | TPU v5e / TPU v5p | MaxText, JAX, Cloud Monitoring | 8 | 2x4* |
| https://github.com/google/maxtext/blob/main/docs/guides/monitoring_and_debugging/monitor_goodput.md | Pre-training / Monitoring & Debugging | TPU | TPU v5e / TPU v5p / TPU v6e | MaxText, JAX, Goodput | 8 | 2x4* |
| https://github.com/google/maxtext/blob/main/docs/guides/monitoring_and_debugging/understand_logs_and_metrics.md | Pre-training / Monitoring & Debugging | TPU | TPU v5e / TPU v5p | MaxText, JAX, Cloud Logging | 8 | 2x4* |
| https://github.com/google/maxtext/blob/main/docs/guides/optimization/benchmark_and_performance.md | Pre-training / Performance Optimization | TPU | TPU v5e / TPU v5p / TPU v6e | MaxText, JAX, XLA | 8 | 2x4* |
| https://github.com/google/maxtext/blob/main/docs/guides/run_python_notebook.md | Pre-training / Interactive Notebooks | TPU | TPU v5e / TPU v5p / TPU v6e | MaxText, JAX, Jupyter Notebooks | 8 | 2x4* |
| https://github.com/google/maxtext/blob/main/docs/install_maxtext.md | Infrastructure Setup / Installation | TPU / GPU | TPU v4 / TPU v5e / TPU v5p / TPU v6e / NVIDIA H100 | MaxText, JAX, PyTorch, Docker | 8 | 2x4* |
| https://github.com/google/maxtext/blob/main/docs/run_maxtext/decoupled_mode.md | Pre-training / Decoupled Input Execution | TPU | TPU v5e / TPU v5p | MaxText, JAX, Grain | 8 | 2x4* |
| https://github.com/google/maxtext/blob/main/docs/run_maxtext/run_maxtext_elastic_training.md | Pre-training / Elastic Training | TPU | TPU v5e | MaxText, JAX, Pathways, Cluster Toolkit, GKE, XPK | 16 | 4x4 |
| https://github.com/google/maxtext/blob/main/docs/run_maxtext/run_maxtext_localhost.md | Pre-training / Local Execution | TPU / GPU | TPU v4 / TPU v5p / NVIDIA H100 / NVIDIA B200 | MaxText, JAX, Grain, Orbax | 8 | 2x4* |
| https://github.com/google/maxtext/blob/main/docs/run_maxtext/run_maxtext_single_host_gpu.md | Pre-training / GPU Single-Host Execution | GPU | NVIDIA H100 | MaxText, JAX, Cluster Toolkit, GKE | 8 | single-host |
| https://github.com/google/maxtext/blob/main/docs/run_maxtext/run_maxtext_via_cluster_toolkit.md | Pre-training / Orchestration | TPU | TPU v5p / TPU v6e | MaxText, JAX, Cluster Toolkit, GKE | 128 | 4x4x4 |
| https://github.com/google/maxtext/blob/main/docs/run_maxtext/run_maxtext_via_multihost_job.md | Pre-training / Multihost Execution | TPU | TPU v4 / TPU v5p / TPU v6e | MaxText, JAX | 8 | 2x4* |
| https://github.com/google/maxtext/blob/main/docs/run_maxtext/run_maxtext_via_multihost_runner.md | Pre-training / Multihost Runner Execution | TPU | TPU v4 | MaxText, JAX, Multihost Runner | 8 | 2x4* |
| https://github.com/google/maxtext/blob/main/docs/run_maxtext/run_maxtext_via_pathways.md | Pre-training / Distributed Execution | TPU | TPU v5p / TPU v6e | MaxText, JAX, Pathways, Cluster Toolkit, GKE | 64 | 4x4x4 |
| https://github.com/google/maxtext/blob/main/docs/run_maxtext/run_maxtext_via_xpk.md | Pre-training / Orchestration | TPU / GPU | TPU v5p / NVIDIA H100 | MaxText, JAX, XPK, Cluster Toolkit, GKE | 32 | 4x4* |
| https://github.com/google/maxtext/blob/main/docs/tutorials/build_maxtext.md | Infrastructure Setup / Container Build | TPU / GPU | TPU v5e / TPU v5p / TPU v6e / NVIDIA H100 | MaxText, JAX, Docker, XPK, Cluster Toolkit, GKE | 8 | 2x4* |
| https://github.com/google/maxtext/blob/main/docs/tutorials/inference.md | Inference | TPU | TPU v6e / Trillium | MaxText, JAX, vLLM | 8 | 2x4 |
| https://github.com/google/maxtext/blob/main/docs/tutorials/posttraining/dpo.md | DPO | TPU | TPU v5p / TPU v6e | MaxText, JAX, Tunix | 8 | 2x4* |
| https://github.com/google/maxtext/blob/main/docs/tutorials/posttraining/full_finetuning.md | SFT / Full Fine-tuning | TPU | TPU v5p / TPU v6e | MaxText, JAX, Grain | 8 | 2x4* |
| https://github.com/google/maxtext/blob/main/docs/tutorials/posttraining/knowledge_distillation.md | Knowledge Distillation | TPU | TPU v5p / TPU v6e | MaxText, JAX, Tunix, vLLM, PyTorch, Orbax, XPK, GKE | 128 | 4x4x4 |
| https://github.com/google/maxtext/blob/main/docs/tutorials/posttraining/lora.md | SFT / LoRA | TPU | TPU v5p / TPU v6e | MaxText, JAX, Tunix, Orbax | 8 | 2x4* |
| https://github.com/google/maxtext/blob/main/docs/tutorials/posttraining/lora_on_multi_host.md | SFT / LoRA Multihost | TPU | TPU v6e / Trillium | MaxText, JAX, Tunix, Pathways, Orbax, XPK, GKE | 256 | 16x16* |
| https://github.com/google/maxtext/blob/main/docs/tutorials/posttraining/multimodal.md | Pre-training / SFT / Multimodal | TPU | TPU v5p | MaxText, JAX, Grain, PyTorch, Orbax | 16 | 2x2x4* |
| https://github.com/google/maxtext/blob/main/docs/tutorials/posttraining/native_lora.md | SFT / LoRA | TPU | TPU v5p / TPU v6e | MaxText, JAX, Orbax | 8 | 2x4* |
| https://github.com/google/maxtext/blob/main/docs/tutorials/posttraining/rl.md | RL/GRPO | TPU | TPU v5p / TPU v6e | MaxText, JAX, Tunix, vLLM | 8 | 2x4* |
| https://github.com/google/maxtext/blob/main/docs/tutorials/posttraining/rl_gemma4_26b.md | RL/GRPO | TPU | TPU v6e / Trillium | MaxText, JAX, Tunix, Pathways, XPK, GKE | 64 | 4x4x4 |
| https://github.com/google/maxtext/blob/main/docs/tutorials/posttraining/rl_gemma4_e4b.md | RL/GRPO | TPU | TPU v6e / Trillium | MaxText, JAX, Tunix, Pathways, XPK, GKE | 32 | 4x8 |
| https://github.com/google/maxtext/blob/main/docs/tutorials/posttraining/rl_gptoss_20b.md | RL/GRPO | TPU | TPU v5p | MaxText, JAX, Tunix, Pathways, XPK, GKE | 64 | 4x4x4* |
| https://github.com/google/maxtext/blob/main/docs/tutorials/posttraining/rl_on_multi_host.md | RL/GRPO Multihost | TPU | TPU v5p | MaxText, JAX, Tunix, vLLM, Pathways, XPK, GKE | 128 | 4x4x4* |
| https://github.com/google/maxtext/blob/main/docs/tutorials/posttraining/rl_qwen3_30b.md | RL/GRPO | TPU | TPU v5p / TPU v6e | MaxText, JAX, Tunix, Pathways, XPK, GKE | 64 | 4x4x4* |
| https://github.com/google/maxtext/blob/main/docs/tutorials/posttraining/sft.md | SFT | TPU | TPU v5p / TPU v6e | MaxText, JAX, Tunix | 8 | 2x4* |
| https://github.com/google/maxtext/blob/main/docs/tutorials/posttraining/sft_on_multi_host.md | SFT Multihost | TPU | TPU v5p / TPU v6e | MaxText, JAX, Tunix, Pathways, XPK, GKE | 256 | 16x16* |
| https://github.com/google/maxtext/blob/main/docs/tutorials/pretraining.md | Pre-training | TPU | TPU v2 / TPU v4 / TPU v5p / TPU v6e | MaxText, JAX, Grain | 8 | 2x4* |
| https://github.com/google/maxtext/blob/main/src/maxtext/configs/README.md | Pre-training / Configuration Reference | TPU | TPU v4 / TPU v5e / TPU v5p | MaxText, JAX, Cluster Toolkit, GKE | 8 | 2x4* |
| https://github.com/google/maxtext/blob/main/src/maxtext/eval/README.md | Evaluation | TPU | TPU v6e / Trillium | MaxText, JAX, vLLM, Orbax | 8 | 2x4* |
| https://github.com/google/maxtext/blob/main/src/maxtext/experimental/agent/ckpt_conversion_agent/README.md | Checkpoint Conversion Agent | TPU / GPU | TPU v5p / TPU v6e / NVIDIA H100 | MaxText, JAX, Orbax, LangChain | 8 | 2x4* |
| https://github.com/google/maxtext/blob/main/src/maxtext/experimental/omni_pipeline/README.md | Pre-training / Multimodal Pipeline | TPU | TPU v5p / TPU v6e | MaxText, JAX | 8 | 2x4* |
| https://github.com/google/maxtext/blob/main/src/maxtext/experimental/rl/README.md | RL/GRPO | TPU | TPU v5p | MaxText, JAX, Pathways, XPK, GKE | 256 | 8x8x4* |
| https://github.com/google/maxtext/blob/main/src/maxtext/inference/jetstream_pathways/README.md | Inference Server Deployment | TPU | TPU v5e / TPU v5p / TPU v6e | MaxText, JetStream, Pathways | 8 | 2x4* |
| https://github.com/google/maxtext/blob/main/src/maxtext/inference/maxengine/maxengine_server_deployment/README.md | Inference Server Deployment | TPU | TPU v5e / TPU v5p / TPU v6e | MaxEngine, JetStream, MaxText | 8 | 2x4* |
| https://github.com/google/maxtext/blob/main/src/maxtext/inference/mlperf/README.md | Inference / MLPerf Benchmarking | TPU | TPU v4 / TPU v5e / TPU v5p / TPU v6e | MaxText, JAX, MLPerf, Orbax | 8 | 2x4 |
| https://github.com/google/maxtext/blob/main/src/maxtext/trainers/post_train/distillation/README.md | Knowledge Distillation | TPU | TPU v5p | MaxText, JAX, Tunix, Grain, XPK, GKE | 16 | 4x4x4 |
| https://github.com/google/maxtext/blob/main/src/maxtext/trainers/pre_train/scripts/olmo/README.md | Pre-training Launcher | TPU | TPU v5p / TPU v6e | MaxText, JAX, Grain, PyTorch, Orbax, XPK | 256 | 4x8x8 |
| https://github.com/google/maxtext/blob/main/tests/end_to_end/gpu/te/README.md | Benchmarking / Pre-training | GPU | NVIDIA H100 | MaxText, JAX, TransformerEngine | 8 | single-host |
| https://github.com/google/maxtext/blob/main/tests/end_to_end/tpu/deepseek/Run_DeepSeek.md | Pre-training / End-to-End Test | TPU | TPU v4 / TPU v5p | MaxText, JAX, Grain, Pathways, Orbax | 256 | 8x8x4* |
| https://github.com/google/maxtext/blob/main/tests/end_to_end/tpu/gemma3/Run_Gemma3.md | Pre-training / End-to-End Test | TPU | TPU v5p / TPU v6e | MaxText, JAX, Grain | 8 | 2x4* |
| https://github.com/google/maxtext/blob/main/tests/end_to_end/tpu/gemma4/Run_Gemma4.md | Pre-training / Inference Test | TPU | TPU v5p | MaxText, JAX, Grain, Orbax, vLLM | 8 | 2x4* |
| https://github.com/google/maxtext/blob/main/tests/end_to_end/tpu/gpt_oss/run_gpt_oss.md | Pre-training / End-to-End Test | TPU | TPU v5p | MaxText, JAX, Grain, Orbax | 8 | 2x4* |
| https://github.com/google/maxtext/blob/main/tests/end_to_end/tpu/kimi/Run_Kimi.md | Pre-training / End-to-End Test | TPU | TPU v3 / TPU v4 / TPU v5p | MaxText, JAX, Grain, Orbax | 8 | 2x4* |
| https://github.com/google/maxtext/blob/main/tests/end_to_end/tpu/llama4/Run_Llama4.md | Pre-training / End-to-End Test | TPU | TPU v5p | MaxText, JAX, PyTorch | 128 | 4x4x4* |
| https://github.com/google/maxtext/blob/main/tests/end_to_end/tpu/qwen/dense/run_qwen2.5_dense.md | Pre-training / End-to-End Test | TPU | TPU v5p / TPU v6e | MaxText, JAX | 8 | 2x4* |
| https://github.com/google/maxtext/blob/main/tests/end_to_end/tpu/qwen/moe/run_qwen_moe.md | Pre-training / End-to-End Test | TPU | TPU v5p | MaxText, JAX, Grain | 512 | 8x8x8* |
| https://github.com/google/maxtext/blob/main/tests/end_to_end/tpu/qwen/next/run_qwen3_next.md | Pre-training / End-to-End Test | TPU | TPU v5p | MaxText, JAX, Grain, Orbax | 64 | 4x4x4* |
