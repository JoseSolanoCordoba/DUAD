
def odd_elimination(list):
    for index, value in enumerate(list):
        if value % 2 != 0:
            list.pop(index)
    print("Lista final:\n", f"{list}")

if __name__ == '__main__':
    my_list = []

    list_length = int(input("Ingrese el tamaño de la lista de números deseado:\n"))
    for index in range(0,list_length):
        my_list.append(index)

    print("Lista inicial:\n", f"{my_list}")
    odd_elimination(my_list)