def single_line(path):
    try:
        with open(path, 'r', encoding='utf-8') as my_file:
            my_file = my_file.read()
            my_file = my_file.replace('\n', ' ')
            my_file = my_file.readlines()
            print(len(my_file))
    except FileNotFoundError:
            print(f"Error: File not found at {path}")
   


def main():
    path = "..\\Curso Lyfter\\Semana 8\\Songs.txt"
    try:
        single_line(path)
    except Exception as ex:
            print(ex)
            exit()

if __name__ == '__main__':
    main()
    