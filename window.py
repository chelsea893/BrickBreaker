"""
title: Custom Classes
author: Chelsea Chen
date-created: 2021-03-08
"""

import pygame
from loader import Color


class Window:
    def __init__(self, TITLE = "Pygame", WIDTH =630, HEIGHT = 480, FPS = 30):
        self.TITLE = TITLE
        self.FPS = FPS
        self.WIDTH = WIDTH
        self.HEIGHT = HEIGHT
        self.SCREEN_DIMESIONS = (self.WIDTH, self.HEIGHT)
        self.BACKGROUND = Color.GREY
        self.FRAME = pygame.time.Clock()
        self.SCREEN = pygame.display.set_mode(self.SCREEN_DIMESIONS)
        self.SCREEN.fill(self.BACKGROUND)
        self.CAPTION = pygame.display.set_caption(self.TITLE)

    # --- MODIFIER METHODS (SETTER) --- #
    # use of setter/modifier methods to encapsulate

    def updateFrame(self):
        self.FRAME.tick(self.FPS)
        pygame.display.flip()

    def clearScreen(self):
        self.SCREEN.fill(self.BACKGROUND)

    def setBackgroundColor(self,COLOR):
        self.BACKGROUND = COLOR
        self.clearScreen()

    # --- ACCESSOR METHODS (GETTER) --- #
    # use of getter/accessor methods to encapsulate

    def getScreen(self):
        return self.SCREEN

    def getVirtualWidth(self):
        return self.SCREEN.get_rect().width

    def getVirtualHeight(self):
        return self.SCREEN.get_rect().height

