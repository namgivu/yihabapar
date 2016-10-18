#!/usr/bin/env bash

#ref. http://stackoverflow.com/a/246128/248616
SCRIPT_HOME="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

#remove non-util assets
pushd `pwd` ; cd $SCRIPT_HOME ; rm -rf README.md LICENSE .gitirnore ; popd

#create util_config from template and clean up template
t="$SCRIPT_HOME/util_config.template.py"
c="$SCRIPT_HOME/util_config.py"
cp -f $t $c ; rm -rf $t

#get app home, app name ref. http://unix.stackexchange.com/a/6470/17671
APP_HOME=`git rev-parse --show-toplevel`
APP_NAME=`basename $APP_HOME`

#fill in util_config ref. http://stackoverflow.com/a/525612/248616
s="path/to/app/home" ; sed -i-e "s#$s#$APP_HOME#g" $c
s="YOUR-APP-NAME"    ; sed -i-e "s#$s#$APP_NAME#g" $c

