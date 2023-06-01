import pygame
from Sprites.BackGroundSprite import BackGroundSprite


class SimpleSprite(BackGroundSprite):
    def __init__(self, image: pygame.Surface, color=-1):
        super().__init__(color)

        self.image = image
        self.image.convert_alpha()

        self.image = pygame.transform.scale(self.image, (self.size, self.size))

        self.background.blit(self.image, (0, 0))
        self.image = self.background
        self.rect = self.image.get_rect()
