class Mammal:
    def mammal_info(self):
        print("Mammals give birth to live young.")

class WingedAnimal:
    def winged_info(self):
        print("Winged animals can flap their wings.")

class Bat(Mammal, WingedAnimal):
    pass

b1 = Bat()
b1.mammal_info()  
b1.winged_info()  