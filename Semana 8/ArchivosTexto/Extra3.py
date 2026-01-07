def capitalize_letters(path):
    with open(path, 'r', encoding='utf-8') as my_file:
        my_file = my_file.read()
        upper_content = my_file.upper()
    return upper_content


def create_new_file(capital_letters):
    path = "..\\Curso Lyfter\\Semana 8\\capitalized_file.txt"
    with open(path, 'w') as new_file:
        new_file.write(capital_letters)


def main():
    path = "..\\Curso Lyfter\\Semana 8\\Songs.txt"
    try:
        capital_letters = capitalize_letters(path)
        create_new_file(capital_letters)
    except Exception as ex:
            print(ex)
            exit()

if __name__ == '__main__':
    main()
    