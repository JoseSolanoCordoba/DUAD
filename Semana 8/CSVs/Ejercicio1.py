import csv

videogames_headers = (
	'Nombre',
	'Género',
	'Desarrollador',
	'ESRB',
)
def videogames_input():
    videogames_list = []
    try:
        games_quantity = int(input("Ingrese el número de videojuegos que deseas añadir:\n"))
    except ValueError:
        print("No has ingresado un número válido")
    for i in range(games_quantity):
        videogame_info = {}
        videogame_info['Nombre'] = input("Ingrese el nombre del juego:\n")
        videogame_info['Género'] = input("Ingrese el género del juego:\n")
        videogame_info['Desarrollador'] = input("Ingrese el nombre del desarrollador:\n")
        videogame_info['ESRB'] = input("Ingrese la clasificación del juego:\n") 
        videogames_list.append(videogame_info)
    return videogames_list

    
def write_csv_file(file_path, data, headers):
    with open(file_path, 'w', encoding='utf-8') as file:
        writer = csv.DictWriter(file, headers)
        writer.writeheader()
        writer.writerows(data)


def main():
    path = "..\\Curso Lyfter\\Semana 8\\CSVs\\VideoGames.csv"
    try:
        videogames_list = videogames_input()
        write_csv_file(path, videogames_list, videogames_headers)
    except Exception as ex:
            print(ex)
            exit()

if __name__ == '__main__':
    main()
    