import pygame
import math
import physics2D

class projectile:
    def __init__(self, startObject, targetLocation):
        self.location = (startObject.location[0] + 1, startObject.location[1] + 1)
        self.targetLocation = targetLocation
        self.img = pygame.image.load('images/missile.png')
        self.speed = 4
        self.physics = physics2D.physics()
        self.projectileMovement = self.physics.getMovement(self.location, self.targetLocation)

    #update the projectile for the frame
    def updateProjectile(self, gameDisplay):
        self.location = (self.location[0] + self.projectileMovement[0] * self.speed, self.location[1] + self.projectileMovement[1] * self.speed)

    #draw the projectile onto the canvas
    def drawProjectile(self, gameDisplay):
        location = round(self.location[0]),round(self.location[1])
        gameDisplay.blit(self.img, (location))

    #detect if the projectile is offscreen
    def detectOffScreen(self, display_width, display_height):
        if self.location[0] > display_width or self.location[0] < 0 or self.location[1] > display_height or self.location[1] < 0:
            return True