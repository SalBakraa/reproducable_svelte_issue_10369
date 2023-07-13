#!/usr/bin/sh

cd azure

python -m venv .venv
. .venv/bin/activate
pip install -r requirements.txt

pnpm i azure-functions-core-tools@4
pnpm func start
