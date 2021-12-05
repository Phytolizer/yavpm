import os, shutil
from yavpm import git
from yavpm.yavpm import dir

def repl():
	while True:
		args = input("Please input command followed by argument:\n").split(" ") 
		if args[0] in exit_words(): break
		run_command(args)
		print("\n\n*****type exit, break or quit to leave input*****")
		print("What would you like to do next?")

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
	if project_name == "all" or project_name == "":
		test_proj = git.Project("")
		for plugin in os.listdir(os.path.join(dir(), "start")):
			print(f"updating: {plugin}")
			print("*************************")
			test_proj.set_project_name(plugin)
			test_proj.pull()
		##pass
	else:	
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

