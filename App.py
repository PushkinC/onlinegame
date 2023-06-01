import pygame
import threading
from const import *
from API import API
from Entitys.Player import Player
from Sprites.ImageLoader import load_image


class App:
    def __init__(self, title):
        pygame.init()

        self.surface = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption(title)
        self.clock = pygame.time.Clock()
        self.running = True

        self.plyer_group = pygame.sprite.Group()
        self.player = Player(load_image('Sprites/img/Player.png'))
        self.plyer_group.add(self.player)

        self.enemies = pygame.sprite.Group()

        self.tick_from_start = 0

        self.api = API()
        self.api.in_server_init(self.player)


    def tick(self):
        self.tick_from_start += 1
        self.surface.fill(BACKGROUNDCOLOR)
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

        self.plyer_group.draw(self.surface)
        self.plyer_group.update()

        self.enemies.draw(self.surface)
        self.enemies.update()

        pygame.display.flip()