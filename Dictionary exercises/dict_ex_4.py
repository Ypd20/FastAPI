employees = ['Kelly', 'Emma']
defaults = {"designation": 'Developer', "salary": 8000}
defs= dict.fromkeys(employees, defaults)
print(defs)
print(defs["Kelly"])
