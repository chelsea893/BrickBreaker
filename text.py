'''
title: text object
'''

from loader import Color
import pygame
from mySprite import MySprite

class Text(MySprite):
    def __init__(self, TEXT = "Hello World", COLOR = Color.WHITE):
        super().__init__()
        self.TEXT = TEXT
        self.COLOR = COLOR
        self.FONT = pygame.font.SysFont("Arial", 30)
        self.SCREEN = self.FONT.render(self.TEXT, True, self.COLOR)

    # --- MODIFIER METHODS --- #

    def setText(self, NEW_TEXT):
        self.TEXT = NEW_TEXT
        self.SCREEN = self.FONT.render(self.TEXT, True, self.COLOR)

    def setScale(self,  SCALE_X, SCALE_Y = 0):
        if SCALE_Y == 0:
            SCALE_Y = SCALE_X
        self.SCREEN = pygame.transform.scale(self.SCREEN, (int(self.getWidth()//SCALE_X), int(self.getHeight()//SCALE_Y)))



