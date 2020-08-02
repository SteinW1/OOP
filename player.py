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
        self.moveDown, self.moveUp, self.moveLeft, self.moveRight = False, False, False, False
        self.sprite.setAnimationIndex(0 * self.framesInAnimation, self.framesInAnimation)

    # update the player for the frame
    def updatePlayer(self, display_width, display_height, gameDisplay):
        self.updatePlayerPosition()
        self.hitbox = (self.location[0], self.location[1], self.width, self.height)
        if self.detectCollision(display_width, display_height) == True:
            return True        

    #draw the player sprite onto the game canvas
    def drawPlayer(self, gameDisplay, currentTime):

        #draw the sprite
        self.sprite.draw(gameDisplay, self.location[0], self.location[1])

        #check if its time for the sprite to be updated
        self.sprite.update(currentTime)

        if self.moveDown == True or self.moveUp == True or self.moveLeft == True or self.moveRight == True:
            self.sprite.animate()
        else:
            self.sprite.idle()

    #get the users keypress and convert it into the player's movement
    def getPlayerMovement(self, event):

        # set animation index values
        down, up, right, left = 0, 4, 8, 12

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                self.moveRight = True
                self.x_change += self.speed
                self.framesInAnimation = 4
                self.sprite.setAnimationIndex(right, self.framesInAnimation)
                self.moveRight = True
            if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                self.moveLeft = True
                self.x_change -= self.speed
                self.framesInAnimation = 4
                self.sprite.setAnimationIndex(left, self.framesInAnimation)
            if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                self.moveDown = True
                self.y_change += self.speed
                self.framesInAnimation = 4
                self.sprite.setAnimationIndex(down, self.framesInAnimation)
            if event.key == pygame.K_UP or event.key == pygame.K_w:
                self.moveUp = True
                self.y_change -= self.speed
                self.framesInAnimation = 4
                self.sprite.setAnimationIndex(up, self.framesInAnimation)

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