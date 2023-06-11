import pygame
from const import *
from requests import Session

pygame.init()
clock = pygame.time.Clock()
running = True
session = Session()


def get_stat_from_server():
    return session.get(url=URL + '/stat').json()


def post_data_to_server(data):
    session.post(url=URL + '/collision', json=json.dumps(data)).json()


def check_collision(data: dict):
    hits = {i: {'damage': 0, 'bullets': []} for i in data.keys()}  # {player: {damage, bullets: []}} (Урон player и какие пули у player надо удалить)
    # Проверка столкнулся ли i с пулями j
    distance = lambda pos1, pos2: ((pos1[0] - pos2[0]) ** 2 + (pos1[1] - pos2[1]) ** 2) ** 0.5
    for i in data.keys():
        for j in data.keys():
            if i == j:
                continue

            pos_i = data[i]['pos']
            size_i = data[i]['size']

            bullets = data[j]['bullets']

            for b in bullets.keys():
                if distance(pos_i, bullets[b]['pos']) <= (bullets[b]['size'] + size_i) // 1.5:
                    print('damage')
                    hits[i]['damage'] += bullets[b]['damage']
                    hits[j]['bullets'].append(b)




    return hits


def tick():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            global running
            running = False

    resp = get_stat_from_server()
    data = check_collision(resp)
    post_data_to_server(data)

    clock.tick(RPS)

print('collision runnig')

while running:
    tick()
