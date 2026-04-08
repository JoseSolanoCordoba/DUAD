import math

class Circle():
    def get_area(self, radius):
        return math.pi*pow(radius,2)
    
circle_one = Circle()
print(circle_one.get_area(10))

