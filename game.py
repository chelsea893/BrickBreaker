"""
title: Brick Breaker
author: Chelsea Chen
date-created: 2021-03-08
"""
import pygame
import sys
from window import Window
from loader import Color, Image
from text import Text
from box import Box
from imageSprite import ImageSprite
from random import randrange

class Game:
    pygame.init()
    def __init__(self):
        self.WINDOW = Window()
        self.WINDOW.setBackgroundColor(Color.GREY)
        self.START_GAME = False
        # TEXT
        self.TITLE = Text("BRICK BREAKER")
        self.TITLE.setPOS(self.WINDOW.getVirtualWidth()//2 - self.TITLE.getWidth()//2, 2)
        self.SCORE = 0
        self.SCORE_TEXT = Text(f"SCORE: {self.SCORE}")
        self.SCORE_TEXT.setPOS(0, 0)
        self.INSTRUCTIONS = Text("Press SPACE to start!")
        self.INSTRUCTIONS.setPOS(self.WINDOW.getVirtualWidth()//2 - self.INSTRUCTIONS.getWidth()//2, self.WINDOW.getVirtualHeight() - 70)
        self.BOXES = []
        self.END = False
        # Timer
        self.TIMER = pygame.time.Clock()
        self.TIMER_MS = 0
        self.TIME_LEFT = 30
        self.TIME_TEXT = Text(f"TIME LEFT: {self.TIME_LEFT}")
        self.TIME_TEXT.setPOS(self.WINDOW.getVirtualWidth() - self.TIME_TEXT.getWidth(), 0)

        # END TEXT
        self.END_TEXT = Text("GAME OVER!")
        self.END_TEXT.setPOS(self.WINDOW.getVirtualWidth() // 2 - self.END_TEXT.getWidth() // 2, (self.WINDOW.getVirtualHeight()-self.END_TEXT.getHeight())//2)
        self.SCORE_END = Text(f"YOUR SCORE WAS: {self.SCORE}")
        self.SCORE_END.setPOS(self.WINDOW.getVirtualWidth() // 2 - self.SCORE_END.getWidth() // 2, (self.WINDOW.getVirtualHeight() - self.SCORE_END.getHeight() + self.SCORE_END.getHeight() + 100) // 2)

        #IMAGE SPRITES
        self.MULTIPLIER= []
        for i in range(2):
            self.MULTIPLIER.append(ImageSprite(Image.MULTIPLIER))
            self.MULTIPLIER[-1].setScale(6)

        self.BOMB = []
        for i in range(2):
            self.BOMB.append(ImageSprite(Image.BOMB))
            self.BOMB[-1].setScale(6)
        self.SLOW = []
        for i in range(2):
            self.SLOW.append(ImageSprite(Image.TIME))
            self.SLOW[-1].setScale(6)
        self.placeItems()



        for i in range(24):
            self.BOXES.append(Box(90,30))
        for box in range(len(self.BOXES)):
            if box < 6:
                self.BOXES[box].setPOS((10 + (self.BOXES[box].getWidth() * box)) + box * 10,40)
            if 6 <= box <= 12:
                self.BOXES[box].setPOS((30 + (self.BOXES[box].getWidth() * (box - 6)))+ (box -6) * 10, 80)
            if  12 <= box < 18:
                self.BOXES[box].setPOS((10 + (self.BOXES[box].getWidth() * (box - 12))) + (box - 12) * 10, 120)
            if 18 <= box < 24:
                self.BOXES[box].setPOS((30 + (self.BOXES[box].getWidth() * (box - 18))) + (box - 18) * 10, 160)

        # BOXES
        self.PLAYER = Box(100, 10)
        self.PLAYER.setPOS(self.WINDOW.getVirtualWidth()//2 - self.PLAYER.getWidth()//2, self.WINDOW.getVirtualHeight() - 15)
        self.BALL = Box(10,10)
        self.BALL.setPOS(self.WINDOW.getVirtualWidth()//2 - self.BALL.getWidth() // 2, self.WINDOW.getVirtualHeight() - 30)

    def start(self, KEYPRESSES):
        if KEYPRESSES[pygame.K_SPACE] == 1:
            self.START_GAME = True

    def checkTime(self):
        if self.TIME_LEFT == 0:
            return True
        else:
            return False

    def updateTime(self):
        self.TIMER_MS += self.TIMER.tick()
        if self.TIMER_MS > 1000 and self.TIME_LEFT > 0:
            self.TIME_LEFT -= 1
            self.TIME_TEXT.setText(f"TIME LEFT: {self.TIME_LEFT}")
            self.TIMER_MS = 0

    def placeItems(self):
        for multiplier in self.MULTIPLIER:
            multiplier.setPOS(randrange(self.WINDOW.getVirtualWidth() - multiplier.getWidth()), randrange(200, self.WINDOW.getVirtualHeight() - 50))
        for bomb in self.BOMB:
            bomb.setPOS(randrange(self.WINDOW.getVirtualWidth() - bomb.getWidth()),randrange(200, self.WINDOW.getVirtualHeight() - 50))
        for slow in self.SLOW:
            slow.setPOS(randrange(self.WINDOW.getVirtualWidth() - slow.getWidth()),randrange(200, self.WINDOW.getVirtualHeight() - 50))

    def getPowerCollision(self, SPRITE1, SPRITE2):
        if pygame.Rect.colliderect(SPRITE1.getRect(), SPRITE2.getRect()):
            return True
        else:
            return False




    def getSpriteCollision(self, SPRITE1, SPRITE2):
        if pygame.Rect.colliderect(SPRITE1.getRect(), SPRITE2.getRect()):
            if abs(SPRITE2.getRect().top - SPRITE1.getRect().bottom) < 10 and SPRITE1.getSpeed() > 0:
                SPRITE1.setDirectionY(-1)
                return True
            if abs(SPRITE2.getRect().bottom - SPRITE1.getRect().top) < 10 and SPRITE1.getSpeed() > 0:
                SPRITE1.setDirectionY(1)
                return True
            if abs(SPRITE2.getRect().right - SPRITE1.getRect().left) < 10 and SPRITE1.getSpeed() > 0:
                SPRITE1.setDirectionX(-1)
                return True
            if abs(SPRITE2.getRect().left - SPRITE1.getRect().right) < 10 and SPRITE1.getSpeed() > 0:
                SPRITE1.setDirectionX(1)
                return True

    def checkBallPos(self):
        if self.BALL.getY() > self.WINDOW.getVirtualHeight() - self.BALL.getWidth():
            self.END = True




    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            # Move the player
            self.getSpriteCollision(self.BALL, self.PLAYER)
            KEYS_PRESSED = pygame.key.get_pressed()
            self.start(KEYS_PRESSED)
            self.WINDOW.clearScreen()
            self.WINDOW.getScreen().blit(self.TITLE.getScreen(), self.TITLE.getPOS())
            self.WINDOW.getScreen().blit(self.SCORE_TEXT.getScreen(), self.SCORE_TEXT.getPOS())
            self.WINDOW.getScreen().blit(self.INSTRUCTIONS.getScreen(), self.INSTRUCTIONS.getPOS())
            self.WINDOW.getScreen().blit(self.PLAYER.getScreen(), self.PLAYER.getPOS())
            self.WINDOW.getScreen().blit(self.BALL.getScreen(), self.BALL.getPOS())

            for box in self.BOXES:
                self.WINDOW.getScreen().blit(box.getScreen(), box.getPOS())



            if self.START_GAME == True:
                self.PLAYER.adMoveChkBoundaries(KEYS_PRESSED, self.WINDOW.getVirtualWidth())
                self.WINDOW.getScreen().blit(self.TIME_TEXT.getScreen(), self.TIME_TEXT.getPOS())
                self.updateTime()
                self.INSTRUCTIONS.setPOS(1000, 1000)
                # display power ups
                for multiplier in self.MULTIPLIER:
                    self.WINDOW.getScreen().blit(multiplier.getScreen(), multiplier.getPOS())
                for bomb in self.BOMB:
                    self.WINDOW.getScreen().blit(bomb.getScreen(), bomb.getPOS())
                for slow in self.SLOW:
                    self.WINDOW.getScreen().blit(slow.getScreen(), slow.getPOS())
                # get ball to bounce
                self.BALL.horizBounce(self.WINDOW)
                self.BALL.vertBounce(self.WINDOW)

                # ball collides with power up
                for multiplier in self.MULTIPLIER:
                    if self.getPowerCollision(self.BALL, multiplier):
                        multiplier.setPOS(1000,1000)
                        self.SCORE = self.SCORE*2
                        self.SCORE_TEXT.setText(f"SCORE: {self.SCORE}")

                for bomb in self.BOMB:
                    if self.getPowerCollision(self.BALL, bomb):
                        bomb.setPOS(1000,1000)
                        self.SCORE = self.SCORE - 1
                        self.SCORE_TEXT.setText(f"SCORE: {self.SCORE}")

                for slow in self.SLOW:
                    if self.getPowerCollision(self.BALL, slow):
                        slow.setPOS(1000, 1000)
                        self.TIME_LEFT = self.TIME_LEFT + 5
                        self.TIME_TEXT.setText(f"TIME LEFT: {self.TIME_LEFT}")

                # collision with box
                for box in self.BOXES:
                    self.getSpriteCollision(self.BALL,box)
                    if self.getSpriteCollision(self.BALL, box):
                        box.setPOS(1000, 1000)
                        self.SCORE = self.SCORE + 1
                        self.SCORE_TEXT.setText(f"SCORE: {self.SCORE}")

                self.checkBallPos()
                self.checkTime()
                if self.END == True or self.checkTime():
                    self.WINDOW.clearScreen()
                    self.SCORE_END.setText(f"YOUR SCORE WAS: {self.SCORE}")
                    self.WINDOW.getScreen().blit(self.END_TEXT.getScreen(), self.END_TEXT.getPOS())
                    self.WINDOW.getScreen().blit(self.SCORE_END.getScreen(), self.SCORE_END.getPOS())

            self.WINDOW.updateFrame()












if __name__ == "__main__":
    GAME = Game()
    GAME.run()