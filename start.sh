#!/bin/bash

SCRIPT_PATH=$(dirname "$(realpath "$0")")
. "$SCRIPT_PATH/.venv/bin/activate"
python "$SCRIPT_PATH/p1_influx_db/main.py"