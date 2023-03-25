#!/bin/bash

echo "Installing Pip"
curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
python3 get-pip.py
rm get-pip.py filename

PIP_VERSION=$(pip3 --version)
echo "The pip version installed is: ${PIP_VERSION}" 

echo "Installing Virtual Environment Command"
pip install virtualenv

echo "Creating Virtual Environment"
virtualenv small_biz
source small_biz/bin/activate

echo "Installing requirements.txt into Virtual Environment"
pip install -r requirements.txt