def words_counter(path):
    try:
        with open(path, 'r', encoding='utf-8') as my_file:
            my_file = my_file.read()
            words_count = my_file.split()
            print(f"Este archivo contiene {len(words_count)} palabras")
    except FileNotFoundError:
            print(f"Error: File not found at {path}")

def main():
    path = "..\\Curso Lyfter\\Semana 8\\Songs.txt"
    try:
        words_counter(path)
    except Exception as ex:
            print(ex)
            exit()

if __name__ == '__main__':
    main()
    