import json

with open('Saves/SettingsData.json', 'rt') as f:
    data = json.load(f)

with open('Saves/PlayerData.json', 'rt') as f:
    NAME = json.load(f)['name']

URL = data['URL']
FPS = data['FPS']
if FPS < 30:
    RPS = FPS
else:
    RPS = 30

WIDTH = data['width']
HEIGHT = data['height']
SPEED = 4 * 60 // FPS
BACKGROUNDCOLOR = 'white'
