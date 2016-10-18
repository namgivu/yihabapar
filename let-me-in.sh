#!/usr/bin/env bash

UTIL_HOME="/path/to/UTIL_HOME"
UTIL_HOME="/home/namgivu/NN/code/django-start/util"
#UTIL_HOME="./util"

u="https://github.com/namgivu/yihabapar/archive/master.zip" ;
t="/tmp/namgivu.yihabapar" ;
o="$t/master.zip" ;

rm -rf $t ; mkdir -p $t ;
wget $u -O $o ; unzip $o -d $t ;
mv $t/yihabapar-master/* $UTIL_HOME ; rm -rf $t ;
echo ; echo $UTIL_HOME ; ls -lA $UTIL_HOME
