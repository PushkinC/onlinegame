import pygame


class StatisticsMonitor:
    def __init__(self, id: str):
        self.id = id
        self.padding = {'top': 5, 'bottom': 5, 'left': 5, 'right': 5}
        self.font = pygame.font.SysFont('Verdana', 12)

    def draw(self, fps, ping) -> pygame.Surface:
        stat = self.font.render(f'FPS: {fps}, PING: {ping}, Your_ID: {self.id}', True, (0, 255, 0))
        stat_rect = stat.get_rect()
        background = pygame.Surface((stat_rect.w + self.padding['top'] + self.padding['bottom'],
                                     stat_rect.h + self.padding['left'] + self.padding['right']), flags=pygame.SRCALPHA)
        background.fill(color=(150, 150, 150, 150))
        background.blit(stat, (self.padding['top'], self.padding['left']))
        return background
