#!/usr/bin/python
from init import *


#region params
sshkeyNN='/home/ubuntu/.ssh/namgivu-github-ssh'

gitRepos={
  #repo for hoangphuong demo for Maya 30-days Hackathon
  'hoangphuong': {'githubKey': sshkeyNN,
                    'repoUrl':'git@github.com:hoangphuong/personal_robot_abilities.git',
                     'branch':'master',
                 },
}

#parse active git repo as 1st cmd's arg
activeGitRepo = get_arg('-activeGitRepo', default=gitRepos.keys()[0])

gitRepo=gitRepos[activeGitRepo]
githubKey=gitRepo['githubKey']
repoUrl=gitRepo['repoUrl']

GIT_SSH_COMMAND='GIT_SSH_COMMAND="ssh -i ''%s''"' % githubKey

CLONED_TO='ext/{activeGitRepo}'.format(activeGitRepo=activeGitRepo)
#endregion params


#region cloning
shGitSubModule='git -C {APP_HOME} submodule add {repoUrl} {CLONED_TO}'.format(APP_HOME=APP_HOME, repoUrl=repoUrl, CLONED_TO=CLONED_TO)
sh='{GIT_SSH_COMMAND} ; ' \
   '{shGitSubModule}'.format(GIT_SSH_COMMAND=GIT_SSH_COMMAND, shGitSubModule=shGitSubModule)

if __name__ == "__main__": # stuff only to run when not called via 'import' here ref. http://stackoverflow.com/a/6523852/248616
  print 'Cloning external repo...'
  print

  run_bash(sh)

  print
  print sh
  print 'Cloning external repo... DONE'
#endregion cloning
