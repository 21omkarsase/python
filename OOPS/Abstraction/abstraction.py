# Abstraction in python is defined as a process of handling complexity by hiding unnecessary information from the user. This is one of the core concepts of object-oriented programming (OOP) languages. 

# In Python, abstraction can be achieved by having/using abstract classes and methods in our programs.


# ABC ABSTRACT BASE CALSSES


from abc import ABC,abstractmethod

class Computer(ABC):
	@abstractmethod
	def process(self,laptop_name):
		pass
	
class Laptop1(Computer):
	def process(self,laptop_name):
		print(f"process is running on {laptop_name}")
	
class Laptop2(Computer):
	def process(self,laptop_name):
		print(f"process is running on {laptop_name}")
			

lap1=Laptop1()
lap1.process("hp")

lap2=Laptop2()
lap2.process("dell")
