import sys

from yavpm import fs, git

TEST_URL = "https://github.com/preservim/nerdcommenter.git"

##terminal & cli commands to replicate each other
##create a commands list, preferrably in linked list/map
##future: commands.py
if len(sys.argv - 1) == 0:
    ##todo:
    ##drop into terminal to run commands
    ##future: terminal.py
    pass
else:
    ##todo:
    ##parse commands to have actions
    ##future: commandline.py
    pass

test_proj = git.Project(TEST_URL)
test_fs = fs.Project(test_proj.project_name)
if test_fs.already_installed:
    print(test_proj.project_name + " is already installed")
else:
    test_proj.clone()
    test_fs.write_file()
