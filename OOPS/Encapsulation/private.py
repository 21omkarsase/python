class FatherTest:
    def __init__(self, par1):
        self._className = "ParentTest"
        self._par1 = par1
        pass 
    
    def printClassName(self):
        print('father', self._className)
class MotherTest:
    def __init__(self, par3):
        self._className = "MotherTest"
        self._par3 = par3
        pass 
    
    def printClassName(self):
        print('mother', self._className)
    

class ChildTest(FatherTest, MotherTest):
    def __init__(self, par1, par2, par3):
        MotherTest.__init__(self, par3)
        FatherTest.__init__(self, par1)
        self._par2 = par2
        pass
	
    def printClassName(self):
        super().printClassName()
        MotherTest.printClassName(self)
        FatherTest.printClassName(self)
        
ct = ChildTest("par1", "par2", "par3")

ct.printClassName()

# # Private members are similar to protected members, the difference is that the class members declared private should neither be accessed outside the class nor by any base class. In Python, there is no existence of Private instance variables that cannot be accessed except inside a class.

# # However, to define a private member prefix the member name with double underscore “__”.


# # Python program to
# # demonstrate private members

# # Creating a Base class


# class Base:
# 	def __init__(self):
# 		self.a = "GeeksforGeeks"
# 		self.__c = "GeeksforGeeks"

# # Creating a derived class
# class Derived(Base):
# 	def __init__(self):

# 		# Calling constructor of
# 		# Base class
# 		Base.__init__(self)
# 		print("Calling private member of base class: ")
# 		print(self.__c)


# # Driver code
# obj1 = Base()
# print(obj1.a)

# # Uncommenting print(obj1.c) will
# # raise an AttributeError

# # Uncommenting obj2 = Derived() will
# # also raise an AtrributeError as
# # private member of base class
# # is called inside derived class

