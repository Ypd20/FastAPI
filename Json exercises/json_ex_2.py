import json

sampleJson = """{"key1": "value1", "key2": "value2"}"""
result=json.loads(sampleJson)
print(result['key2'])