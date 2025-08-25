# zoom-tldr-evals (fork)
## Quick start
python3 -m venv .venv && source .venv/bin/activate
pip install -U openai zstandard backoff rich tiktoken numpy pyyaml
export OPENAI_API_KEY="sk-..."; python scripts/eval_runner.py
## Artifacts
- JSON logs in `reports/`.
