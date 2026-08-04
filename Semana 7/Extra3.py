def add_list_values(list):
    result = 0.0
    for value in list:
        try:
            number = float(value)
            result += number
            print(f'<{value}> sumado correctamente')
        except ValueError as ex:
            print(f'Elemento inválido: <{value}>')
    return result



def main():

    my_list = ['45', 'word', 'another word', '3.4', '4.23', '5']
    try:
        print(f'"Total de la suma:" {add_list_values(my_list)}')

    except Exception as ex:
            print(ex)
            exit()

if __name__ == '__main__':
    main()
    