import pygame
import json
from const import *
from requests import Session
from Sprites.ImageLoader import load_image
from Entitys.Player import Player
from Entitys.Enemy import Enemy
from Timers.CustomTimer import Timer


class API:
    def __init__(self):
        self.session = Session()
        self.timer_ping = Timer()

    def in_server_init(self, player: Player):
        data = {
            'id': player.id,
            'color': player.color
        }
        resp = self.session.post(url=URL + '/add', json=json.dumps(data)).json()
        if resp['code'] != 200:
            print('Что то не так в addUser', resp['error'])
            return

    def thread_request_for_stat(self, player: Player, enemies: pygame.sprite.Group):
        data = {
            'id': player.id,
            'pos': player.rect.center
        }

        resp = self.session.post(url=URL + '/tick', json=json.dumps(data)).json()

        if 'code' in resp.keys():
            print('Что то не так в tick', resp['error'])
            return

        if player.id in resp.keys():
            del resp[player.id]

        if len(resp.keys()) == 0:
            # print('No other players')
            enemies.empty()
            return

        del_data = []
        for i in enemies:
            if i.id in resp.keys():
                i.set_pos(*resp[i.id]['pos'])
                del_data.append(i.id)
            else:
                enemies.remove(i)

        for i in del_data:
            del resp[i]

        for key, val in resp.items():
            enemies.add(Enemy(image=load_image('Sprites/img/Enemy.png'), color=val['color'], pos=val['pos'], id=key))

    def out(self, player: Player):
        data = {'id': player.id}
        resp = self.session.post(url=URL + '/del', json=json.dumps(data)).json()
        # self.timer.save('stat/statThread.txt')

        if resp['code'] != 200:
            print('Что то не так в delUser', resp['error'])
            return -1
        return 200

    def get_ping(self, container: list):
        self.timer_ping.start()
        self.session.get(url=URL + '/ping')
        container[0] = int(round(self.timer_ping.stop(), 4) * 1000)
