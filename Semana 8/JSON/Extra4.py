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

def group_pokemons(pokemons_data):
    summary_dict = {}
    for pokemon_dict in pokemons_data:
        level = pokemon_dict.get("base").get("HP") + pokemon_dict.get("base").get("Attack") + pokemon_dict.get("base").get("Defense") + pokemon_dict.get("base").get("Sp. Attack") + pokemon_dict.get("base").get("Sp. Defense") + pokemon_dict.get("base").get("Speed")
        
        if summary_dict.get(pokemon_dict.get("type")[0]) is None:
            summary_dict[pokemon_dict.get("type")[0]] = {"level": level, "counter": 1, "average": level}
        else:
            summary_dict[pokemon_dict.get("type")[0]]["level"] = summary_dict.get(pokemon_dict.get("type")[0]).get("level") + level
            summary_dict[pokemon_dict.get("type")[0]]["counter"] += 1
            summary_dict[pokemon_dict.get("type")[0]]["average"] = summary_dict[pokemon_dict.get("type")[0]]["level"]/summary_dict[pokemon_dict.get("type")[0]]["counter"]

    return summary_dict

def show_summary(grouped_pokemons):
    for types in grouped_pokemons.keys():
        print(f"Tipo: {types} -> Promedio de nivel: {grouped_pokemons[types]["average"]}")

def main():
    json_file_path = "..\\Curso Lyfter\\Semana 8\\JSON\\pokemons.json"
    
    try:
        pokemon_data_list = read_json_file(json_file_path)
        grouped_pokemons = group_pokemons(pokemon_data_list)
        show_summary(grouped_pokemons)
    except Exception as ex:
            print(ex)
            exit()

if __name__ == '__main__':
    main()
    