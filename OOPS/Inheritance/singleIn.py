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
        super().__init__(xname,xage,xcollege)
        self.language = xlanguage

    def printProgDetails(self):
        return f"I'm a {self.language} programmer and my name is {self.name} , I'm  {self.age} years old."



binod = Programmer("binod", 25, "TU", "Python")
print(binod.printProgDetails())
print(binod.printDetails())
print(Programmer.no_of_holidays)


print(binod.name)

# ***********************************


class Player:
    no_of_games = 3
    var = 11

    def __init__(self,game,gameName):
        self.game = game
        self.gameName = gameName

    def printPlayerDetails(self):
        return f"name is {self.gameName} and the game is {self.game}"

class Employee(Player):
    no_of_leaves = 10

    def __init__(self, name, age, college,game,gameName):
        super().__init__(game,gameName)
        self.name = name
        self.age = age
        self.college = college

    def printDetails(self):
        return f"name is {self.name} , age is {self.age} , college is {self.college} and no of leaves is {self.no_of_leaves}"


class CoolProgrammer(Employee):
    def __init__(self,name,age,college,role,game,gameName):
        super().__init__(name,age,college,game,gameName)
        self.role=role
        
    def printProgDetails(self):
        print(f"{self.name},{self.role},{self.age},{self.college}")
        

omkar = CoolProgrammer("Omkar", 20, "PCE","SDE","Cricket","IPL")
print(omkar.printDetails())
print(omkar.printPlayerDetails())
print(omkar.var)

print(omkar.printProgDetails())