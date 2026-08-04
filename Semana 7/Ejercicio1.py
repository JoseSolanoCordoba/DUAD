def ask_operation_number():
    operation_number = 0
    while(operation_number == 0):
        try:
            operation_number = int(input(f"\nIngrese el número de operación deseado\n 1: Suma\n 2: Resta\n 3: Multiplicación\n 4: División\n 5: Borrar resultado\n 6: Salir\n"))
            if operation_number < 1 or operation_number > 6:
                raise ValueError("Ingresaste un valor fuera del menú")
            
        except ValueError as ex:
            print("Ingrese un número de operación válido")
            print(f"{ex}\n")
            operation_number = 0
            
    return operation_number


def sum_numbers(actual_number = 0):
    flag = 0
    result = 0
    while(flag == 0):
        try:
            second_number = int(input(f"\nIngrese un número (+):\n"))
            result = actual_number + second_number
            flag = 1
        except ValueError as ex:
            print("Ingrese un número válido")
            print(f"{ex}\n")
            flag = 0
    return result


def sub_numbers(actual_number):
    flag = 0
    result = 0
    while(flag == 0):
        try:
            second_number = int(input(f"\nIngrese un número (-):\n"))
            result = actual_number - second_number
            flag = 1
        except ValueError as ex:
            print("Ingrese un número válido")
            print(f"{ex}\n")
            flag = 0
    return result


def product_numbers(actual_number):
    flag = 0
    result = 0
    while(flag == 0):
        try:
            second_number = int(input(f"\nIngrese un número (*):\n"))
            result = actual_number * second_number
            flag = 1
        except ValueError as ex:
            print("Ingrese un número válido")
            print(f"{ex}\n")
            flag = 0
    return result


def div_numbers(actual_number):
    flag = 0
    result = 0
    while(flag == 0):
        try:
            second_number = int(input(f"\nIngrese un número (/):\n"))
            result = actual_number / second_number
            flag = 1
        except ZeroDivisionError as ex:
            print("No se puede dividir entre cero, ingrese otro denominador\n")
            print(f"{ex}\n")
            flag = 0
        except ValueError as ex:
            print("Ingrese un número válido")
            print(f"{ex}\n")
            flag = 0
    return result


def main():
    actual_number = 0
    operation_number = 0
    print("""\n***************************
*************************** 
Bienvenido a la calculadora 
***************************
***************************\n""")
    try:
        print(f"\nNúmero actual: {actual_number}\n")
        actual_number = sum_numbers()
        while True:
            print(f"\nNúmero actual: {actual_number}\n")
            operation_number = ask_operation_number()
            if operation_number == 1:
                actual_number = sum_numbers(actual_number)
            elif operation_number == 2:
                actual_number = sub_numbers(actual_number)
            elif operation_number == 3:
                actual_number = product_numbers(actual_number)
            elif operation_number == 4:
                actual_number = div_numbers(actual_number)
            elif operation_number == 5:
                actual_number = 0
                print(f"\nNúmero actual: {actual_number}\n")
                actual_number = sum_numbers()
            else:
                exit()

    except Exception as ex:
            print(ex)
            exit()

if __name__ == '__main__':
    main()
    