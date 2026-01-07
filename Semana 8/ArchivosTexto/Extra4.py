
def create_new_file(path, new_text):
    path = "..\\Curso Lyfter\\Semana 8\\append_file.txt"
    with open(path, 'a') as new_file:
        new_file.write(new_text)


def main():
    path = "..\\Curso Lyfter\\Semana 8\\new_file.txt"
    try:
        input_text = input("Ingrese su texto:\n")
        create_new_file(path, input_text)
    except Exception as ex:
            print(ex)
            exit()

if __name__ == '__main__':
    main()
    