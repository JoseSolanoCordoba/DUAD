my_list = []
memory = 0

for index in range(5):
    number = int(input(f"Ingrese el número #{index+1}:\n"))
    my_list.append(number)
		
    if index ==0:
        memory = number
        continue
    if number < memory:
        memory = number
        

print("La lista de números introducidos es:\n", f"{my_list}")
print("El valor más pequeño es:\n", f"{memory}")
