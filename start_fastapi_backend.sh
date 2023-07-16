#!/usr/bin/sh

cd fastapi

python -m venv .venv
. .venv/bin/activate
pip install -r requirements.txt
python main.py
