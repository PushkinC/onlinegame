import json


with open('Saves/OpenSettings.json', 'rt') as f:
    data = json.load(f)






URL = data['URL']
FPS = data['FPS']
NAME = data['name']
if FPS < 30:
    RPS = FPS
else:
    RPS = 30

WIDTH = HEIGHT = 1000
SPEED = 4 * 60 // FPS
BACKGROUNDCOLOR = 'white'