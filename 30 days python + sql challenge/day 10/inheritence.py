class Vehicle:
    def __init__(self, type):
        self.type = type

class Car(Vehicle):
    def __init__(self, type, avgSpeed):
        super().__init__(type)

        self.speed = avgSpeed

    def printInfo(self):
        print("type : ", self.type)
        print("speed", self.speed)


c1 = Car("car", 60)

c1.printInfo()