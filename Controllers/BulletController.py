import pygame
from const import *
from Entitys.Bullet import SimpleBullet



class BulletController:
    def __init__(self, bullets: pygame.sprite.Group):
        self.bullets = bullets


    def add(self, bullet: SimpleBullet):
        self.bullets.add(bullet)

    def check_out_bullets(self):
        for i in self.bullets:
            if WIDTH < i.rect.centerx or i.rect.centerx < 0 or HEIGHT < i.rect.centery or i.rect.centery < 0:
                print(f'удаляю {i.rect.center}')
                self.bullets.remove(i)

