'''
title: box class
author: Chelsea Chen
date-created: 2021-03-08
'''

import pygame
from loader import Color
from mySprite import MySprite


class Box(MySprite): # inherits the MySprite class
    def __init__(self, WIDTH = 1, HEIGHT =1, X =1, Y=0, COLOR = Color.WHITE):
        super().__init__()
        self.WIDTH = WIDTH
        self.HEIGHT = HEIGHT
        self.updateDimension()
        self.X = X
        self.Y = Y
        self.updatePOS()
        self.POS = (self.X, self.Y)
        self.COLOR = COLOR
        self.SCREEN = pygame.Surface(self.DIMENSION, pygame.SRCALPHA, 32)
        self.SCREEN.fill(self.COLOR)

# --- MODIFIER METHODS --- #
    def setColor(self, NEWCOLOR): # use of setter method to encapsulate
        self.COLOR = NEWCOLOR
        self.SCREEN.fill(self.COLOR)



