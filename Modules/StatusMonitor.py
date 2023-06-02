import pygame
from Fonts.MultilineText import render_multiline_text
from Entitys.Player import Player


class StatusMonitor:
    def __init__(self):
        self.padding = {'top': 5, 'bottom': 5, 'left': 5, 'right': 5}
        self.font = pygame.font.SysFont('Verdana', 20)
        self.visibility = 1

    def draw(self, player: Player) -> pygame.Surface:
        if self.visibility:
            text = [f'HP: {player.hp}',
                    f'Bullet: {player.weapon.magazine.count}']
            stat = render_multiline_text(self.font, text, True, (0, 255, 0), 5)
            stat_rect = stat.get_rect()
            background = pygame.Surface((stat_rect.w + self.padding['top'] + self.padding['bottom'],
                                         stat_rect.h + self.padding['left'] + self.padding['right']),
                                        flags=pygame.SRCALPHA)
            background.fill(color=(150, 0, 0, 150))
            background.blit(stat, (self.padding['top'], self.padding['left']))
            return background
        return pygame.Surface((1, 1))
