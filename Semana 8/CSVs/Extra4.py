import csv

def read_csv_file(file_path, developer):
    try:
        with open(file_path, newline='', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            print(f"Videojuegos desarrollador por {developer}")
            for row in reader:
                if row['Desarrollador'] == developer:
                    print(f"-{row['Nombre']} (Clasificación: {row['ESRB']}, Género: {row['Género']})")

    except FileNotFoundError:
        print(f"Error: File '{file}' not found.")

def main():
    path = "..\\Curso Lyfter\\Semana 8\\CSVs\\VideoGames.csv"
    try:
        developer = input("Ingrese el desarrollador deseado:\n")
        read_csv_file(path, developer)
    except Exception as ex:
            print(ex)
            exit()

if __name__ == '__main__':
    main()
    