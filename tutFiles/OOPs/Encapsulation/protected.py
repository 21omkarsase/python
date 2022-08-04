#protected member start with _ 
# Although the protected variable can be accessed out of the class as well as in the derived class(modified too in derived class), it is customary(convention not a rule) to not access the protected out the class body.

class ClassA:
	def __init__(self):
		self._className="ClassA"
	
	
class ClassB(ClassA):
	# def __init__(self):
		# self._className="ClassB"
	# 	pass
	def printDetails(self):	
		print(f"class name is {self._className}")
		

a=ClassA()
b=ClassB()

# Calling protected member
# Can be accessed but should not be done due to convention
print("Accessing protected member of obj1: ", a._className)
 
# Accessing the protected variable outside
print("Accessing protected member of obj2: ", b._className)

print(b.printDetails())