memory = 0

for _ in range(1,4):
    number = int(input("Ingrese el número:\n"))
    if number>memory:
        memory = number
    
print("El número mayor es:", memory)