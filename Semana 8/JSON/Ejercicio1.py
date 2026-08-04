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

def modify_json(pokemon_data_lst):
    new_pokemon_dict = {}
    pokemon_name = input("Ingresa el nombre del Pokemón que deseas añadir:\n")
    pokemon_type = input("Ingresa el tipo de Pokemón que deseas añadir:\n")
    try:
        pokemon_hpoints = int(input("Ingresa los HP del Pokemón que deseas añadir:\n"))
        pokemon_attack = int(input("Ingresa el attack del Pokemón que deseas añadir:\n"))
        pokemon_defense = int(input("Ingresa el defense del Pokemón que deseas añadir:\n"))
        pokemon_special_attack = int(input("Ingresa el sp attack del Pokemón que deseas añadir:\n"))
        pokemon_special_defense = int(input("Ingresa el sp defense del Pokemón que deseas añadir:\n"))
        pokemon_speed = int(input("Ingresa el speed del Pokemón que deseas añadir:\n"))
    except ValueError:
        print("No has ingresado un número válido")
    new_pokemon_dict["name"] = {"english": pokemon_name}
    new_pokemon_dict["type"] = [pokemon_type]
    new_pokemon_dict["base"] = {"HP": pokemon_hpoints, "Attack": pokemon_attack, "Defense": pokemon_defense, "Sp. Attack": pokemon_special_attack, "Sp. Defense": pokemon_special_defense, "Speed": pokemon_speed}
    pokemon_data_lst.append(new_pokemon_dict)
    return pokemon_data_lst

def create_json (path, data_dictionary):
    with open(path, "w") as json_file:
        json.dump(data_dictionary, json_file, indent=4)

def main():
    json_file_path = "..\\Curso Lyfter\\Semana 8\\JSON\\pokemons.json"
    
    try:
        pokemon_data_list = read_json_file(json_file_path)
        new_data = modify_json(pokemon_data_list)
        create_json(json_file_path, new_data)
    except Exception as ex:
            print(ex)
            exit()

if __name__ == '__main__':
    main()
    