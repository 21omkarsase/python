class Student:
	def __init__(self,name,lap_name):
		self.name=name
		self.lap=self.Laptop(lap_name)
		
	def show(self):
		print(self.name)
		self.lap.show()
	
	class Laptop:
		def __init__(self,lap_name):
			self.lap_name=lap_name
		
		def show(self):
			print(self.lap_name)


s1=Student("omkar","hp")
print(s1.name)

lap_s1=Student.Laptop("dell")
s1.lap.show()
lap_s1.show()
print(lap_s1.lap_name)