import pygame as pg
import  random

from pygame import Rect
from pygame.locals import (K_UP, K_DOWN,
                           K_LEFT,
                           K_RIGHT,
                           K_ESCAPE,
                           KEYDOWN,
                           K_s,
                           K_w,

                           QUIT,
                           )


screen_width=1550
screen_hight=800

class Player(pg.sprite.Sprite):
    player_hight=150
    player_width=10


    def __init__(self):
        super(Player, self).__init__()
        self.rect = pg.Rect(screen_width - 30, screen_hight / 2 - 70, self.player_width, self.player_hight)
        self.rect.x=self.rect.x
        self.rect.y=self.rect.y
        self.score=0


    def movement_handeling(self):
        if self.rect.y >= screen_hight-self.player_hight:
            self.rect.y= screen_hight-self.player_hight
        if self.rect.y <= 0:
            self.rect.y = 0

    def move(self, pressed_keys, up, down):
        if pressed_keys[up]:
            self.rect.y -=4
            self.movement_handeling()
        if pressed_keys[down]:
            self.rect.y+= 4
            self.movement_handeling()









class Ball(pg.sprite.Sprite):

    def __init__(self):
        super(Ball,self).__init__()
        self.rect =pg.Rect(screen_width/2, screen_hight/2 -70, 30, 30)













