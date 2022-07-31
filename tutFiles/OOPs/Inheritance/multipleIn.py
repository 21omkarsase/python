
class Employee:
    no_of_leaves = 10
    var = 10

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


class Player:
    no_of_games = 3
    var = 11

    def __init__(self, name, game):
        self.game = game
        self.gameName = name

    def printPlayerDetails(self):
        return f"name is {self.gameName} and the game is {self.game}"


class CoolProgrammer(Employee, Player):
    var = 13


omkar = Employee("omkar", 20, "PCE")
sairaj = Employee("sairaj", 20, "Terna")
rohan = Employee.from_str("rohan-20-DY Patil")

omkarPlayer = Player("storm", "Cricket")
print(omkarPlayer.printPlayerDetails())
omkarTheCoolProgrammer = CoolProgrammer("Omkar", 20, "PCE", "killer", "PUBG")
print(omkarTheCoolProgrammer.printDetails())
print(omkarTheCoolProgrammer.var)
