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


omkar = Employee("omkar", 20, "PCE")
omkar.age = 21
omkar.change_leaves(10)
print(omkar.no_of_leaves)
Employee.change_leaves(30)
print(omkar.printDetails())
sairaj = Employee("sairaj", 20, "Terna")
print(sairaj.printDetails())

rohan = Employee.from_str("rohan-20-DY Patil")
print(rohan.printDetails())
Employee.printCompanyName("VISION 11")

Employee.printCompanyName("STM11.ai")
omkar.printCompanyName("STM11.ai")
