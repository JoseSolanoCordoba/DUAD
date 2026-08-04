def convert_string_list_to_int(list):

    for value in list:
        try:
            name = int(value)   
            print(f'"{value}" convertido a {name}')
        except ValueError as ex:
            print(f'No se pudo convertir el elemento: "{value}"')




def main():

    my_list = ['45', 'word', 'another word', '3.4', '4.23', '5']
    try:
        convert_string_list_to_int(my_list)

    except Exception as ex:
            print(ex)
            exit()

if __name__ == '__main__':
    main()
    