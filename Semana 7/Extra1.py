def request_name():
    name = ""
    while(name == ""):
        try:
            name = input(f"Ingrese su nombre: ")
            if name.isdigit():
                raise ValueError("El nombre no puede ser un número")
            
        except ValueError as ex:
            print(f"{ex}\n")
            print("Ingrese un nombre válido")  
            name = ""
            
    return name


def request_age():
    age = 0
    while(age == 0):
        try:
            age = int(input(f"Ingrese su edad: "))
        except ValueError as ex:
            print(f"{ex}\n")
            print("Ingrese un número válido")  
            age = 0
            
    return age


def main():

    try:
        print(f"Hola {request_name()}, su edad es {request_age()}")

    except Exception as ex:
            print(ex)
            exit()

if __name__ == '__main__':
    main()
    