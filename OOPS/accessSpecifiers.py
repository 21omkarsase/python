class Employee:
    __privateAs = "I'm private"  # only class
    _protectedAs = "I'm  protected"  # class and subclass

    no_of_leaves = 10

    def __init__(self, xname, xage, xcollege):
        self.name = xname
        self.age = xage
        self.college = xcollege

    def printDetails(self):
        return f"name is {self.name} , age is {self.age} , college is {self.college} and no of leaves is {self.no_of_leaves}"


omkar = Employee("omkar", 20, "PCE")
print(omkar._protectedAs)  # for protected
print(omkar._Employee__privateAs)  # for private
