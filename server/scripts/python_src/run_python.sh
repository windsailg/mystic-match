#!/bin/bash

# echo 'running python script'

path=`pwd`
# echo ${path}

cd ${path}/server/scripts/python_src
# uv self update
# uv venv --python 3.9.21
source .venv/bin/activate
# uv sync
# python --version
uv run mode_vgg16.py $1
