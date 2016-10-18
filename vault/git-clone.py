#!/usr/bin/python
from init import *


#region params
sshkeyNN='/home/ubuntu/.ssh/namgivu-github-ssh'

gitRepos = {
  #repo for namgivu code for Maya 30-days Hackathon
  'namgivu': {'githubKey': sshkeyNN,
                'repoUrl':'git@github.com:namgivu/aos-maya.git',
                 'branch':'master',
              },

  #repo for hoangphuong demo for Maya 30-days Hackathon
  'hoangphuong': {'githubKey': sshkeyNN,
                    'repoUrl':'git@github.com:hoangphuong/personal_robot_abilities.git',
                     'branch':'master',
                  },
}

#parse active git repo as 1st cmd's arg
activeGitRepo = get_arg('-activeGitRepo', default=gitRepos.keys()[0])

gitRepo=gitRepos[activeGitRepo]
githubKey = gitRepo['githubKey']
repoUrl = gitRepo['repoUrl']
branch = gitRepo['branch']

GIT_SSH_COMMAND='GIT_SSH_COMMAND="ssh -i ''%s''"' % githubKey

CLONED_TO_NAME=activeGitRepo
CLONED_TO_DIR='/tmp/{APP_NAME}'.format(APP_NAME=APP_NAME)
CLONED_TO='{CLONED_TO_DIR}/{CLONED_TO_NAME}'.format(CLONED_TO_DIR=CLONED_TO_DIR, CLONED_TO_NAME=CLONED_TO_NAME)
#endregion params


#region do git clone

#region cloning
shGitClone='git -C {CLONED_TO_DIR} clone {repoUrl} -b {branch} {CLONED_TO_NAME}'.format(repoUrl=repoUrl, branch=branch,
                                                                                        CLONED_TO_DIR=CLONED_TO_DIR, CLONED_TO_NAME=CLONED_TO_NAME)
sh='rm -rf {CLONED_TO} ; ' \
   'mkdir -p {CLONED_TO} ; ' \
   '{GIT_SSH_COMMAND} ; ' \
   '{shGitClone}'.format(CLONED_TO=CLONED_TO,GIT_SSH_COMMAND=GIT_SSH_COMMAND, shGitClone=shGitClone)

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