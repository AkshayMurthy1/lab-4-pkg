from tests.geometry.shapes import *
from tests.geometry.utils import *

def demo():
    square_1 = Square(side = 5)
    circle_1 = Circle(radius = 10)
    #Print out area of a shape:
    print(f"Area of Square 1: {square_1.area()}")
    print(f"Area of Circle 1: {circle_1.area()}")
    #Print out summary dict
    print(area_stats(square_1,circle_1))
    