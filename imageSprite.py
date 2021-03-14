'''
title: Image Sprites
'''
import pygame
from mySprite import MySprite

class ImageSprite(MySprite):
    def __init__(self, IMAGE_FILE):
        super().__init__()
        self.FILE_LOCATION = IMAGE_FILE
        self.SCREEN = pygame.image.load(self.FILE_LOCATION).convert_alpha()

    # --- MODIFIER METHODS --- #

    def setScale(self,  SCALE_X, SCALE_Y = 0):
        if SCALE_Y == 0:
            SCALE_Y = SCALE_X
        self.SCREEN = pygame.transform.scale(self.SCREEN, (int(self.getWidth()//SCALE_X), int(self.getHeight()//SCALE_Y)))
