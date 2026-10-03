# sneppx-bench

Public benchmark harness: SneppX vs PyTorch/ONNX on CPU.

## Build & Test

- Python: per-file pytest only: `python -m pytest tests/<file>.py -q`.
- CPU + NumPy only; no GPU assumptions; no CI workflow files (org policy).
- git remote: `github.com/SneppX/sneppx-bench` (public).
