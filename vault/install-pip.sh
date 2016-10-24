#!/usr/bin/env bash

#preqreq. install python
SCRIPT_HOME="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
$SCRIPT_HOME/install-python.sh

#install pip
echo
echo "Installing pip..."
echo

  #download pip source code
  t=/tmp
  pushd `pwd` ; cd $t ; wget https://bootstrap.pypa.io/get-pip.py ; popd

  #install
  python $t/get-pip.py

  #get latest
  pip install -U pip ; pip --version

echo
echo "Installing pip... DONE"
