def repeat_twice (func):
    def wrapper (parameter):
        func(parameter)
        func(parameter)
    return wrapper

@repeat_twice
def greetings (name):
    print(f"Hola {name}")

greetings("Andrés")