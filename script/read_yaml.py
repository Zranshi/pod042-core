import yaml
import json

# from src.utils.dot_dict import DotDict

with open("docs/conf.yaml", "r") as f:
    temp = yaml.load(f.read())

with open("docs/conf.json", "r") as f:
    temp1 = json.load(f)

print(temp1)
print(temp)
print(temp == temp1)
