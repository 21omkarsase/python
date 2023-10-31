class Employee:
    __email = "abcxyz123@gmail.com"  # only class
    _phoneNo = "7304289092"  # class and subclass

    no_of_leaves = 10

    def __init__(self, xname, xage, xcollege):
        self.name = xname
        self.age = xage
        self.college = xcollege
        
    def getEmail(self):
        return self.__email

    def printDetails(self):
        return f"name is {self.name} , age is {self.age} , college is {self.college} and no of leaves is {self.no_of_leaves}"


employee1 = Employee("omkar", 20, "PCE")

print(employee1.getEmail())