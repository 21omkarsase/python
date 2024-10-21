#method overloading==>same function with different no. of arguments

from multipledispatch import dispatch
class Employee:
    no_of_leaves = 10

    def __init__(self, xname, xage, xcollege):
        self.name = xname
        self.age = xage
        self.college = xcollege

    @dispatch(int, int)
    def subtract(self, a, b):
        return a - b
    
    @dispatch(int, str)
    def subtract(self, a, b):
        return str(a) + str(b)
    
    @dispatch(str, int)
    def subtract(self, a, b):
        return str(a) + str(b)

    @dispatch(int, int, int)
    def subtract(self, a, b, c):
        return a - b - c

    def printDetails(self):
        return f"name is {self.name} , age is {self.age} , college is {self.college} and no of leaves is {self.no_of_leaves}"
        
    def add(self,a=None,b=None,c=None):
        if(a!=None and b!=None and c!=None):
            return a+b+c
        elif a!=None and b!=None:
            return a+b
        else:
            return a

omkar = Employee("omkar", 20, "PCE")


print(omkar.add(1,2,3))
print(omkar.add(1,2))
print(omkar.add(2))

print(omkar.subtract(2, 3))
print(omkar.subtract(2, 3, 4))
print(omkar.subtract(2, 'ds'))
print(omkar.subtract('ds', 33))
