#!/bin/bash
#This script installs all deps. It can be ran in a virtualenv

DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null && pwd )"
cd "$DIR"

#download model
wget -nc https://github.com/freethenation/sentimental_nlp/releases/download/v0.1.0/model.bin

#install deps
pip install numpy scipy flask pybind11 waitress
cd fastText
make
pip install .

