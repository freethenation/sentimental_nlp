#!/bin/bash
DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null && pwd )"
cd "$DIR"
pip install numpy scipy flask pybind11
cd fastText
make
pip install .
