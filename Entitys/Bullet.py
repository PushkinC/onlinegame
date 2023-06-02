import pygame

from Sprites.BackGroundSprite import BackGroundSprite
import math


class SimpleBullet(BackGroundSprite):
    def __init__(self, bc, velocity: float, stat: tuple, color='yellow'):
        super(SimpleBullet, self).__init__(color=color, size=10)

        self.image.blit(self.background, (0, 0))
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.center = stat[0]
        bc.add(self)
        self.velocity = velocity

        self.vector = self.calculate_vector(stat[1])
        radius = self.calculate_radius(stat[1], stat[2])
        self.rect.centerx += radius[0]
        self.rect.centery += radius[1]

    def calculate_vector(self, angle):
        x = -math.sin(math.radians(angle)) * self.velocity
        y = -math.cos(math.radians(angle)) * self.velocity
        return x, y

    def calculate_radius(self, angle, size):
        x = -math.sin(math.radians(angle)) * (size // 2 + 10)
        y = -math.cos(math.radians(angle)) * (size // 2 + 10)
        return x, y

    def update(self):
        self.rect.x += self.vector[0]
        self.rect.y += self.vector[1]



class EnemyBullet(BackGroundSprite):
    def __init__(self, pos, color='yellow'):
        super(EnemyBullet, self).__init__(color=color, size=10)

        self.image.blit(self.background, (0, 0))
        self.rect = self.image.get_rect()
        self.rect.center = pos


class MachineGunBullet(SimpleBullet):
    color = 'orange'

    def __init__(self, bc, stat):
        super(MachineGunBullet, self).__init__(bc=bc, velocity=7, stat=stat, color=self.color)
