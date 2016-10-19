#!/usr/bin/python


#region init util
import sys, os
UTIL_HOME='{SCRIPT_HOME}/..'.format(SCRIPT_HOME=os.path.abspath(os.path.dirname(__file__)) )
sys.path.insert(0, UTIL_HOME)
from util_init import *
#endregion init util


def git_clone(gitRepo, CLONED_TO_DIR, CLONED_TO_NAME):
  CLONED_TO=os.path.join(CLONED_TO_DIR, CLONED_TO_NAME)

  #region do git clone

  #region cloning
  GIT_SSH_COMMAND='GIT_SSH_COMMAND="ssh -i {key}"'.format(key=gitRepo['key'])
  shGitClone='git -C {CLONED_TO_DIR} clone {repoUrl} -b {branch} {CLONED_TO_NAME}'.format(repoUrl=gitRepo['url'], branch=gitRepo['branch'],
                                                                                          CLONED_TO_DIR=CLONED_TO_DIR, CLONED_TO_NAME=CLONED_TO_NAME)
  sh='rm -rf {CLONED_TO} ; mkdir -p {CLONED_TO} ; ' \
     '{GIT_SSH_COMMAND}  ; {shGitClone}' \
     .format(CLONED_TO=CLONED_TO, GIT_SSH_COMMAND=GIT_SSH_COMMAND, shGitClone=shGitClone)

  print 'Cloning maya repo...'
  print
  run_bash(sh)
  print
  print sh
  print 'Cloning maya repo... DONE'
  #endregion cloning

  #region print last commit
  sh='ls -lA {CLONED_TO} ; git -C {CLONED_TO} log -n1'.format(CLONED_TO=CLONED_TO)

  print
  print 'Clone summary...'
  print
  run_bash(sh)
  print
  print sh
  print 'Clone summary... DONE'
  #endregion print last commit

  #endregion do git clone

if __name__=='__main__': #this file is executed ref. http://stackoverflow.com/a/419185/248616
  all=['url', 'branch', 'key', 'CLONED_TO_DIR', 'CLONED_TO_NAME']
  git_clone(gitRepo={'url'   : get_arg('url', all),
                     'branch': get_arg('branch', all),
                     'key'   : get_arg('key', all),
                     },
            CLONED_TO_DIR=get_arg('CLONED_TO_DIR', all),
            CLONED_TO_NAME=get_arg('CLONED_TO_NAME', all)
            )