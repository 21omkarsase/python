from abc import ABC, abstractclassmethod


class Shape(ABC):  # ABC O
    @abstractclassmethod
    def printArea(self):
        return 0


class Rectangle(Shape):
    type = "rectangle"
    sides = 4

    def __init__(self):
        self.length = 4
        self.breadth = 5

    def printArea(self):
        print(self.length*self.breadth)


rect = Rectangle()
rect.printArea()
