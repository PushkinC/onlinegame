import pygame
from Fonts.MultilineText import render_multiline_text
from Sprites.ImageLoader import load_image
from Entitys.Player import Player


class StatusMonitor:
    def __init__(self):
        self.padding = {'top': 5, 'bottom': 5, 'left': 5, 'right': 5}
        self.font = pygame.font.SysFont('Verdana', 20)
        self.reload_image = load_image('Sprites/img/Reload.png')
        self.reload_image.convert_alpha()
        self.reloading = False
        self.visibility = 1

    def draw(self, player: Player) -> pygame.Surface:
        if self.visibility:
            text = [f'HP: {player.hp}',
                    f'Bullet: {player.weapon.magazine.count}']
            stat = render_multiline_text(self.font, text, True, (0, 255, 0), 5)
            stat_rect = stat.get_rect()
            if self.reloading:
                reload = pygame.transform.scale(self.reload_image, (stat_rect.h, stat_rect.h))
            else:
                reload = pygame.Surface((1, 1))
            reload_rect = reload.get_rect()
            background = pygame.Surface((stat_rect.w + self.padding['left'] * 2 + self.padding['right'] + reload_rect.w,
                                         stat_rect.h + self.padding['top'] + self.padding['bottom']),
                                        flags=pygame.SRCALPHA)
            background.fill(color=(150, 0, 0, 150))
            background.blit(reload, (self.padding['left'], self.padding['top']))
            background.blit(stat, (self.padding['left'] * 2 + reload_rect.w, self.padding['top']))
            return background
        return pygame.Surface((1, 1))
