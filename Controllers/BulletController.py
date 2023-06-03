import pygame
from const import *
from Entitys.Bullet import SimpleBullet



class BulletController:
    def __init__(self, bullets: pygame.sprite.Group, other_bullets: pygame.sprite.Group):
        self.my_bullets = bullets
        self.other_bullets = other_bullets


    def add(self, bullet: SimpleBullet):
        self.my_bullets.add(bullet)

    @staticmethod
    def remove_by_id(bullets: list[str], group: pygame.sprite.Group):
        for i in group:
            if i.id in bullets:
                group.remove(i)


    def check_out_bullets(self):
        for i in self.my_bullets:
            if WIDTH < i.rect.centerx or i.rect.centerx < 0 or HEIGHT < i.rect.centery or i.rect.centery < 0:
                self.my_bullets.remove(i)

