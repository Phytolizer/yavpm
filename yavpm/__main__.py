from sys import argv
## Question:
## To import terminal from yavpm how do I include the Terminal class into the yavpm
##from yavpm import commandline ##, fs, terminal
from yavpm.commands import repl, run_command

TEST_URL = "https://github.com/preservim/nerdcommenter.git"
## get rid of the first item in argv
argv.pop(0)
arg_count = len(argv)
if arg_count == 0:
	##terminal.repl()
    repl()
elif arg_count < 3:
    run_command(argv)
else:
    print("Too many arguments")