from abc import ABC, abstractmethod
import math 

class Shape(ABC):
    @abstractmethod
    def area(self) -> float:
        '''Compute the area of the shape'''

class Square(Shape):
    def __init__(self,side:float):
        self.side = side
    def area(self)->float:
        return self.side**2
    
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def area(self)->float:
        return self.radius**2 * math.pi
    
class Rectangle(Shape):
    def __init__(self,height,width):
        self.height,self.width = height,width
    def area(self) -> float:
        return self.height*self.width