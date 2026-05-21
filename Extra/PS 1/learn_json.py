import json

data = []

def dumper(dict_name, mode):
    data.append(dict_name)
    with open("person.json", mode) as file:
        json.dump(data, file, indent= 4 )


person1 = {
    "name": "Hardik",
    "age": 18,
    "city": "Bakani"
}

person2 = {
    "name": "Virat",
    "age": 37,
    "city": "Delhi"
}


dumper(person1, "a")
print(data)

dumper(person2, "a")
print(data)








    
