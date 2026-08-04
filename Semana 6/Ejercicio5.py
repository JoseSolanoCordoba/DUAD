def case_evaluation(my_string):
    lower_case = 0
    upper_case = 0

    for char in my_string:
        if char.isupper():
            upper_case += 1
        if char.islower():
            lower_case += 1
    print(f"There's {upper_case} upper cases and {lower_case} lower cases")


if __name__ == '__main__':
    requested_string = input("Ingrese el string\n")
    case_evaluation(requested_string)