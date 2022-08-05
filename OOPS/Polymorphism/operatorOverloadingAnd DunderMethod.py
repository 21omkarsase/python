class Employee:
    no_of_leaves = 10

    def __init__(self, xname, xage, xcollege):
        self.name = xname
        self.age = xage
        self.college = xcollege

    def printDetails(self):
        return f"name is {self.name} , age is {self.age} , college is {self.college} and no of leaves is {self.no_of_leaves}"
        
    def add(self,a:int,b:int)->int:
        return a+b
    
    def add(self,a:str,b:str)->str:
        return a+b
        
    def add(self,a:int,b:str)->str:
        return b
        
    def __floordiv__(self, other):
        return self.age//other.age

    def __add__(self, other):
        return self.age+other.age

    def __repr__(self):
        return f"Employee('{self.name}',{self.age},'{self.college}')"

    def __str__(self):
        return f"name is {self.name} , age is {self.age} , college is {self.college} and no of leaves is {self.no_of_leaves}"


omkar = Employee("omkar", 20, "PCE")
sairaj = Employee("sairaj", 50, "Terna")
rohan = Employee("rohan", 90, "Terna")
print(omkar+rohan)
print(omkar//rohan)

print(repr(omkar))
print(str(omkar))