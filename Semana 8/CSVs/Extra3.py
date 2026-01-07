import csv

def read_csv_file(file_path):
    dict_types = {}
    try:
        with open(file_path, newline='', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                if not dict_types.get(row['Género']):
                    dict_types[row['Género']] = 0
                if len(dict_types) != 0:
                    dict_types[row['Género']] = dict_types[row['Género']] + 1
        print("Géneros encontrados:\n")
        for gen, number in dict_types.items():
            print(f'{gen} : {number}')
    except FileNotFoundError:
        print(f"Error: File '{file}' not found.")

def main():
    path = "..\\Curso Lyfter\\Semana 8\\CSVs\\VideoGames.csv"
    try:
        read_csv_file(path)
    except Exception as ex:
            print(ex)
            exit()

if __name__ == '__main__':
    main()
    