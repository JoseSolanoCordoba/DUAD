def divide(number1, number2):
    if number2 == 0:
        raise ValueError("No se puede dividir por cero")
    return number1/number2

if __name__ == '__main__':
    my_list = [3, 20, 12, 5, 4] 