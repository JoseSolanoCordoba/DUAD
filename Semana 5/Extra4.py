my_list = []
reduced_list = []
number = 0
suma = 0
average = 0

for index in range(5):
    number = int(input(f"Ingrese el número #{index+1}:\n"))
    my_list.append(number)
    suma += number

if len(my_list) != 0:
    average = suma/len(my_list)

reduced_list = [value for value in my_list if value>average]

print(f"El promedio es {average}")
print("La lista de números introducidos es:\n", f"{my_list}")
print("La lista de valores mayores al promedio es:\n", f"{reduced_list}")
