# Python Object Oriented Programming by Joe Marini course example
# Using Abstract Base Classes to enforce class constraints

from abc import ABC,abstractmethod

class JSONify(ABC):
    @abstractmethod
    def toJSON(Self):
        pass

class GraphicShape(ABC):
    def __init__(self):
        super().__init__()
    @abstractmethod #override method in the child classes
    def calcArea(self):
        pass


class Circle(GraphicShape,JSONify):
    def __init__(self, radius):
        self.radius = radius
    def calcArea(self): 
        return 3.14 *(self.radius**2)
    def toJSON(self):
        return f"{{\"circle\": {str(self.calcArea())}}}"
       


class Square(GraphicShape):
    def __init__(self, side):
        self.side = side
    def calcArea(self):
        return self.side*self.side


#g = GraphicShape()

c = Circle(10)
print(c.calcArea())
#s = Square(12)
#print(s.calcArea())
print(c.toJSON())
