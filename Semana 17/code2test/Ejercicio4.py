def revert_string(my_string):
    reverted_string = ""
    my_string = list(my_string)
    for char in range(len(my_string)-1, -1, -1):
        reverted_string += my_string[char]

    return reverted_string

if __name__ == '__main__':
    requested_string = input("Ingrese el string\n")
    print(revert_string(requested_string))