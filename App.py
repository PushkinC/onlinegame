import pygame
import threading
from const import *
from API import API
from Entitys.Player import Player
from Sprites.ImageLoader import load_image
from Modules.StatisticsMonitor import StatisticsMonitor


class App:
    def __init__(self, title):
        pygame.init()
        pygame.font.init()

        self.surface = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption(title)
        self.clock = pygame.time.Clock()
        self.running = True

        self.plyer_group = pygame.sprite.Group()
        self.player = Player(load_image('Sprites/img/Player.png'))
        self.plyer_group.add(self.player)

        self.enemies = pygame.sprite.Group()

        self.tick_from_start = 0
        self.ping = [-1]
        self.statistics = pygame.surface.Surface((1, 1))

        self.background = load_image('Sprites/img/background.jpg')
        self.background = pygame.transform.scale(self.background, self.surface.get_rect().size)

        self.api = API()
        self.api.in_server_init(self.player)

        self.statisticsMonitor = StatisticsMonitor(self.player.id)



    def tick(self):
        self.tick_from_start += 1
        self.surface.fill(BACKGROUNDCOLOR)
        self.surface.blit(self.background, (0, 0))
        self.surface.blit(self.statistics, (0, 0))
        self.clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                if self.api.out(self.player) == 200:
                    self.running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    self.player.chars['a'] = True
                elif event.key == pygame.K_d:
                    self.player.chars['d'] = True
                elif event.key == pygame.K_s:
                    self.player.chars['s'] = True
                elif event.key == pygame.K_w:
                    self.player.chars['w'] = True
                elif event.key == pygame.K_F1: # Отображение statisticsMonitor
                    self.statisticsMonitor.visibility = 1 - self.statisticsMonitor.visibility
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_a:
                    self.player.chars['a'] = False
                elif event.key == pygame.K_d:
                    self.player.chars['d'] = False
                elif event.key == pygame.K_s:
                    self.player.chars['s'] = False
                elif event.key == pygame.K_w:
                    self.player.chars['w'] = False # #

        if self.tick_from_start % (FPS // RPS) == 0:  # Отправка и получение координат игроков
            thread = threading.Thread(target=lambda: self.api.thread_request_for_stat(self.player, self.enemies))
            thread.start()

        if self.tick_from_start % FPS == 0:
            thread = threading.Thread(target=lambda: self.api.get_ping(self.ping))
            thread.start()
            self.statistics = self.statisticsMonitor.draw(int(self.clock.get_fps()), self.ping[0])

        self.plyer_group.draw(self.surface)
        self.plyer_group.update()

        self.enemies.draw(self.surface)
        self.enemies.update()

        pygame.display.flip()