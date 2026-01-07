import json
    
def read_json_file(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)
    except FileNotFoundError:
        print(f"Error: El archivo '{file_path}' no se encontró")
    except json.JSONDecodeError:
        print(f"Error: No se pudo decodificar JSON del path '{file_path}'. Verifique si el archivo es de formato JSON.")
    return data

def show_pokemons_data(pokemons_data):
    pokemon_list = []
    pokemon_type = input("Ingrese el tipo de Pokemón que desea buscar: \n")

    for pokemon_dict in pokemons_data:
        if pokemon_dict.get("type")[0] == pokemon_type:
            pokemon_list.append(pokemon_dict.get("name").get("english"))
    print("Los pokemones de ese tipo son: \n")
    for names in pokemon_list:
        print(f"{names}")

def main():
    json_file_path = "..\\Curso Lyfter\\Semana 8\\JSON\\pokemons.json"
    
    try:
        pokemon_data_list = read_json_file(json_file_path)
        show_pokemons_data(pokemon_data_list)
    except Exception as ex:
            print(ex)
            exit()

if __name__ == '__main__':
    main()
    