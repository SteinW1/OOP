import pygame
import math

class player:
    def __init__(self, screenSize, image):
        #self.x = (screenSize[0] * 0.5)
        #self.y = ((screenSize[1] * 0.5) - 32)
        self.location = (screenSize[0] * 0.5), ((screenSize[1] * 0.5) - 32)
        self.img = image
        self.x_change = 0
        self.y_change = 0
        self.width = 16
        self.height = 32
        self.speed = 5
        self.hitbox = (self.location[0], self.location[1], self.width, self.height)

    # update the player for the frame
    def updatePlayer(self, display_width, display_height, gameDisplay):
        self.updatePlayerPosition()
        self.drawPlayer(gameDisplay)
        self.hitbox = (self.location[0], self.location[1], self.width, self.height)
        if self.detectCollision(display_width, display_height) == True:
            return True

    #draw the player sprite onto the game canvas
    def drawPlayer(self, gameDisplay):
        gameDisplay.blit(self.img, (self.location))

    #get the users keypress and convert it into the player's movement
    def getPlayerMovement(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                self.x_change -= self.speed
            if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                self.x_change += self.speed
            if event.key == pygame.K_UP or event.key == pygame.K_w:
                self.y_change -= self.speed
            if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                self.y_change += self.speed
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                self.x_change += self.speed
            if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                self.x_change -= self.speed
            if event.key == pygame.K_UP or event.key == pygame.K_w:
                self.y_change += self.speed
            if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                self.y_change -= self.speed
        return(self.x_change, self.y_change)

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