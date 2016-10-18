#!/usr/bin/python
from init import *
from ext_clone import gitRepos

#parse active git repo as 1st cmd's arg
activeGitRepo = get_arg('-activeGitRepo', default=gitRepos.keys()[0])

#params
REMOVED_EXT='ext/{activeGitRepo}'.format(activeGitRepo=activeGitRepo)

#do remove ext repo via git submodule removal ref. http://stackoverflow.com/a/16162000/248616
sh='git -C {APP_HOME} submodule deinit -f {REMOVED_EXT} ; ' \
   'git -C {APP_HOME} rm -f {REMOVED_EXT} ; ' \
   'rm -rf {APP_HOME}/.git/modules/{REMOVED_EXT}'.format(REMOVED_EXT=REMOVED_EXT, APP_HOME=APP_HOME)

print 'Removing submodule...'
print

run_bash(sh)

print
print sh
print 'Removing submodule... DONE'