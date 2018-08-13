#!/usr/bin/python
"""
TODO::
1. Read configuraion for tool
2. Initiaize Git, RBT
3. review_id = Poll on Review Request()
a. rbt patch -c <review_id>
4. get changed files.
5. seperate files by extension
6. check secuirty issues in each filesby extension

"""
from git import Repo
from config import Configuration


CONFIG_PATH = "checker.json"

# Initialize config
c = Configuration(CONFIG_PATH)
c.read_config()

# Initialize Git repository
repo = Repo(c.cfg['git']['repo'])
origin = repo.remotes.origin
origin.pull()[0]

# Get changed files.
changedFiles = [ item.a_path for item in repo.index.diff(None) ]
for item in repo.untracked_files:
    changedFiles.append(item)

# seperate file data set
c_files = []
cpp_files = []
h_files = []
py_files = []
cpp_files = []
go_files = []
others = []

for item in changedFiles:
    if item.endswith('.c'):
        c_files.append(item)
    elif item.endswith('.cpp') or item.endswith('.cc'):
        cpp_files.append(item)
    elif  item.endswith('.h'):
        h_files.append(item)
    elif item.endswith('.py'):
        py_files.append(item)
    elif item.endswith('.go'):
        go_files.append(item)
    else:
        others.append(item)
#import pdb;pdb.set_trace()
#print changedFiles
