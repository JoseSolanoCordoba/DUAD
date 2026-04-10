class Person():
	def __init__(self, name, age):
		print(f"You have created a person called {name} of {age} years old!")
		self.name = name
		self.age = age

class Bus():
    def __init__(self, max_passengers, passengers_list):
        self.max_passengers = max_passengers
        self.passengers_list = passengers_list
    def add_passenger(self, person):
        if len(self.passengers_list) + 1 > self.max_passengers:
            print("The bus is full now")
        else:
            self.passengers_list.append(person)
            print(f"Adding one more passenger, passengers in bus: {self.passengers_list}")
    
    def get_passenger_out(self):
        try:
            if self.passengers_list:
                self.passengers_list.pop()
                print(f"Taking one passenger out, remaining passengers: {self.passengers_list}")

            else:
                raise ValueError
        except ValueError:
            print("Can not get passengers out, bus is out of passengers")
        

person_1 = Person("José", 29)
person_2 = Person("Andrés", 24)
person_3 = Person("Paula", 26)

bus_one = Bus(10, [])

bus_one.add_passenger(person_1)
#bus_one.add_passenger(person_2)
#bus_one.add_passenger(person_3)
bus_one.get_passenger_out()
bus_one.get_passenger_out()