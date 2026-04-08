class Person():
	def __init__(self, name, age):
		print(f"You have created a person called {name} of {age} years old!")
		self.name = name
		self.age = age

class Bus():
    max_passengers = 2
    passengers_list = []
    def add_passenger(self, person):
        if len(self.passengers_list) + 1 > self.max_passengers:
            print("The bus is full now")
        else:
            self.passengers_list.append(person)
            print(f"Adding one more passenger, passengers in bus: {self.passengers_list}")
    
    def get_passenger_out(self):
        self.passengers_list.pop()
        print(f"Taking one passenger out, remaining passengers: {self.passengers_list}")

person_1 = Person("José", 29)
person_2 = Person("Andrés", 24)
person_3 = Person("Paula", 26)

bus_one = Bus()

bus_one.add_passenger(person_1)
bus_one.add_passenger(person_2)
bus_one.add_passenger(person_3)
bus_one.get_passenger_out()