@echo off
setlocal

if not exist ".venv-batch" (
    python -m venv .venv-batch
    call .venv-batch\Scripts\activate
    python -m pip install -r requirements.txt
) else (
    call .venv-batch\Scripts\activate
)

python -m app
