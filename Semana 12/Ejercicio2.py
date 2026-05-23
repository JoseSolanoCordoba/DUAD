from abc import ABC, abstractmethod
import math

class Shape(ABC):
    @abstractmethod
    def calculate_perimeter(self, amount):
        pass

    @abstractmethod
    def calculate_area(self, amount):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def calculate_perimeter(self):
        perimeter = 2*math.pi*self.radius
        print(f'Circle perimeter is: {perimeter}')

    def calculate_area(self):
        area = math.pi*math.pow(self.radius, 2)
        print(f'Circle area is: {area}')

class Square(Shape):
    def __init__(self, side):
        self.side = side

    def calculate_perimeter(self):
        perimeter = self.side*4
        print(f'Square perimeter is: {perimeter}')

    def calculate_area(self):
        area = self.side*self.side
        print(f'Square area is: {area}')

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def calculate_perimeter(self):
        perimeter = 2*self.length + 2*self.width
        print(f'Rectangle perimeter is: {perimeter}')

    def calculate_area(self):
        area = self.length*self.width
        print(f'Rectangle area is:{area}')

my_circle = Circle(5)
my_square = Square(3)
my_rectangle = Rectangle(4, 5)

my_circle.calculate_area()
my_rectangle.calculate_perimeter()
my_square.calculate_area()