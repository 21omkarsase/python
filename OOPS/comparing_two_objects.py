class Computer:
	def __init__(self, name, age):
		self.name = name
		self.age = age
	
	def compare(self,other):
		return self.name==other.name and self.age == other.age
	
c1=Computer("omkar", 20)
c2=Computer("Sairaj", 20)


print(c1.compare(c2))