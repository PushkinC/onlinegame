from typing import Any
import math
import pygame
from Sprites.SimpleSprite import SimpleSprite
from const import *
import random as rnd
import string



class Player(SimpleSprite):
    def __init__(self, image):
        super().__init__(image)

        self.id = self.__create_id()
        self.rect.center = [500, 500]
        self.chars = {}


    def __create_id(self) -> str:
        letters = string.ascii_lowercase
        rand_string = ''.join(rnd.choice(letters) for i in range(20))
        return rand_string

    def update(self, *args: Any, **kwargs: Any) -> None:
        for key, val in self.chars.items():
            if val: self.move(key)

        x, y = pygame.mouse.get_pos()
        angle = int(math.degrees(math.atan2(-self.rect.centerx + x, -self.rect.centery + y)) + 180)
        self.rotate(angle)



    def move(self, key):
        match key:
            case 'a':
                self.rect.x -= SPEED
            case 'd':
                self.rect.x += SPEED
            case 'w':
                self.rect.y -= SPEED
            case 's':
                self.rect.y += SPEED



