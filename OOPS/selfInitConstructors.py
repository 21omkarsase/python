class Employee:
    no_of_leaves = 10

    def __init__(self, xname, xage, xcollege):
        self.name = xname
        self.age = xage
        self.college = xcollege

    def printDetails(self):
        return f"name is {self.name} , age is {self.age} , college is {self.college} and no of leaves is {self.no_of_leaves}"


omkar = Employee("omkar", 20, "PCE")
# omkar.name = "omkar"
# omkar.college = "PCE"
# omkar.age = 20
omkar.age = 21
omkar.no_of_leaves = 1
print(omkar.printDetails())
sairaj = Employee("sairaj", 20, "Terna")
# sairaj.name = "sairaj"
# sairaj.college = "Terna"
# sairaj.age = 20
print(sairaj.printDetails())
