from typing import Any

import pygame
from Sprites.PlayerSprite import EnemySprite
from const import *
import random as rnd
import string



class Enemy(EnemySprite):
    def __init__(self, image, color, id, pos, name):
        super().__init__(image=image, color=color, name=name)
        self.id = id
        self.rect.center = pos

    def set_pos(self, x, y):
        self.rect.center = (x, y)




