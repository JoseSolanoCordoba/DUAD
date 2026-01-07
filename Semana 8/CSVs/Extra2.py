import csv

def read_csv_file(file_path, clasification):
    try:
        with open(file_path, newline='', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                if row['ESRB'] == clasification:
                    for header, value in row.items():
                        print(f"  {header}: {value}")
    except FileNotFoundError:
        print(f"Error: File '{file}' not found.")

def main():
    path = "..\\Curso Lyfter\\Semana 8\\CSVs\\VideoGames.csv"
    try:
        clasification = input("Ingrese la clasificación deseada:\n")
        read_csv_file(path, clasification)
    except Exception as ex:
            print(ex)
            exit()

if __name__ == '__main__':
    main()
    