import pygame
from Sprites.BackGroundSprite import BackGroundSprite


class SimpleSprite(BackGroundSprite):
    def __init__(self, image: pygame.Surface, color=-1):
        super().__init__(color)
        self.angle = 0

        self.player_image = image
        self.player_image.convert_alpha()

        self.player_image = pygame.transform.scale(self.player_image, (self.size, self.size))

        self.image.blit(self.background, (0, 0))
        self.image.blit(self.player_image, (0, 0))

        self.rect = self.image.get_rect()

    def clear_background(self):
        self.clear()
        self.image.blit(self.background, (0, 0))


    def rotate(self, global_angle):
        self.angle = global_angle

        old_rect = self.rect
        old_player_rect = self.player_image.get_rect()

        rotated_image = pygame.transform.rotate(self.player_image, global_angle)
        rotated_rect = rotated_image.get_rect(center=old_player_rect.center)

        self.clear_background()
        self.image.blit(rotated_image, rotated_rect)
        self.rect = self.image.get_rect()
        self.rect.center = old_rect.center

