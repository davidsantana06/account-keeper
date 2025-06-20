#!/bin/bash

if [ ! -d ".venv-bash" ]; then
    python3 -m venv .venv-bash
    source .venv-bash/bin/activate
    pip install -r requirements.txt
else
    source .venv-bash/bin/activate
fi

python3 -m app
