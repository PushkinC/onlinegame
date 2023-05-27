import tkinter as tk
import random as rnd
import string
import json
import threading
from requests import Session
from tkinter import Canvas
from const import *



class Player():
    def __init__(self, canvas: Canvas, session: Session):

        self.id = self.__create_id()
        self.color = self.__create_random_color()
        self.pos = [500, 500]
        self.canvas = canvas
        self.session = session
        self.size = 100
        self.object = self.canvas.create_oval(self.pos[0], self.pos[1], self.pos[0] + self.size,
                                              self.pos[1] + self.size, fill=self.color)
        self.__in_server_init()



    def __in_server_init(self):
        data = {
            'id': self.id,
            'color': self.color
        }
        resp = self.session.post(url=URL + '/add', json=json.dumps(data)).json()
        if resp['code'] != 200:
            print('Что то не так в addUser', resp['error'])
            exit(-1)

    def move(self, key):
        match key:
            case 'a':
                self.pos[0] -= SPEED
            case 'd':
                self.pos[0] += SPEED
            case 'w':
                self.pos[1] -= SPEED
            case 's':
                self.pos[1] += SPEED

    def tick(self):

        self.canvas.coords(self.object, self.pos[0], self.pos[1], self.pos[0] + self.size,
                           self.pos[1] + self.size)










    def __create_id(self) -> str:
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
