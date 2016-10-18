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


#region set up path on destination site

  #remove non-util assets
  pushd `pwd` ; cd $UTIL_HOME ; rm -rf README.md LICENSE .gitirnore ; popd

  #create util_config from template and clean up template
  t="$UTIL_HOME/util_config.template.py"
  c="$UTIL_HOME/util_config.py"
  cp -f $t $c ; rm -rf $t

  #get app home, app name ref. http://unix.stackexchange.com/a/6470/17671
  APP_HOME=`git rev-parse --show-toplevel`
  APP_NAME=`basename $APP_HOME`

  #fill in util_config ref. http://stackoverflow.com/a/525612/248616
  s="path/to/app/home" ; sed -i-e "s#$s#$APP_HOME#g" $c
  s="YOUR-APP-NAME"    ; sed -i-e "s#$s#$APP_NAME#g" $c

#endregion set up path on destination site


#print the outcome
echo ; echo $UTIL_HOME ; ls -lA $UTIL_HOME
