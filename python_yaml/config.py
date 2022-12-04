import yaml
import pprint

with open('example.yml') as file:
    data = yaml.full_load(file)
    pprint.pprint(data, indent=2)