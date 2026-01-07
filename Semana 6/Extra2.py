def modified_list(my_list, number):
    new_list = []
    for value in my_list:
        if len(value) > number:
            new_list.append(value)
    return new_list

if __name__ == '__main__':
    list_of_words = ["delfín", "array", "letter", "pseudocódigo", "uno", "dos", "tres", "cuatro"]
    number_of_letters = int(input("Ingrese el número de letras a superar\n"))

    print(modified_list(list_of_words, number_of_letters))