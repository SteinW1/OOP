import pygame
import math
import animation
import physics2D

class player:
    def __init__(self, screenSize):
        self.location = (screenSize[0] * 0.5), ((screenSize[1] * 0.5) - 32)
        self.x_change = 0
        self.y_change = 0
        self.width = 16
        self.height = 32
        self.speed = 1
        self.rect = (self.location[0], self.location[1], self.width, self.height)
        self.hitbox = (self.location[0], self.location[1], self.width, self.height)

        #load spritesheet using the animator object
        self.sprite = animation.animator("images/mainsheet.png", 6, 4)

        #initialize animation settings
        self.currentSpriteFrame = 0
        self.framesInAnimation = 1
        self.direction = 0
        self.moveDown, self.moveUp, self.moveLeft, self.moveRight = False, False, False, False
        self.sprite.setAnimationIndex(0 * self.framesInAnimation, self.framesInAnimation)
        self.physics = physics2D.physics()

    # update the player for the frame
    def updatePlayer(self, display_width, display_height, gameDisplay):
        self.updatePlayerPosition()
        self.hitbox = (self.location[0], self.location[1], self.width, self.height)
        if self.detectCollision(display_width, display_height) == True:
            return True        

    #draw the player sprite onto the game canvas
    def drawPlayer(self, gameDisplay):
        
        #set animation index values
        down, up, right, left = 0, 4, 8, 12
        if self.moveDown == True:
            self.framesInAnimation = 4
            self.sprite.setAnimationIndex(down, self.framesInAnimation)
            self.sprite.animate()
        elif self.moveUp == True:
            self.framesInAnimation = 4
            self.sprite.setAnimationIndex(up, self.framesInAnimation)
            self.sprite.animate()
        elif self.moveRight == True:
            self.framesInAnimation = 4
            self.sprite.setAnimationIndex(right, self.framesInAnimation)
            self.sprite.animate()
        elif self.moveLeft == True:
            self.framesInAnimation = 4
            self.sprite.setAnimationIndex(left, self.framesInAnimation)
            self.sprite.animate()
        else:
            self.sprite.idle()

        #draw the sprite
        self.sprite.draw(gameDisplay, self.location[0], self.location[1])

    #get the users keypress and convert it into the player's movement
    def getPlayerMovement(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                self.moveRight = True
                self.x_change += self.speed
            if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                self.moveLeft = True
                self.x_change -= self.speed
            if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                self.moveDown = True
                self.y_change += self.speed
            if event.key == pygame.K_UP or event.key == pygame.K_w:
                self.moveUp = True
                self.y_change -= self.speed

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                self.moveLeft = False
                self.x_change += self.speed
            if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                self.moveRight = False
                self.x_change -= self.speed
            if event.key == pygame.K_UP or event.key == pygame.K_w:
                self.moveUp = False
                self.y_change += self.speed
            if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                self.moveDown = False
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