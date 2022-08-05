
class Employee:
    no_of_leaves = 10

    def __init__(self, name, age, college):
        self.name = name
        self.age = age
        self.college = college

    def printDetails(self):
        return f"name is {self.name} , age is {self.age} , college is {self.college} and no of leaves is {self.no_of_leaves}"



class Player:
    no_of_games = 3
    var = 11

    def __init__(self):
        self.game = "cricket"
        self.gameName = "IPL"

    def printPlayerDetails(self):
        return f"name is {self.gameName} and the game is {self.game}"


class CoolProgrammer(Employee, Player):
    def __init__(self,name,age,college,role):
        super().__init__(name,age,college)
        self.role=role
        
    def printProgDetails(self):
        print(f"{self.name},{self.role},{self.age},{self.college}")
        

omkar = CoolProgrammer("Omkar", 20, "PCE","SDE")
print(omkar.printDetails())
print(omkar.var)
print(omkar.printPlayerDetails())

# cp1=CoolProgrammer

