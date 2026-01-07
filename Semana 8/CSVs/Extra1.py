import csv

def read_csv_file(file_path):
    with open(file_path, newline='', encoding='utf-8') as file:
        reader = csv.reader(file)
        headers = next(reader)
        for row in reader:
            for i, value in enumerate(row):
                print(f"  {headers[i]}: {value}")

def main():
    path = "..\\Curso Lyfter\\Semana 8\\CSVs\\VideoGames.csv"
    try:
        read_csv_file(path)
    except Exception as ex:
            print(ex)
            exit()

if __name__ == '__main__':
    main()
    