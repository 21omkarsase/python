class Student:
	def __init__(self, name, lap_name):
		self.name = name
		self.lap = self.Laptop(lap_name)
		
	def show(self):
		print(self.name)
		self.lap.show()
	
	class Laptop:
		def __init__(self, lap_name):
			self.lap_name = lap_name
		
		def show(self):
			print(self.lap_name)


s1=Student("omkar","hp")

# lap_s1=Student.Laptop("dell")
# lap_s1.show()

s1.show()
