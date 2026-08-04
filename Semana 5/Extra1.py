def number_searching(list, number_searched):
    occurrences = 0
    for value in list:
        if value == number_searched:
            occurrences += 1
    print(f"El número {number_searched} aparece {occurrences} veces")

if __name__ == '__main__':
    my_list = []
    number = 0
    wanted_number = 0

    for index in range(10):
        number = int(input(f"Ingrese el número #{index+1}:\n"))
        my_list.append(number)

number_2search = int(input(f"Ingrese el número que desea buscar:\n"))
print("Lista ingresada:\n", f"{my_list}")
number_searching(my_list, number_2search)


