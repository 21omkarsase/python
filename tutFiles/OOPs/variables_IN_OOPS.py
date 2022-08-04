class Employee:
    no_of_leaves = 10   #class variable

    def __init__(self, xname, xage, xcollege):
        self.name = xname            #instance variable
        self.age = xage              #instance variable
        self.college = xcollege      #instance variable


omkar = Employee("omkar", 20, "PCE")

print(Employee.no_of_leaves)  #10
omkar.no_of_leaves=1

Employee.no_of_leaves=20  #will not change no_of_leaves of omkar object

print(omkar.no_of_leaves)     #1
