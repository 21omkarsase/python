class Student:
	school_name="MHDK"
	def __init__(self,name,age):
		self.name=name
		self.age=age
	
	def get_name(self):
		return self.name
	
	def set_name(self,name):         #instance method
		self.name=name
	
	@classmethod                      #for class method
	def get_school_name(cls):         #static method
		return cls.school_name
	
	@staticmethod	                 #for static method
	def info():                      #static method
		return "this is student class..."

		

s1=Student("omkar",20)
print(s1.name,s1.age)

s1.set_name("omkarsase")

print(s1.get_name())

print(Student.get_school_name())         #calling class method

print(Student.info())                    #calling static method
