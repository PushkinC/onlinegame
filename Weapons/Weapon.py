import json
import threading
import time
from Controllers.WeaponAudioController import WeaponAudioController

from Entitys.Bullet import SimpleBullet, create_bullet
from Controllers.BulletController import BulletController
from const import *


SINGLFIRE = 0
AUTOFIRE = 1
TRIPLEFIRE = 2
SINGLEAUTO = 3
SINGLETRIPLE = 4


class Magazine:
    def __init__(self, max: int, sm):
        self.max = max
        self.count = max
        self.statusMonitor = sm

    def fire(self):
        if self.count:
            self.count -= 1
            return True
        else:
            return False

    def reload(self, reload_time):
        self.statusMonitor.reloading = True
        time.sleep(reload_time)
        self.count = self.max
        self.statusMonitor.reloading = False




class SimpleWeapon:
    def __init__(self, bullet: SimpleBullet, reload_time: int, magazine_bullet: int, rate_of_fire: int, fire_mode: int, sm, name, ac: WeaponAudioController):
        self.magazine = Magazine(magazine_bullet, sm)
        self.name = name
        self.audioController = ac
        self.rate_of_fire = rate_of_fire
        self.fire_mode = fire_mode
        self.cur_fire_mode = fire_mode
        if fire_mode > 2:
            self.cur_fire_mode = SINGLFIRE
        self.__first_shot = True
        self.__one_mouse_three_click = True
        self.__last_shot = 0
        self.__triple = 4
        self.tick = 0
        self.bullet = bullet
        self.reload_time = reload_time
        self.reloading = False

    def reload(self):
        if self.reloading:
            self.reloading = False
            self.audioController.clipempty.play()
            self.audioController.reload.play()
            thread = threading.Thread(target=lambda: self.magazine.reload(self.reload_time))
            thread.start()



    def update(self, mouse: dict, stat):
        self.tick += 1
        if mouse[1]:
            if self.cur_fire_mode == SINGLFIRE:
                if self.__first_shot:
                    print('shot', self.__first_shot)
                    self.__first_shot = False
                    if self.magazine.fire():
                        self.audioController.fire.play()
                        self.bullet(stat)
                        self.reloading = True
                    else:
                        self.reload()


            elif self.cur_fire_mode == AUTOFIRE:
                if self.tick - self.__last_shot > FPS / self.rate_of_fire:
                    if self.magazine.fire():
                        self.__last_shot = self.tick
                        self.audioController.fire.play()
                        self.bullet(stat)
                        self.reloading = True
                    else:
                        self.reload()

            elif self.cur_fire_mode == TRIPLEFIRE:
                if self.__first_shot:
                    if self.tick - self.__last_shot > FPS / self.rate_of_fire * 3:
                        self.__first_shot = False
                        self.__triple = 0

        else:
            self.__first_shot = True

        if self.__triple < 3:
            if self.tick - self.__last_shot > FPS / self.rate_of_fire:
                if self.magazine.fire():
                    self.__last_shot = self.tick
                    self.bullet(stat)
                    self.audioController.fire.play()
                    self.__triple += 1
                    self.reloading = True
                else:
                    self.__triple = 4
                    self.reload()

        if mouse[3]:
            if self.__one_mouse_three_click:
                self.__one_mouse_three_click = False
                if self.fire_mode == SINGLEAUTO:
                    if self.cur_fire_mode == SINGLFIRE:
                        self.cur_fire_mode = AUTOFIRE
                    else:
                        self.cur_fire_mode = SINGLFIRE
                elif self.fire_mode == SINGLETRIPLE:
                    if self.cur_fire_mode == SINGLFIRE:
                        self.cur_fire_mode = TRIPLEFIRE
                    else:
                        self.cur_fire_mode = SINGLFIRE
        else:
            self.__one_mouse_three_click = True

        if mouse['r']:
            self.reload()



def load_weapon(name: str, bc: BulletController, sm) -> SimpleWeapon:
    with open('Weapons/Weapons.json', 'rt') as f:
        weapons = json.load(f)
    weapon = weapons[name]
    bullet = create_bullet(weapon['bullet'], bc)
    audioController = WeaponAudioController(name)

    return SimpleWeapon(bullet=bullet, reload_time=weapon['reload_time'], magazine_bullet=weapon['magazine_bullet'], rate_of_fire=weapon['rate_of_fire'], fire_mode=weapon['fire_mode'], sm=sm, name=name, ac=audioController)




