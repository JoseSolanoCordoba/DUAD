def count_vocals(my_text):
    number_of_vocals = 0
    for value in my_text:
        if value in ("a","e","i","o","u", "A","E","I","O",):
            number_of_vocals += 1
    return number_of_vocals

if __name__ == '__main__':
    requested_text = input("Ingrese el texto\n")
    print(f"El texto contiene {count_vocals(requested_text)} vocales")