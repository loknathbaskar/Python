import json

#JSON input: 
x = '{ "name":"John", "age":30, "city":"Chicago", "country":"USA" }'

#parse json:
y = json.loads(x)

# the result is a Python dictionary:
print(y["age"], y["country"])

