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

# Creates power ups
def powerUps():
    MULTIPLIER = []
    for i in range(randrange(2, 3)):
        MULTIPLIER.append(ImageSprite(Image.MULTIPLIER))
        MULTIPLIER[-1].setScale(6)

    BOMB = []
    for i in range(randrange(2, 4)):
        BOMB.append(ImageSprite(Image.BOMB))
        BOMB[-1].setScale(40)
    SLOW = []
    for i in range(randrange(2, 3)):
        SLOW.append(ImageSprite(Image.TIME))
        SLOW[-1].setScale(60)
    return MULTIPLIER, BOMB, SLOW

class Game:
    pygame.init()
    def __init__(self):
        self.WINDOW = Window()
        self.WINDOW.setBackgroundColor(Color.GREY)
        self.START_GAME = False

        # Start title
        self.TITLE = Text("BRICK BREAKER")
        self.TITLE.setPOS(self.WINDOW.getVirtualWidth()//2 - self.TITLE.getWidth()//2, 2)
        self.SCORE = 0
        self.SCORE_TEXT = Text(f"SCORE: {self.SCORE}")
        self.SCORE_TEXT.setPOS(0, 0)
        self.INSTRUCTIONS = Text("Press SPACE to start!")
        self.INSTRUCTIONS.setPOS(self.WINDOW.getVirtualWidth()//2 - self.INSTRUCTIONS.getWidth()//2, self.WINDOW.getVirtualHeight() - 70)

        self.BOXES = []
        self.END = False
        self.RESTART = False
        self.NEWSPEED = 0
        self.TIME_STOPPED = 0
        self.FINAL_SCORE = 0
        self.START_LEVEL = False
        self.STARTUP = False
        # Timer
        self.TIMER = pygame.time.Clock()
        self.TIMER_MS = 0
        self.TIME_LEFT = 40
        self.TIME_TEXT = Text(f"TIME LEFT: {self.TIME_LEFT}")
        self.TIME_TEXT.setPOS(self.WINDOW.getVirtualWidth() - self.TIME_TEXT.getWidth(), 0)

        #LIVES TEXT
        self.NUMOFLIVES = 3
        self.LIVES_TEXT = Text("LIVES:")
        self.LIVES_TEXT.setPOS(200, 0)


        #RESTART
        self.RESTART_TEXT = Text("PRESS s/S TO START AGAIN!")
        self.RESTART_TEXT.setPOS(self.WINDOW.getVirtualWidth() // 2 - self.RESTART_TEXT.getWidth() // 2, self.WINDOW.getVirtualHeight() - 70)

        #BEGIN LEVEL 2 TEXT
        self.STARTLEVEL2 = False
        self.LEVEL2_TEXT = Text("PRESS y/Y TO START LEVEL 2!")
        self.LEVEL2_TEXT.setPOS(self.WINDOW.getVirtualWidth() // 2 - self.LEVEL2_TEXT.getWidth() // 2,self.WINDOW.getVirtualHeight() - 70)

        # END TEXT
        self.END_TEXT = Text("GAME OVER!")
        self.END_TEXT.setPOS(self.WINDOW.getVirtualWidth() // 2 - self.END_TEXT.getWidth() // 2, (self.WINDOW.getVirtualHeight()-self.END_TEXT.getHeight())//2)
        self.SCORE_END = Text(f"YOUR SCORE WAS: {self.SCORE}")
        self.SCORE_END.setPOS(self.WINDOW.getVirtualWidth() // 2 - self.SCORE_END.getWidth() // 2, (self.WINDOW.getVirtualHeight() - self.SCORE_END.getHeight() + self.SCORE_END.getHeight() + 100) // 2)

        #IMAGE SPRITES
        self.LIVES = []
        for i in range(3):
            self.LIVES.append(ImageSprite(Image.LIVES))
            self.LIVES[-1].setScale(60)
        self.MULTIPLIER, self.BOMB, self.SLOW = powerUps()
        self.MULTIPLIER2, self.BOMB2, self.SLOW2 = powerUps()
        self.placeItems()


        # level 1
        for i in range(24): #6
            self.BOXES.append(Box(90,30)) # 90,30
        for box in range(len(self.BOXES)):
            if box < 6: #6
                self.BOXES[box].setPOS((10 + (self.BOXES[box].getWidth() * box)) + box * 10,40) # 10
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

        # level 2

        self.OBSTACLES = []
        for i in range(2):
            self.OBSTACLES.append(Box(150, 20, Color.BLACK))
        self.OBSTACLES[0].setPOS(0, 200)
        self.OBSTACLES[1].setPOS(self.WINDOW.getVirtualWidth()-self.OBSTACLES[1].getWidth(), 200)

        self.BOXES2 = []
        for i in range(24):
            self.BOXES2.append(Box(90,30))
        for box in range(len(self.BOXES2)):
            if box < 5:
                self.BOXES2[box].setPOS((50 + (self.BOXES2[box].getWidth() * box)) + box * 20, 40)
            if 5 <= box <= 11:
                self.BOXES2[box].setPOS((20 + (self.BOXES2[box].getWidth() * (box - 5)) + (box - 5) * 10), 80)
            if 11 <= box <= 16:
                self.BOXES2[box].setPOS((50 + (self.BOXES2[box].getWidth() * (box - 11)) + (box - 11) * 10), 120)
            if 16 <= box <= 18:
                self.BOXES2[box].setPOS((210 + (self.BOXES2[box].getWidth() * (box - 16)) + (box - 16) * 10), 200)
            if 18 <= box <= 24:
                self.BOXES2[box].setPOS((20 + (self.BOXES2[box].getWidth() * (box - 18)) + (box - 18) * 10), 250)






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
        for i in range(len(self.LIVES)):
            self.LIVES[i].setPOS((300 + (self.LIVES[i].getWidth() * i)) + i * 10, 0)
        for multiplier in self.MULTIPLIER:
            multiplier.setPOS(randrange(self.WINDOW.getVirtualWidth() - multiplier.getWidth()), randrange(45, self.WINDOW.getVirtualHeight() - 80))
        for bomb in self.BOMB:
            bomb.setPOS(randrange(self.WINDOW.getVirtualWidth() - bomb.getWidth()),randrange(35, self.WINDOW.getVirtualHeight() - 80))
        for slow in self.SLOW:
            slow.setPOS(randrange(self.WINDOW.getVirtualWidth() - slow.getWidth()),randrange(35,self.WINDOW.getVirtualHeight() - 80))

        for multiplier in self.MULTIPLIER2:
            multiplier.setPOS(randrange(self.WINDOW.getVirtualWidth() - multiplier.getWidth()), randrange(45, self.WINDOW.getVirtualHeight() - 80))
        for bomb in self.BOMB2:
            bomb.setPOS(randrange(self.WINDOW.getVirtualWidth() - bomb.getWidth()),randrange(35, self.WINDOW.getVirtualHeight() - 80))
        for slow in self.SLOW2:
            slow.setPOS(randrange(self.WINDOW.getVirtualWidth() - slow.getWidth()),randrange(35,self.WINDOW.getVirtualHeight() - 80))

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
        if (self.BALL.getY() == self.WINDOW.getVirtualHeight() - self.BALL.getWidth()) and len(self.LIVES) == 1:
            self.END = True
        elif (self.BALL.getY() == self.WINDOW.getVirtualHeight() - self.BALL.getWidth()) and len(self.LIVES) > 1:
            self.RESTART_TEXT.setPOS(self.WINDOW.getVirtualWidth() // 2 - self.RESTART_TEXT.getWidth() // 2,self.WINDOW.getVirtualHeight() - 70)
            self.TIME_TEXT.setPOS(1000,1000)
            self.LIVES.pop()
            self.BALL.setPOS(self.WINDOW.getVirtualWidth() // 2 - self.BALL.getWidth() // 2,self.WINDOW.getVirtualHeight() - 30)
            self.PLAYER.setPOS(self.WINDOW.getVirtualWidth() // 2 - self.PLAYER.getWidth() // 2, self.WINDOW.getVirtualHeight() - 15)
            self.NEWSPEED = self.BALL.getSpeed()
            self.BALL.setSpeed(0)
            self.TIME_STOPPED = self.TIME_LEFT
            self.RESTART = True

    def startLevel2(self):
        if len(self.BOXES) == 0 and self.STARTLEVEL2 == False:
            self.TIME_TEXT.setPOS(1000, 1000)
            self.BALL.setPOS(self.WINDOW.getVirtualWidth() // 2 - self.BALL.getWidth() // 2, self.WINDOW.getVirtualHeight() - 30)
            self.PLAYER.setPOS(self.WINDOW.getVirtualWidth() // 2 - self.PLAYER.getWidth() // 2,self.WINDOW.getVirtualHeight() - 15)
            self.BALL.setSpeed(0)
            self.TIMES = 50
            self.TIME_LEFT = self.TIMES
            self.STARTUP = True

    def startLevel(self):
        KEYPRESS = pygame.key.get_pressed()
        if KEYPRESS[pygame.K_y] == 1:
            self.BALL.setSpeed(5)
            self.STARTLEVEL2 = True




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
                self.WINDOW.getScreen().blit(self.LIVES_TEXT.getScreen(), self.LIVES_TEXT.getPOS())
                self.INSTRUCTIONS.setPOS(1000, 1000)
                self.TITLE.setPOS(1000, 1000)
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

                #lives of player
                for lives in self.LIVES:
                    self.WINDOW.getScreen().blit(lives.getScreen(), lives.getPOS())


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
                        self.BOXES.pop(self.BOXES.index(box))
                        self.SCORE = self.SCORE + 1
                        self.SCORE_TEXT.setText(f"SCORE: {self.SCORE}")

                self.checkBallPos()
                if self.RESTART == True:
                    self.WINDOW.getScreen().blit(self.RESTART_TEXT.getScreen(), self.RESTART_TEXT.getPOS())
                    KEYPRESS = pygame.key.get_pressed()
                    if KEYPRESS[pygame.K_s] == 1:
                        self.BALL.setSpeed(self.NEWSPEED)
                        self.RESTART_TEXT.setPOS(1000, 1000)
                        self.TIME_LEFT = self.TIME_STOPPED
                        self.TIME_TEXT.setText(f"TIME LEFT: {self.TIME_LEFT}")
                        self.TIME_TEXT.setPOS(self.WINDOW.getVirtualWidth() - self.TIME_TEXT.getWidth(), 0)


                self.startLevel2()
                if self.STARTUP == True:
                    if len(self.MULTIPLIER) > 0:
                        for multi in self.MULTIPLIER:
                            self.MULTIPLIER.pop(self.MULTIPLIER.index(multi))

                    if len(self.BOMB) > 0:
                        for bomb in self.BOMB:
                            self.BOMB.pop(self.BOMB.index(bomb))

                    if len(self.SLOW) > 0:
                        for slow in self.SLOW:
                            self.SLOW.pop(self.SLOW.index(slow))

                    self.WINDOW.getScreen().blit(self.LEVEL2_TEXT.getScreen(), self.LEVEL2_TEXT.getPOS())
                    for box in self.BOXES2:
                        self.WINDOW.getScreen().blit(box.getScreen(), box.getPOS())
                    for obstacles in self.OBSTACLES:
                        self.WINDOW.getScreen().blit(obstacles.getScreen(), obstacles.getPOS())
                    self.startLevel()
                    if self.STARTLEVEL2 == True:
                        for multiplier in self.MULTIPLIER2:
                            self.WINDOW.getScreen().blit(multiplier.getScreen(), multiplier.getPOS())
                        for bomb in self.BOMB2:
                            self.WINDOW.getScreen().blit(bomb.getScreen(), bomb.getPOS())
                        for slow in self.SLOW2:
                            self.WINDOW.getScreen().blit(slow.getScreen(), slow.getPOS())
                        self.LEVEL2_TEXT.setPOS(1000, 1000)
                        self.TIME_TEXT.setText(f"TIME LEFT: {self.TIME_LEFT}")
                        self.TIME_TEXT.setPOS(self.WINDOW.getVirtualWidth() - self.TIME_TEXT.getWidth(), 0)

                        for multiplier in self.MULTIPLIER2:
                            if self.getPowerCollision(self.BALL, multiplier):
                                multiplier.setPOS(1000, 1000)
                                self.SCORE = self.SCORE * 2
                                self.SCORE_TEXT.setText(f"SCORE: {self.SCORE}")

                        for bomb in self.BOMB2:
                            if self.getPowerCollision(self.BALL, bomb):
                                bomb.setPOS(1000, 1000)
                                self.SCORE = self.SCORE - 1
                                self.SCORE_TEXT.setText(f"SCORE: {self.SCORE}")

                        for slow in self.SLOW2:
                            if self.getPowerCollision(self.BALL, slow):
                                slow.setPOS(1000, 1000)
                                self.TIME_LEFT = self.TIME_LEFT + 5
                                self.TIME_TEXT.setText(f"TIME LEFT: {self.TIME_LEFT}")




                        # collision with box
                        for box in self.BOXES2:
                            self.getSpriteCollision(self.BALL, box)
                            if self.getSpriteCollision(self.BALL, box):
                                self.BOXES2.pop(self.BOXES2.index(box))
                                self.SCORE = self.SCORE + 1
                                self.SCORE_TEXT.setText(f"SCORE: {self.SCORE}")

                        # collision with obstacle
                        for obstacles in self.OBSTACLES:
                            self.getSpriteCollision(self.BALL, obstacles)



                self.checkTime()
                self.updateTime()
                if self.END == True or self.checkTime():
                    self.WINDOW.clearScreen()
                    self.FINAL_SCORE = self.SCORE
                    self.SCORE_END.setText(f"YOUR SCORE WAS: {self.FINAL_SCORE}")
                    self.WINDOW.getScreen().blit(self.END_TEXT.getScreen(), self.END_TEXT.getPOS())
                    self.WINDOW.getScreen().blit(self.SCORE_END.getScreen(), self.SCORE_END.getPOS())





            self.WINDOW.updateFrame()












if __name__ == "__main__":
    GAME = Game()
    GAME.run()