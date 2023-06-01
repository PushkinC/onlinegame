from typing import Any

import pygame
from Sprites.SimpleSprite import SimpleSprite
from const import *
import random as rnd
import string



class Enemy(SimpleSprite):
    def __init__(self, image, color, id, pos):
        super().__init__(image, color)

        self.id = id
        self.rect.center = [100, 900]

    def set_pos(self, x, y):
        self.rect.center = (x, y)



    def update(self, *args: Any, **kwargs: Any) -> None:
        pass




