from abc import ABC, abstractmethod
import math

class Shape(ABC):
    @abstractmethod
    def calculate_perimeter(self):
        pass

    @abstractmethod
    def calculate_area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def calculate_perimeter(self):
        perimeter = 2*math.pi*self.radius
        return perimeter

    def calculate_area(self):
        area = math.pi*math.pow(self.radius, 2)
        return area
    
class Square(Shape):
    def __init__(self, side):
        self.side = side

    def calculate_perimeter(self):
        perimeter = self.side*4
        return perimeter
    
    def calculate_area(self):
        area = self.side*self.side
        return area
    
class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def calculate_perimeter(self):
        perimeter = 2*self.length + 2*self.width
        return perimeter
    
    def calculate_area(self):
        area = self.length*self.width
        return area

my_circle = Circle(5)
my_square = Square(3)
my_rectangle = Rectangle(4, 5)

print(f'Circle area is: {my_circle.calculate_area()}')
print(f'Rectangle perimeter is: {my_rectangle.calculate_perimeter()}')
print(f'Square area is: {my_square.calculate_area()}')

