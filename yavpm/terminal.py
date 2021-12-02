from yavpm import commands

##going to add input method, similar to cin or scanf in cpp&c
##not sure to make into full class or just functions

class Project:
	def repl(self):
		self.input_var = input("Please input command followed by argument:\n") 
		self.parse()
		print(self.input_var)
	
	def parse(input_var):
		pass