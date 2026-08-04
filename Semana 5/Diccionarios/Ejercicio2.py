list_1 = ["Mascota", "Color", "Edad"]
list_2 = ["Perro", "Negro", "7 años"]
dictionary = {}

for index in range(len(list_1)):
    dictionary[list_1[index]] = list_2[index]

print(dictionary)