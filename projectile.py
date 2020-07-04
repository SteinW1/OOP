import pygame
import math

class projectile:
    def __init__(self, player, img, speed):
        self.location = (player.location)
        self.img = img
        self.speed = speed
        self.projectileVector = self.getProjectileVector(player.location)
        self.projectileMovement = (self.projectileVector[0] * self.speed, self.projectileVector[1] * self.speed)

    #get the directional vector of a created projectile and calculate the unit movement vector
    def getProjectileVector(self, location):
        mousePosition = pygame.mouse.get_pos()
        positionDifference = (mousePosition[0] - location[0], mousePosition[1] - location[1])
        positiontDifferenceLength = math.sqrt(positionDifference[0]**2 + positionDifference[1]**2)
        unitVector = (positionDifference[0]/positiontDifferenceLength, positionDifference[1]/positiontDifferenceLength)
        return unitVector

    #draw the projectile onto the canvas
    def drawProjectile(self, gameDisplay):
        location = round(self.location[0]),round(self.location[1])
        gameDisplay.blit(self.img, (location))

    #update the projectiles (x,y) position and then send it to be drawn
    def updateProjectilePosition(self, gameDisplay):
        self.location = (self.location[0] + self.projectileMovement[0], self.location[1] + self.projectileMovement[1])
        self.drawProjectile(gameDisplay)
    
    #detect if the projectile 
    def detectOffScreen(self, display_width, display_height):
        if self.location[0] > display_width or self.location[0] < 0 or self.location[1] > display_height or self.location[1] < 0:
            return True