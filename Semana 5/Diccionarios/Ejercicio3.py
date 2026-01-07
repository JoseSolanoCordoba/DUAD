list_2eliminate = ["Losses", "Sales"]
dictionary = {
    "Building#": 1, 
    "Sales": "80%", 
    "Employees#": 22000, 
    "Losses": "2%", 
    "Expansion": 2028
    }
for value in list_2eliminate:
    dictionary.pop(value)

print(dictionary)