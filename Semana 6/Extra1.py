def count_character(my_text, my_char):
    return my_text.count(my_char) 

if __name__ == '__main__':
    requested_text = input("Ingrese el texto\n")
    char_to_find = input("Ingrese el carácter que desea buscar\n")
    print(f"El carácter buscado se ha encontrado {count_character(requested_text, char_to_find)} veces")