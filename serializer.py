import json

def serialize(object, file):
    with open(file, 'w') as f:
        json.dump(object, f, sort_keys=True)

def deserialize(file):
    with open(file, 'r') as f:
        data = json.load(f)
    return data