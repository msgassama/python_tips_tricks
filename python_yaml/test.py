import yaml

with open('sample.yml') as file:
    for d in yaml.load_all(file, yaml.Loader):
        print(d)