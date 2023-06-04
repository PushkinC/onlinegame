import pygame
import random as rnd


class BackGroundSprite(pygame.sprite.Sprite):
    def __init__(self, color, size=100):
        super().__init__()

        self.color = color
        if color == -1:
            self.color = self.__create_random_color()

        self.size = size
        self.background = pygame.Surface((self.size, self.size))
        self.background.set_colorkey('black')
        pygame.draw.circle(self.background, self.color, (self.size // 2, self.size // 2), self.size // 2)
        self.image = pygame.Surface((self.size, self.size))
        self.image.set_colorkey('black')
        self.rect = self.image.get_rect()

    def clear(self):
        self.image = pygame.Surface((self.size, self.size))
        self.image.set_colorkey('black')


    def __create_random_color(self) -> tuple:
        r = rnd.randrange(60, 200)
        g = rnd.randrange(60, 200)
        b = rnd.randrange(60, 200)
        return r, g, b


