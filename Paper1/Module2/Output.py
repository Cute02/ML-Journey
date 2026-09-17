import json
data = {'a': 1, 'b': 2, 'c': 3}
# Python object → JSON string
json_string = json.dumps(data)

# Python object → JSON file
with open("out.json", "w") as f:
    json.dump(data, f)


# JSON file → Python object
with open("out.json", "r") as f:
    data = json.load(f)
    
    # JSON string → Python object
    new = json.loads(json_string)
    for key in new:
        print(key)

    # print(new)
