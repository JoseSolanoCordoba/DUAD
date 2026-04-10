import math

class Circle():
    def __init__(self, radius):
        self.radius = radius
    def get_area(self):
        return math.pi*pow(self.radius,2)
    
circle_one = Circle(10)
print(circle_one.get_area())

