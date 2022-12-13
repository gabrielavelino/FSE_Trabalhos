import json

class ConfigJson:
    def __init__(self,fileName):
        with open(fileName) as f:
            self.json = json.load(f)


sala_1 = ConfigJson('configuracao_sala1.json')

print(sala_1.json['outputs'])

