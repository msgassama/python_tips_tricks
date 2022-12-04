import pprint
pp = pprint.PrettyPrinter(indent=2)
import yaml
import json
document = """
  a: 1
  b:
    c: 3
    d: 4
    e:
     - 12
     - 24
     - 36
"""

demo = """
'apple': 'I am a red fruit'
'orange': 'I am a orange fruit'
'banana': 'I am a green fruit'
"""
print(yaml.dump(yaml.load(document, yaml.Loader)))
print(yaml.load(document, yaml.Loader))
print(yaml.load(demo, yaml.Loader))

with open('person.yaml') as person:
    john = yaml.full_load(person)
    pprint.pprint(john)
with open('person.json', 'w') as p:
    json.dump(john, p, indent=2, default=str)
    
li = [
    None, 
    'John', 
    'Jane', 
    'Smith',
    [
        {'nom': 'doe', 'prenom': 'John'},
        {'nom': 'doe', 'prenom': 'Jane'},
        {'nom': 'smith', 'prenom': 'John'},
    ],
    True,
    False,
    'good',
    'bad',
    {
        'maths': [12, 9, 25],
        "english":[17, 16, 19],
        "dba": [19, 20, 12],
        "tdo": ["A Bien", "T Bien", "Excellent"]
    }
    ]
with open('liste.yaml', 'w') as file:
    yaml.dump(li, file)