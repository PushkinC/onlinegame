import tkinter as tk
import random as rnd
import string
import json
import threading
from requests import post, get
from tkinter import Canvas

URL = 'http://127.0.0.1:5050'
FPS = 60

app = tk.Tk()
app.geometry('1000x1000')

players = {}


class Player():
    def __init__(self, canvas:Canvas):
        self.name = self.__create_name()
        self.color = self.__create_random_color()
        self.pos = [500, 500]
        self.canvas = canvas
        self.size = [100, 100]
        self.object = self.canvas.create_oval(self.pos[0], self.pos[1], self.pos[0] + self.size[0], self.pos[1] + self.size[1], fill=self.color)
        self.__in_server_init()
        self.t = 0

    def __in_server_init(self):
        data = {
            'name': self.name,
            'color': self.color
        }
        resp = post(URL + '/add', json=json.dumps(data)).json()
        if resp['code'] != 200:
            print('Что то не так в addUser', resp['error'])
            exit(-1)

    def move(self, key, e):
        match key:
            case 'a':
                self.pos[0] -= 5
            case 'd':
                self.pos[0] += 5
            case 'w':
                self.pos[1] -= 5
            case 's':
                self.pos[1] += 5

    def tick(self):
        self.t += 1
        self.canvas.coords(self.object, self.pos[0], self.pos[1], self.pos[0] + self.size[0], self.pos[1] + self.size[1])

        if self.t % (FPS // 3) == 0:
            thread = threading.Thread(target=self.__thread_request_for_stat())
            thread.start()


    def out(self):
        data = {'name': self.name}
        resp = post(URL + '/del', json=json.dumps(data)).json()

        if resp['code'] != 200:
            print('Что то не так в delUser', resp['error'])
            exit(-1)


    def __thread_request_for_stat(self):
        data = {
            'name': self.name,
            'pos': self.pos
        }
        resp = post(URL + '/tick', json=json.dumps(data)).json()

        if resp['code'] != 200:
            print('Что то не так в tick', resp['error'])
            exit(-1)

        resp = get(URL + '/stat').json()
        self.__serv_stat(resp)

    def __serv_stat(self, data: dict):
        if self.name in data.keys():
            del data[self.name]

        if len(data.keys()) == 0:
            print('No other players')
            return

        for key, val in data.items():
            if key not in players.keys():
                players[key] = self.canvas.create_oval(*val['pos'], val['pos'][0] + self.size[0], val['pos'][1] + self.size[1], fill=val['color'])
            self.canvas.coords(players[key], *val['pos'], val['pos'][0] + self.size[0], val['pos'][1] + self.size[1])
    def __create_name(self):
        letters = string.ascii_lowercase
        rand_string = ''.join(rnd.choice(letters) for i in range(20))
        return rand_string
    def __create_random_color(self) -> str:
        r = hex(rnd.randrange(0, 200))[2:]
        g = hex(rnd.randrange(0, 200))[2:]
        b = hex(rnd.randrange(0, 200))[2:]
        if len(r) < 2:
            r = '0' + r
        if len(g) < 2:
            g = '0' + g
        if len(b) < 2:
            b = '0' + b

        return f'#{r}{g}{b}'


class Canvas(tk.Canvas):
    def __init__(self, app, width=1000, height=1000):
        super().__init__(app, width=width, height=height)


canvas = Canvas(app)
player = Player(canvas)

app.protocol("WM_DELETE_WINDOW", player.out)


canvas.pack()


def game():

    player.tick()
    app.after(1000 // FPS, game)

app.bind('a', lambda e: player.move('a', e))
app.bind('w', lambda e: player.move('w', e))
app.bind('s', lambda e: player.move('s', e))
app.bind('d', lambda e: player.move('d', e))



game()
app.mainloop()