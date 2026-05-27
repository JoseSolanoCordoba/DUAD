class Vehicle():
    def __init__(self, brand, year):
        self._brand = brand
        self._year = year

    def get_info(self):
        return f'{self._brand} ({self._year})'

class Car(Vehicle):
    def __init__(self, brand, year, typ, model, engine):
        super().__init__(brand, year)
        self._type = typ
        self._model = model
        self._engine = engine
    
    def get_info(self):
        return f'{self._brand} ({self._year}) - Type: {self._type} - Model: {self._model} {self._engine}'

class Motorcycle(Vehicle):
    def __init__(self, brand, year, typ, model, engine):
        super().__init__(brand, year)
        self._type = typ
        self._model = model
        self._engine = engine
    
    def get_info(self):
        return f'{self._brand} ({self._year}) - Type: {self._type} - Model: {self._model} {self._engine}'
    
vehicle1 = Car("Totoya", 2017, "SUV", "4Runner", "V6")
vehicle2 = Motorcycle("Yamaha", 2024,"Cross", "YZ", 450)
print(vehicle1.get_info())
print(vehicle2.get_info())