#!/usr/bin/python
'''
Clone an external git repository to sub folder inside another git repo
'''

def ext_clone(gitRepo, CLONED_TO):
  #region init util
  import sys, os
  UTIL_HOME='{SCRIPT_HOME}/..'.format(SCRIPT_HOME=os.path.abspath(os.path.dirname(__file__)) )
  sys.path.insert(0, UTIL_HOME)
  from util_init import *
  #endregion init util

  #region cloning
  GIT_SSH_COMMAND='GIT_SSH_COMMAND="ssh -i {key}"'.format(key=gitRepo['key'])
  shGitSubModule='git -C {APP_HOME} submodule add {repoUrl} {CLONED_TO}'.format(
    APP_HOME=APP_HOME,
    repoUrl=gitRepo['url'],
    CLONED_TO=CLONED_TO
  )
  sh='{GIT_SSH_COMMAND} ; {shGitSubModule}'.format(GIT_SSH_COMMAND=GIT_SSH_COMMAND, shGitSubModule=shGitSubModule)
  run_bash(sh)
  #endregion cloning

if __name__ == "__main__": # when this file executed ref. http://stackoverflow.com/a/6523852/248616
  print 'Cloning external repo...'
  print

  args=['url', 'branch', 'key', 'CLONED_TO']
  ext_clone(gitRepo={'url'   : get_arg('url', args),
                     'branch': get_arg('branch', args),
                     'key'   : get_arg('key', args),
                     },
            CLONED_TO=get_arg('CLONED_TO', args),
            )
  print
  print 'Cloning external repo... DONE'
