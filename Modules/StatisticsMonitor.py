import pygame
from Fonts.MultilineText import render_multiline_text
from Entitys.Player import Player
from Controllers.BulletController import BulletController
from const import *


class StatisticsMonitor:
    def __init__(self):
        self.padding = {'top': 5, 'bottom': 5, 'left': 5, 'right': 5}
        self.font = pygame.font.SysFont('Verdana', 12)
        self.visibility = 0

    def draw(self, fps, ping, player: Player, bc: BulletController) -> pygame.Surface:
        if self.visibility:
            text = [f'FPS: {fps}, PING: {ping}, RPS: {RPS}',
                    f'URL: {URL}',
                    f'Angle: {player.angle}',
                    f'Position: X: {player.rect.centerx}, Y: {player.rect.centery}',
                    f'Count_bullets {len(bc.my_bullets) + len(bc.other_bullets)}',
                    f'Your_ID: {player.id}']
            stat = render_multiline_text(self.font, text, True, (0, 255, 0), 5)
            stat_rect = stat.get_rect()
            background = pygame.Surface((stat_rect.w + self.padding['top'] + self.padding['bottom'],
                                         stat_rect.h + self.padding['left'] + self.padding['right']),
                                        flags=pygame.SRCALPHA)
            background.fill(color=(150, 150, 150, 150))
            background.blit(stat, (self.padding['top'], self.padding['left']))
            return background
        return pygame.Surface((1, 1))
