Dict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New york"
}
keys = ["name", "salary"]

for k in keys:
    Dict.pop(k)
print(Dict)