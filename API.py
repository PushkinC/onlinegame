import pygame
import json
from const import *
from requests import Session
from Sprites.ImageLoader import load_image
from Entitys.Player import Player
from Entitys.Enemy import Enemy
from Entitys.Bullet import EnemyBullet
from Timers.CustomTimer import Timer
from Controllers.BulletController import BulletController


class API:
    def __init__(self):
        self.session = Session()
        self.timer_ping = Timer()

    def in_server_init(self, player: Player):

        data = {
            'id': player.id,
            'name': player.name,
            'color': player.color,
            'size': player.size,
            'hp': player.hp,
            'pos': player.rect.center,
            'deleted_bullets': [],
            'bullets': {}
        }
        resp = self.session.post(url=URL + '/add', json=json.dumps(data)).json()
        if resp['code'] != 200:
            print('Что то не так в addUser', resp['error'])
            return

    def thread_request_for_stat(self, player: Player, enemies: pygame.sprite.Group, bullet_controller: BulletController):
        data = {
            'id': player.id,
            'pos': player.rect.center,
            'bullets': {i.id: {'color': i.color, 'size': i.size, 'damage': i.damage, 'pos': i.rect.center} for i in bullet_controller.my_bullets}
        }

        resp = self.session.post(url=URL + '/tick', json=json.dumps(data)).json()

        bullet_controller.other_bullets.empty()

        if 'code' in resp.keys():
            print('Что то не так в tick', resp['error'])
            return

        player.hp = resp[player.id]['hp']  # Устанавливаю hp как на сервере

        bullet_controller.remove_by_id(resp[player.id]['deleted_bullets'], bullet_controller.my_bullets)

        if player.id in resp.keys():  # Удаляю из ответа от сервера player
            del resp[player.id]

        if len(resp.keys()) == 0:
            # print('No other players')
            enemies.empty()
            return

        for i in resp.keys():  # Добавляю вражеские пули
            a = resp[i]['bullets']
            for j in resp[i]['bullets'].keys():
                bullet_controller.other_bullets.add(EnemyBullet(j, a[j]['pos'], a[j]['damage'], a[j]['size'], a[j]['color']))


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
            enemies.add(Enemy(image=load_image('Sprites/img/Enemy.png'), color=val['color'], pos=val['pos'], id=key, name=val['name']))

    def out(self, player: Player):
        data = {'id': player.id}
        resp = self.session.post(url=URL + '/del', json=json.dumps(data)).json()

        if resp['code'] != 200:
            print('Что то не так в delUser', resp['error'])
            return -1
        return 200

    def get_ping(self, container: list):
        self.timer_ping.start()
        self.session.get(url=URL + '/ping')
        container[0] = int(round(self.timer_ping.stop(), 4) * 1000)

    def heal(self, player: Player, heal: int):
        data = {
            'id': player.id,
            'heal': heal
        }
        self.session.post(URL + '/heal', json=json.dumps(data))
