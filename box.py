'''
title: box class
author: Chelsea Chen
date-created: 2021-03-08
'''

import pygame
from loader import Color
from mySprite import MySprite


class Box(MySprite):
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
    """
    def adMove(self, KEYPRESSES):
        super().adMove(KEYPRESSES)
    """

if __name__ == "__main__":
    from window import Window
    import sys
    pygame.init()

    WINDOW = Window()

    BOX1 = Box(50,50)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()


        KEYS_PRESSED = pygame.key.get_pressed()
        BOX1.wasdMove(KEYS_PRESSED)
        WINDOW.clearScreen()
        WINDOW.getScreen().blit(BOX1.getScreen(), BOX1.getPOS())
        WINDOW.updateFrame()

