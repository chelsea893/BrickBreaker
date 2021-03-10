"""
title: Brick Breaker
author: Chelsea Chen
date-created: 2021-03-08
"""
import pygame
import sys
from window import Window
from loader import Color
from text import Text
from box import Box

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
        # END TEXT
        self.END_TEXT = Text("GAME OVER!")
        self.END_TEXT.setPOS(self.WINDOW.getVirtualWidth() // 2 - self.END_TEXT.getWidth() // 2, (self.WINDOW.getVirtualHeight()-self.END_TEXT.getHeight())//2)
        self.SCORE_END = Text(f"YOUR SCORE WAS: {self.SCORE}")
        self.SCORE_END.setPOS(self.WINDOW.getVirtualWidth() // 2 - self.SCORE_END.getWidth() // 2, (self.WINDOW.getVirtualHeight() - self.SCORE_END.getHeight() + self.SCORE_END.getHeight() + 100) // 2)

        for i in range(10):
            self.BOXES.append(Box(90,60))
        for box in range(len(self.BOXES)):
            self.row = 1
            if box < 5:
                self.BOXES[box].setPOS((self.BOXES[box].getWidth() + (self.BOXES[box].getWidth() * box)) + box * 10,100)
            if 5 <= box <= 10:
                self.row = self.row + 1
                self.BOXES[box].setPOS((self.BOXES[box].getWidth() + (self.BOXES[box].getWidth() * (box - 5)))+ (box -5) * 10, 180)








        # BOXES
        self.PLAYER = Box(100, 10)
        self.PLAYER.setPOS(self.WINDOW.getVirtualWidth()//2 - self.PLAYER.getWidth()//2, self.WINDOW.getVirtualHeight() - 15)
        self.BALL = Box(10,10)
        self.BALL.setPOS(self.WINDOW.getVirtualWidth()//2 - self.BALL.getWidth() // 2, self.WINDOW.getVirtualHeight() - 30)

    def start(self, KEYPRESSES):
        if KEYPRESSES[pygame.K_SPACE] == 1:
            self.START_GAME = True

    def getSpriteCollision(self, SPRITE1, SPRITE2):
        if pygame.Rect.colliderect(SPRITE1.getRect(), SPRITE2.getRect()):
            if abs(SPRITE2.getRect().top - SPRITE1.getRect().bottom) < 10 and SPRITE1.getSpeed() > 0:
                SPRITE1.setDirectionY(-1)
                return True
            if abs(SPRITE2.getRect().bottom - SPRITE1.getRect().top) < 10 and SPRITE1.getSpeed() > 0:
                SPRITE1.setDirectionY(1)
                return True
            if abs(SPRITE2.getRect().right - SPRITE1.getRect().left) < 10 and SPRITE1.getSpeed() > 0:
                SPRITE1.setDirectionX(1)
                return True
            if abs(SPRITE2.getRect().left - SPRITE1.getRect().right) < 10 and SPRITE1.getSpeed() > 0:
                SPRITE1.setDirectionX(-1)
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
                self.INSTRUCTIONS.setPOS(1000, 1000)
                self.BALL.horizBounce(self.WINDOW)
                self.BALL.vertBounce(self.WINDOW)
                for box in self.BOXES:
                    self.getSpriteCollision(self.BALL,box)
                    if self.getSpriteCollision(self.BALL, box):
                        box.setPOS(1000, 1000)
                        self.SCORE = self.SCORE + 1
                        self.SCORE_TEXT.setText(f"SCORE: {self.SCORE}")

                self.checkBallPos()
                if self.END == True:
                    self.WINDOW.clearScreen()
                    self.SCORE_END.setText(f"YOUR SCORE WAS: {self.SCORE}")
                    self.WINDOW.getScreen().blit(self.END_TEXT.getScreen(), self.END_TEXT.getPOS())
                    self.WINDOW.getScreen().blit(self.SCORE_END.getScreen(), self.SCORE_END.getPOS())

            self.WINDOW.updateFrame()












if __name__ == "__main__":
    GAME = Game()
    GAME.run()