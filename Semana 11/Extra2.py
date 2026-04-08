class Car():
	def __init__(self, brand, model):
		self.brand = brand
		self.model = model
		self.speed = 0

	def accelerate(self):
		while(True):
			try:
				amount = int(input("Enter the amount wanted to accelerate:\n"))
				if not amount:
					raise ValueError
				else:
					break
			except ValueError as ex:
				print("Don't let empty data, enter only numbers")
		self.speed = self.speed + amount
		return 0
	
	def activate_break(self):
		while(True):
			try:
				amount = int(input("Enter the amount wanted to decrease speed:\n"))
				if not amount:
					raise ValueError
				else:
					break
			except ValueError as ex:
				print("Don't let empty data, enter only numbers")
		self.speed = self.speed - amount
		return 0

	def __str__(self):
		print(f"{self.brand} {self.model} - Speed: {self.speed} km/h")
		return 0

def get_features():
	while(True):
		try:
			brand = input("Enter the car brand:\n")
			model = input("Enter the car model:\n")
			if not brand or not model:
				raise ValueError
			else:
				break
		except ValueError as ex:
			print("Don't let empty data")
	return brand, model

def play_with_car():
	brand, model = get_features()
	car_1 = Car(brand, model)

	while(True):
		try:
			action = int(input("Choose an option:\n1. Accelerate\n2. Break\n0. Exit program\n"))
			if action not in {1,2,0}:
				raise ValueError
			elif action == 0:
				exit()
			elif action == 1:
				car_1.accelerate()
			elif action == 2:
				car_1.activate_break()
			car_1.__str__()

		except ValueError as ex:
			print("Enter a number only, and don't let an empty value")

play_with_car()
