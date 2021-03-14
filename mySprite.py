'''
title: Abstract Sprite Class
author: Chelsea Chen
date-created: 2021-03-08
'''
import pygame
class MySprite:
    def __init__(self): # acts as a parent class to Box, Text, and ImageSprite class
        self.WIDTH = 0
        self.HEIGHT = 0
        self.DIMENSION = (self.WIDTH, self.HEIGHT)
        self.SCREEN = None
        self.RECT = None
        self.X = 0
        self.Y = 0
        self.POS = (self.X, self.Y)
        self.SPEED = 5
        self.DIR_X = 1
        self.DIR_Y = 1

    # --- MODIFIER METHODS --- #
    # use of setter/modifier methods to encapsulate
    def setPOS(self,X, Y):
        self.X = X
        self.Y = Y
        self.updatePOS()

    def updatePOS(self):
        self.POS = (self.X, self.Y)

    def updateDimension(self):
        self.DIMENSION = (self.WIDTH, self.HEIGHT)

    def adMove(self, KEYPRESSES):
        if KEYPRESSES[pygame.K_d] == 1:
            self.X = self.X + self.SPEED
        if KEYPRESSES[pygame.K_a] == 1:
            self.X = self.X -self.SPEED
        self.updatePOS()

    def checkBoundaries(self, MAX_WIDTH, MIN_WIDTH = 0):
        if self.X > MAX_WIDTH - self.getWidth():
            self.X = MAX_WIDTH -self.getWidth()
        elif self.X < MIN_WIDTH:
            self.X = MIN_WIDTH

        self.updatePOS()

    def adMoveChkBoundaries(self, KEYPRESSES, MAX_WIDTH, MIN_WIDTH = 0):
        self.adMove(KEYPRESSES)
        self.checkBoundaries(MAX_WIDTH, MIN_WIDTH)

    def horizBounce(self, SCREEN):
        self.X = self.X + self.DIR_X*self.SPEED
        if self.X > SCREEN.getVirtualWidth() - self.getWidth():
            self.DIR_X = -1
        if self.X < 0:
            self.DIR_X = 1

        self.POS = (self.X, self.Y)

    def vertBounce(self, SCREEN):
        self.Y = self.Y + self.DIR_Y*self.SPEED
        if self.Y < 30:
            self.DIR_Y = 1

        self.POS = (self.X, self.Y)

    def setDirectionX(self,DIRECTION):
        self.DIR_X = DIRECTION

    def setDirectionY(self,DIRECTION):
        self.DIR_Y = DIRECTION

    def setSpeed(self, SPEED):
        self.SPEED = SPEED





    # ---- ACCESSOR METHODS --- #
    # use of getter/accessor methods to encapsulate

    def getScreen(self):
        return self.SCREEN

    def getPOS(self):
        return self.POS

    def getY(self):
        return self.Y

    def getSpeed(self):
        return self.SPEED

    def getWidth(self):
        return self.SCREEN.get_rect().width

    def getHeight(self):
        return self.SCREEN.get_rect().height

    def getRect(self):
        self.RECT = self.SCREEN.get_rect()
        self.RECT.x = self.X
        self.RECT.y = self.Y
        return self.RECT