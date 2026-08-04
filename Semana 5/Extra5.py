my_list = []
reduced_list = []
word = 0

for index in range(5):
    word = input(f"Ingrese la palabra #{index+1}:\n")
    my_list.append(word)

reduced_list = [value for value in my_list if len(value)> 4]

print("La lista de palabras es:\n", f"{my_list}")
print("La lista de palabras con más de 4 letras es:\n", f"{reduced_list}")
