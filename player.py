import pygame
import math
import animation

class player:
    def __init__(self, screenSize):
        self.location = (screenSize[0] * 0.5), ((screenSize[1] * 0.5) - 32)
        self.x_change = 0
        self.y_change = 0
        self.width = 16
        self.height = 32
        self.speed = 1
        self.hitbox = (self.location[0], self.location[1], self.width, self.height)

        #load spritesheet using the animator object
        self.sprite = animation.animator("images/mainsheet.png", 6, 3)

        #initialize animation settings
        self.currentSpriteFrame = 0
        self.framesInAnimation = 1
        self.direction = 0
        self.moving = False

    # update the player for the frame
    def updatePlayer(self, display_width, display_height, gameDisplay):
        self.updatePlayerPosition()
        #self.drawPlayer(gameDisplay)
        self.hitbox = (self.location[0], self.location[1], self.width, self.height)
        if self.detectCollision(display_width, display_height) == True:
            return True        

    #draw the player sprite onto the game canvas
    def drawPlayer(self, gameDisplay, currentTime):
        self.sprite.draw(gameDisplay, self.location[0], self.location[1])

        if self.moving == True:
            #self.sprite.updateSpriteFrame(self.location[0], self.location[1], self.framesInAnimation, currentTime)
            self.sprite.updateSpriteFrame(self.location[0], self.location[1], currentTime)

    #get the users keypress and convert it into the player's movement
    def getPlayerMovement(self, event):

        # set movement direction values
        down, up, right, left = 0, 1, 2, 3

        if event.type == pygame.KEYDOWN:
            self.moving = True
            if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                self.x_change += self.speed
                self.framesInAnimation = 4
                self.sprite.setAnimationIndex(right * self.framesInAnimation, self.framesInAnimation)
            if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                self.x_change -= self.speed
                self.framesInAnimation = 4
                self.sprite.setAnimationIndex(left * self.framesInAnimation, self.framesInAnimation)
            if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                self.y_change += self.speed
                self.framesInAnimation = 4
                self.sprite.setAnimationIndex(down * self.framesInAnimation, self.framesInAnimation)
            if event.key == pygame.K_UP or event.key == pygame.K_w:
                self.y_change -= self.speed
                self.framesInAnimation = 4
                self.sprite.setAnimationIndex(up * self.framesInAnimation, self.framesInAnimation)

        if event.type == pygame.KEYUP:
            self.moving = False
            if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                self.x_change += self.speed
            if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                self.x_change -= self.speed
            if event.key == pygame.K_UP or event.key == pygame.K_w:
                self.y_change += self.speed
            if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                self.y_change -= self.speed

    #detect if the player collides with the edge of the display screen
    def detectCollision(self, display_width, display_height):
        if self.location[0] > display_width - self.width or self.location[0] < 0 or self.location[1] < 0 or self.location[1] > display_height - self.height:
            return True

    #reset the player's movement to 0,0
    def resetPlayerMovement(self):
        self.x_change = 0
        self.y_change = 0

    #update the players positon based on their movement values
    def updatePlayerPosition(self):
        self.location = (self.location[0] + self.x_change), (self.location[1] + self.y_change)