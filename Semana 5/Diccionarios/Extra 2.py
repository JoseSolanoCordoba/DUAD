employees = [
    {"name": "Carlos", "email": "carlos@empresa.com", "department": "Ventas"},
    {"name": "Ana", "email": "ana@empresa.com", "department": "TI"},
    {"name": "Luis", "email": "luis@empresa.com", "department": "Ventas"},
    {"name": "Sofía", "email": "sofia@empresa.com", "department": "RRHH"},
]

result = {}

for dictionary in employees:
        department = dictionary.pop("department")
        if result.get(department) == None:
            result[department] = []
            result[department].append(dictionary)
        else:
            result[department].append(dictionary)
print(result)