class Rectangle():
	def __init__(self, height, width):
		self.height = height
		self.width = width

	def get_area(self):
		return self.height*self.width
	
	def get_perimeter(self):
		return (self.height+self.width)*2

def get_dimensions():
	while(True):
		try:
			height = int(input("Enter the height:\n"))
			width = int(input("Enter the width:\n"))
			if height<0 or width<0:
				raise ValueError
			else:
				break
		except ValueError as ex:
			print(ex)
			print("Enter only numbers and non negative ones")
	return height, width

height, width = get_dimensions()

rectangle_1 = Rectangle(height, width)

print(f"The rectangle area is: {rectangle_1.get_area()}")
print(f"The rectangle perimeter is: {rectangle_1.get_perimeter()}") 
