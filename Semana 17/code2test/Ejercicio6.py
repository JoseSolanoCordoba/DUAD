def ordering_words(my_string):
    my_list = my_string.split("-")
    my_list.sort()
    ordered_string = '-'.join(my_list)
    return ordered_string


if __name__ == '__main__':
    requested_string = input("Ingrese el string\n")
    print(ordering_words(requested_string))