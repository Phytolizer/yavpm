import sys
## Question:
## To import terminal from yavpm how do I include the Terminal class into the yavpm
from yavpm import commandline, fs, git, terminal

TEST_URL = "https://github.com/preservim/nerdcommenter.git"

##terminal & cli commands to replicate each other
##they will each call commands.py
if len(sys.argv) - 1 == 0:
    ##todo:
    ##drop into terminal to run commands
    ##future: terminal.py
    # terminal.repl()
		# couldn't import Terminal if the class isn't named "Project" in terminal.py
		terminal.Project.repl()
    ##pass
else:
    ##todo:
    ##parse commands to have actions
    ##future: commandline.py
    # commandline.run(sys.argv[1:])
    pass

test_proj = git.Project(TEST_URL)
test_fs = fs.Project(test_proj.project_name)
if test_fs.already_installed:
    print(test_proj.project_name + " is already installed")
else:
    test_proj.clone()
    test_fs.write_file()
