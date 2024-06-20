from abc import ABC, abstractmethod


class Shape(ABC):  # ABC O
    @abstractmethod
    def printArea(self):
        pass
        
    @property
    @abstractmethod
    def area(self):
        pass

class Rectangle(Shape):
    type = "rectangle"
    sides = 4

    def __init__(self):
        self.length = 4
        self.breadth = 5
    
    @property
    def area(self):
        return self.breadth * self.length

    def printArea(self):
        print(self.area)


rect = Rectangle()
rect.printArea()

# ss  = Shape() # can't be created
