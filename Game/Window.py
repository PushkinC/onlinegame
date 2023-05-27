import tkinter as tk
import threading
import json
from CustomModules.CustomTimer import Timer
from Player import Player
from Enemy import Enemy
from requests import Session
from const import *


class Window(tk.Tk):
    def __init__(self, title='main', geometry='500x500'):
        super().__init__()

        self.canvas = tk.Canvas(self, width=1000, height=1000)
        self.tick_from_start = 0
        self.chars = {'w': False, 'a': False, 's': False, 'd': False}
        self.cn = 0

        # self.canvas.create_rectangle(0, 0, 1000, 1000, fill='red')

        self.timer_ping = Timer()
        self.timer_fps = Timer()
        self.session = Session()

        self.label_fps = tk.Label()
        self.label_ping = tk.Label()
        self.player = Player(self.canvas, self.session)
        self.enemies: list[Enemy] = []

        self.__setup(title, geometry)
        self.game()

    def __setup(self, title, geometry):
        self.title(title)
        self.geometry(geometry)

        self.label_fps['text'] = 'fps: 00'
        self.label_ping['text'] = 'ping: 00'

        self.protocol("WM_DELETE_WINDOW", self.out)

        self.label_fps.pack()
        self.label_ping.pack()
        self.canvas.pack()

        self.bind('<KeyPress>', self.keyDown)
        self.bind('<KeyRelease>', self.keyUp)



    def game(self):
        self.cn += 1
        self.tick_from_start += 1

        if  self.tick_from_start % FPS == 0: # Замер ping
            thread = threading.Thread(target=self.__get_ping)
            thread.start()

        if  self.tick_from_start % (FPS // RPS) == 0:  # Отправка и получение координат игроков
            thread = threading.Thread(target=self.__thread_request_for_stat)
            thread.start()


        for key, val in self.chars.items():
            if val:
                self.player.move(key)


        self.player.tick()

        if self.tick_from_start % FPS == 0: # Замер fps
            self.label_fps['text'] = f'fps: {int(self.cn / self.timer_fps.stop())}'
            self.cn = 0
            self.timer_fps.start()




        self.after(1000 // FPS, self.game)



    def out(self):
        data = {'id': self.player.id}
        resp = self.session.post(url=URL + '/del', json=json.dumps(data)).json()
        # self.timer.save('stat/statThread.txt')

        if resp['code'] != 200:
            print('Что то не так в delUser', resp['error'])
        self.quit()
        exit(200)



    def __get_ping(self):
        self.timer_ping.start()
        self.session.get(url=URL + '/ping')
        self.label_ping['text'] = f'ping: {int(round(self.timer_ping.stop(), 4) * 1000)}'

    def __thread_request_for_stat(self):
        data = {
            'id': self.player.id,
            'pos': self.player.pos
        }

        resp = self.session.post(url=URL + '/tick', json=json.dumps(data)).json()

        if resp['code'] != 200:
            print('Что то не так в tick', resp['error'])
            exit(-1)

        resp = self.session.get(url=URL + '/stat').json()
        self.__serv_stat(resp)

    def __serv_stat(self, data: dict):
        if self.player.id in data.keys():
            del data[self.player.id]

        if len(data.keys()) == 0:
            # print('No other players')
            return




        del_data = []
        for i in self.enemies:
            if i.id in data.keys():
                self.canvas.coords(i.object, *data[i.id]['pos'], data[i.id]['pos'][0] + i.size,
                                   data[i.id]['pos'][1] + i.size)
                del_data.append(i.id)
                continue
            del players[i.id]

        for i in del_data:
            del data[i]

        for key, val in data.items():
            self.enemies.append(Enemy(self.canvas, color=val['color'], pos=val['pos'], id=key, size=100))

    def keyDown(self, e):
        key = e.char
        self.chars[key] = True

    def keyUp(self, e):
        key = e.char
        self.chars[key] = False







