import pygame


class WeaponAudioController:
    def __init__(self, weapon):
        self.fire = pygame.mixer.Sound(f'Audio/{weapon}/{weapon}-fire.mp3')
        self.reload = pygame.mixer.Sound(f'Audio/{weapon}/{weapon}-reload.mp3')
        self.clipempty = pygame.mixer.Sound(f'Audio/{weapon}/{weapon}-clipempty.mp3')
        self.fire.set_volume(0.01)
        self.reload.set_volume(0.1)
        self.clipempty.set_volume(0.1)
