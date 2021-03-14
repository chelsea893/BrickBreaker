'''
title: text object
author: Chelsea Chen
date-created: 2021-03-08
'''

from loader import Color
import pygame
from mySprite import MySprite

class Text(MySprite): # inherits the MySprite class
    def __init__(self, TEXT = "Hello World", COLOR = Color.WHITE):
        super().__init__()
        self.TEXT = TEXT
        self.COLOR = COLOR
        self.FONT = pygame.font.SysFont("Arial", 30)
        self.SCREEN = self.FONT.render(self.TEXT, True, self.COLOR)

    # --- MODIFIER METHODS --- #
    # use of setter/modifier methods to encapsulate
    def setText(self, NEW_TEXT):
        self.TEXT = NEW_TEXT
        self.SCREEN = self.FONT.render(self.TEXT, True, self.COLOR)

    def setScale(self,  SCALE_X, SCALE_Y = 0):
        if SCALE_Y == 0:
            SCALE_Y = SCALE_X
        self.SCREEN = pygame.transform.scale(self.SCREEN, (int(self.getWidth()//SCALE_X), int(self.getHeight()//SCALE_Y)))



