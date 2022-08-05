class Sublime:
	def execute(self):
		print("compiling")
		print("running")

class MyEditor:
	def execute(self):
		print("comiled and ran")

class Laptop:
	def code(self,ide):
		ide.execute()
	

# ide=Sublime()
ide=MyEditor()

code1=Laptop()
code1.code(ide)