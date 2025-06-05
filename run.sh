#!/bin/bash
SCRIPT_PATH=$(dirname "$0")
source $SCRIPT_PATH/.venv/bin/activate
python3 $SCRIPT_PATH/main.py
