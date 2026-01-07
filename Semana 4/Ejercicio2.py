def user_group(name, last_name, age):
    age = int(age)
    if age<3:
        grupo="Bebé"
    elif age<12:
        grupo="Niño"
    elif age<15:
        grupo="Adolescente"
    elif age<25:
        grupo="Adulto joven"
    elif age<60:
        grupo = "Adulto"
    else:
        grupo = "Adulto Mayor"

    print(f"Datos ingresados:",name, last_name,",","Edad:", age)
    print(f"Eres un {grupo}")


if __name__ == '__main__':
    name = input("Type your name\n")
    last_name = input("Type your last name\n")
    age = input("Type your age\n")


    user_group(name, last_name, age)