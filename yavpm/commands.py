import os, shutil
from yavpm import git
from yavpm.yavpm import dir
##from yavpm.__main__ import TEST_URL



def repl():
	while True:
		args = input("Please input command followed by argument:\n").split(" ") 
		if args[0] in exit_words(): break
		run_command(args)
		print("\n\n*****type exit, quit, or break to close input*****")
		print("\nWhat would you like to do next?")

def exit_words():
	return {
		"exit",
		"quit",
		"break"
	}

def run_command(args):	
	commands_list = command_list()
	possible_comamnd = args[0]
	if len(args) > 1 and possible_comamnd in commands_list:	
		commands_list[possible_comamnd](args[1])
	else:
		error(possible_comamnd)

def command_list():
	return {
		"add": add,
		"update": update,
		"remove": remove
	}

def error(arg):
	print(f"{arg} is not a valid command")

##dump into git.clone()
def add(project_name):
	test_proj = git.Project(project_name)
	test_proj.clone()
    ##pass

##possibly add git.pull() method
##update all projects installed
def update(project_name):
	test_proj = git.Project(project_name)
	test_proj.pull()


##take project_name and remove from installed
##update installed list of changes
def remove(project_name):
	project_dir = os.path.join(dir(), "start", project_name)
	if os.path.exists(project_dir):
		shutil.rmtree(project_dir)
	else:
		print("That file project isn't installed currently")

