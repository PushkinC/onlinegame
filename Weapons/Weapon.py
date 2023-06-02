import threading
import time
from Entitys.Bullet import MachineGunBullet, SimpleBullet
from Controllers.BulletController import BulletController
from const import *


SINGLFIRE = 0
AUTOFIRE = 1
TRIPLEFIRE = 2


class Magazine:
    def __init__(self, max: int):
        self.max = max
        self.count = max

    def fire(self):
        if self.count:
            self.count -= 1
            return self.count
        else:
            return self.count

    def reload(self, reload_time):
        time.sleep(reload_time)
        self.count = self.max




class SimpleWeapon:
    def __init__(self, bc:BulletController, bullet: SimpleBullet, reload_time=2, magazine_bullet=30, rate_of_fire=10, fire_mode=SINGLFIRE):
        self.magazine = Magazine(magazine_bullet)
        self.rate_of_fire = rate_of_fire
        self.fire_mode = fire_mode
        self.__first_shot = True
        self.tick = 0
        self.bullet = bullet
        self.bullet_controller = bc
        self.reload_time = reload_time
        self.reloading = False

    def reload(self):
        if self.reloading:
            self.reloading = False
            thread = threading.Thread(target=lambda: self.magazine.reload(self.reload_time))
            thread.start()



    def update(self, mouse: dict, stat):
        self.tick += 1
        if mouse[1]:
            if self.fire_mode == SINGLFIRE:
                if self.__first_shot:
                    if self.magazine.fire():
                        self.__first_shot = False
                        self.bullet(self.bullet_controller, stat)
                        self.reloading = True
                    else:
                        self.reload()


            elif self.fire_mode == AUTOFIRE:
                if self.tick % (FPS // self.rate_of_fire) == 0:
                    if self.magazine.fire():
                        self.bullet(self.bullet_controller, stat)
                        self.reloading = True
                    else:
                        self.reload()

        if mouse['r']:
            self.reload()

        else:
            self.__first_shot = True



class Automachine(SimpleWeapon):
    def __init__(self, magazine_bullet, rate_of_fire, bullet, bc):
        super(Automachine, self).__init__(bc=bc, bullet=bullet, magazine_bullet=magazine_bullet, rate_of_fire=rate_of_fire, fire_mode=AUTOFIRE)





class AK_47(Automachine):
    def __init__(self, bc):
        super(AK_47, self).__init__(magazine_bullet=30, rate_of_fire=10, bullet=MachineGunBullet, bc=bc)


