#!/usr/bin/env bash
#ref. http://unix.stackexchange.com/a/2691/17671

UTIL_HOME="/path/to/UTIL_HOME"

u="https://github.com/namgivu/yihabapar/archive/master.zip" ;
t="/tmp/namgivu.yihabapar" ;
o="$t/master.zip" ;

#prepare temp folder
rm -rf $t ; mkdir -p $t ;

#download & unpack code
wget $u -O $o ; unzip $o -d $t ;

#copy to destination & clean up temp
mv $t/yihabapar-master/* $UTIL_HOME ; rm -rf $t ;

#set up path on destination site
$UTIL_HOME/setup.sh

#print the outcome
echo ; echo $UTIL_HOME ; ls -lA $UTIL_HOME
