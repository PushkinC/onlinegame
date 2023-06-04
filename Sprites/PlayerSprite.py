import pygame
from const import NAME
from Sprites.BackGroundSprite import BackGroundSprite


class PlayerSprite(BackGroundSprite):
    def __init__(self, image: pygame.Surface, name, color=-1):
        super().__init__(color)
        self.angle = 0
        self.name = name
        font = pygame.font.SysFont('Verdana', 20)
        font.bold = True
        self.surfname = font.render(name, True, self.color)
        # self.surfname.fill((100,100,100))

        self.player_image = image
        self.player_image.convert_alpha()

        self.player_image = pygame.transform.scale(self.player_image, (self.size, self.size))

        self.clear_background()

        # self.rect = self.image.get_rect()
        # self.rect.x -= (self.backgroundname.get_width() - self.player_image.get_width()) // 2



    def clear_background(self):
        self.clear()
        self.backgroundname = pygame.Surface(
            (max(self.background.get_width(), self.surfname.get_width()), self.background.get_height() + self.surfname.get_height() + 5))
        self.backgroundname.set_colorkey('black')
        self.backgroundname.blit(self.background, ((self.backgroundname.get_width() - self.background.get_width()) // 2, 0))
        self.backgroundname.blit(self.surfname, ((self.backgroundname.get_width() - self.surfname.get_width()) // 2, self.background.get_height() + 5))
        self.image = self.backgroundname.copy()

    def rotate(self, global_angle):
        self.angle = global_angle

        old_rect = self.rect
        old_player_rect = self.player_image.get_rect()

        rotated_image = pygame.transform.rotate(self.player_image, global_angle)
        rotated_rect = rotated_image.get_rect(center=old_player_rect.center)
        rotated_rect.x += (self.backgroundname.get_width() - self.player_image.get_width()) // 2

        self.clear_background()
        self.image.blit(rotated_image, rotated_rect)
        # self.image.fill((100,100,100))
        self.rect = self.image.get_rect()
        self.rect.center = old_rect.center


class EnemySprite(BackGroundSprite):
    def __init__(self, image: pygame.Surface, name, color=-1):
        super().__init__(color)

        self.angle = 0
        self.name = name
        font = pygame.font.SysFont('Verdana', 20)
        font.bold = True
        self.surfname = font.render(name, True, self.color)

        self.player_image = image
        self.player_image.convert_alpha()

        self.player_image = pygame.transform.scale(self.player_image, (self.size, self.size))

        self.clear()
        self.backgroundname = pygame.Surface(
            (max(self.background.get_width(), self.surfname.get_width()),
             self.background.get_height() + self.surfname.get_height() + 5))
        self.backgroundname.set_colorkey('black')
        self.backgroundname.blit(self.background,
                                 ((self.backgroundname.get_width() - self.background.get_width()) // 2, 0))
        self.backgroundname.blit(self.surfname,
                                 ((self.backgroundname.get_width() - self.surfname.get_width()) // 2, self.rect.h + 5))
        self.image = self.backgroundname.copy()
        self.rect = self.image.get_rect()



