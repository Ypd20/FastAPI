import json 

sampleJson = {"id" : 1, "name" : "value2", "age" : 29}
sort=json.dumps(sampleJson, indent=4, sort_keys=True)
print(sort)