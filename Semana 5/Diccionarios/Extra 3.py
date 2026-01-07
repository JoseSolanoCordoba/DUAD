products = [
    {"name": "Monitor", "category": "Electrónica", "price": 200},
    {"name": "Teclado", "category": "Electrónica", "price": 50},
    {"name": "Silla", "category": "Muebles", "price": 120},
    {"name": "Mesa", "category": "Muebles", "price": 180},
    {"name": "Mouse", "category": "Electrónica", "price": 25},
]

result = {}

for dictionary in products:
        category = dictionary.pop("category")
        if result.get(category) == None:
            result[category] = dictionary.get("price")
            
        else:
            result[category] = result.get(category) + dictionary.get("price")
print(result)