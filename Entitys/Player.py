from typing import Any
import math
import pygame
from Sprites.SimpleSprite import SimpleSprite
from const import *
import random as rnd
import string
from Weapons.SimpleWeapon import AK_47



class Player(SimpleSprite):
    def __init__(self, image, bc):
        super().__init__(image)

        self.id = self.__create_id()
        self.rect.center = [500, 500]
        self.chars = {}
        self.mouse = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 'r': 0}
        self.weapon = AK_47(bc)
        self.hp = 100


    def __create_id(self) -> str:
        letters = string.ascii_lowercase
        rand_string = ''.join(rnd.choice(letters) for i in range(20))
        return rand_string

    def update(self, *args: Any, **kwargs: Any) -> None:
        if self.hp <= 0:
            return

        for key, val in self.chars.items():  # Двигаю персонажа
            if val: self.move(key)

        x, y = pygame.mouse.get_pos()  # Вычисляю угол поворота и поворачиваю
        angle = int(math.degrees(math.atan2(-self.rect.centerx + x, -self.rect.centery + y)) + 180)
        self.rotate(angle)

        self.weapon.update(self.mouse, (self.rect.center, angle, self.size))





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




