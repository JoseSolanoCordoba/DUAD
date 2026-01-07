
def positive_number_verification(list):
    positive = 1
    for value in list:
        if value <= 0:
            print("Hay al menos un número negativo o cero")
            positive = 0
            break

    if positive ==1:
        print("Todos los números son positivos")

if __name__ == '__main__':
    my_list = []
    number = 0
    for index in range(10):
        number = int(input(f"Ingrese el número #{index+1}:\n"))
        my_list.append(number)

    positive_number_verification(my_list)
    
