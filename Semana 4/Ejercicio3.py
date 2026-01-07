import random
number = 0
random_number = 1

while(number!=random_number):
    random_number = random.randrange(1,10)
    number = int(input("Ingrese el número:\n"))
    
    
print("El número secreto fue adivinado y es:", random_number)