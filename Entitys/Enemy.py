from typing import Any

import pygame
from Sprites.EntitySprite import EnemySprite
from const import *
import random as rnd
import string



class Enemy(EnemySprite):
    def __init__(self, image, color, id, pos, name, hp):
        super().__init__(image=image, color=color, name=name)
        self.id = id
        self.hp = hp
        self.rect.center = pos

    def set_pos(self, x, y):
        self.rect.center = (x, y)

    def update(self, *args: Any, **kwargs: Any) -> None:
        if self.hp == 0:
            self.cur_image = self.die_image.copy()
        else:
            self.cur_image = self.player_image.copy()
        self.clear_background()




