class Computer:
	def __init__(self):
		self.name="omkar"
	
	def update(self):
		self.name="omkar sase"
	
	def compare(self,other):
		return self.name==other.name
	
c1=Computer()
c2=Computer()

# c2.update()

print(c1.compare(c2))