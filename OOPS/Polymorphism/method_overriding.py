class Employee:
    def __init__(self, xname, xage, xcollege):
        self.name = xname
        self.age = xage
        self.college = xcollege

    def printDetails(self, abc):
        return f"name is {self.name} , age is {self.age} , college is {self.college}"


class Programmer(Employee):
    def __init__(self, xname, xage, xcollege, xlanguage):
        super().__init__(xname, xage, xcollege)
        self.language = xlanguage

    def printDetails(self):
        return f"I'm a {self.language} programmer and my name is {self.name} , I'm  {self.age} years old."



binod = Programmer("binod", 25, "TU", "Python")
print(binod.printDetails())
# print(binod.printDetails('abc')) # error

