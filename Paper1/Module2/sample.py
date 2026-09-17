import json
data = {"name": "Alice", "Age": 20}
# Writing to json
with open("data.json", "w") as f:
    json.dump(data, f)
    # Converting json file to json str
    json_str = json.dumps(data)
    print(json_str)
    # Reading from json
with open("data.json", "r") as f:
    json_data = json.load(f)
    #print(json_data)
    # Converting json str to file
    json_str = '{"name": "Alice", "Age": 20}'
    data = json.loads(json_str)
    #print(data)
