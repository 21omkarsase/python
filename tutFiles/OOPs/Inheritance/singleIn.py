from mimetypes import init


class Employee:
    no_of_leaves = 10

    def __init__(self, xname, xage, xcollege):
        self.name = xname
        self.age = xage
        self.college = xcollege

    def printDetails(self):
        return f"name is {self.name} , age is {self.age} , college is {self.college} and no of leaves is {self.no_of_leaves}"

    @staticmethod
    def printCompanyName(compName):
        print(compName)

    @classmethod
    def change_leaves(cls, newLeaveNo):
        cls.no_of_leaves = newLeaveNo

    @classmethod
    def from_str(cls, string):
        # params = string.split("-")
        # return cls(params[0], params[1], params[2])
        return cls(*string.split("-"))


class Programmer(Employee):
    no_of_holidays = 20

    def __init__(self, xname, xage, xcollege, xlanguage):
        self.name = xname
        self.age = xage
        self.college = xcollege
        self.language = xlanguage

    def printProgDetails(self):
        return f"I'm a {self.language} programmer and my name is {self.name} , I'm  {self.age} years old."


omkar = Employee("omkar", 20, "PCE")
sairaj = Employee("sairaj", 20, "Terna")
rohan = Employee.from_str("rohan-20-DY Patil")

binod = Programmer("binod", 25, "TU", "Python")
print(binod.printProgDetails())
print(binod.printDetails())
print(Programmer.no_of_holidays)
