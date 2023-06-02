import pygame
from Fonts.MultilineText import render_multiline_text


class StatisticsMonitor:
    def __init__(self, id: str):
        self.id = id
        self.padding = {'top': 5, 'bottom': 5, 'left': 5, 'right': 5}
        self.font = pygame.font.SysFont('Verdana', 12)
        self.visibility = 0

    def draw(self, fps, ping, angle) -> pygame.Surface:
        if self.visibility:
            text = [f'FPS: {fps}, PING: {ping}',
                    f'Angle: {angle}, Your_ID: {self.id}']
            stat = render_multiline_text(self.font, text, True, (0, 255, 0), 5)
            stat_rect = stat.get_rect()
            background = pygame.Surface((stat_rect.w + self.padding['top'] + self.padding['bottom'],
                                         stat_rect.h + self.padding['left'] + self.padding['right']),
                                        flags=pygame.SRCALPHA)
            background.fill(color=(150, 150, 150, 150))
            background.blit(stat, (self.padding['top'], self.padding['left']))
            return background
        return pygame.Surface((1, 1))
