#!/usr/bin/python
'''
Remove an external git repository previously added to a git repo
'''

def ext_remove(REMOVED_EXT):
  #region init util
  import sys, os
  UTIL_HOME='{SCRIPT_HOME}/..'.format(SCRIPT_HOME=os.path.abspath(os.path.dirname(__file__)) )
  sys.path.insert(0, UTIL_HOME)
  from util_init import *
  #endregion init util

  #do remove external repo via git submodule removal ref. http://stackoverflow.com/a/16162000/248616
  sh='git -C {APP_HOME} submodule deinit -f {REMOVED_EXT} ; ' \
     'git -C {APP_HOME} rm -f {REMOVED_EXT} ; ' \
     'rm -rf {APP_HOME}/.git/modules/{REMOVED_EXT}'.format(REMOVED_EXT=REMOVED_EXT, APP_HOME=APP_HOME)

  print sh
  #run_bash(sh)


if __name__ == "__main__": # when this file executed ref. http://stackoverflow.com/a/6523852/248616
  print 'Removing submodule...'
  print

  args=['REMOVED_EXT']
  ext_remove(REMOVED_EXT=get_arg('REMOVED_EXT', args) )

  print
  print 'Removing submodule... DONE'
