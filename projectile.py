import pygame
import math
import object2D
import animation

class projectile(object2D.Object2D):
    def __init__(self, startObject, targetLocation):
        object2D.Object2D.__init__(self) #initalize object2D parent class properties
        self.location = (startObject.location[0] + (startObject.width / 2), startObject.location[1] + (startObject.height / 2))
        self.width, self.height = 16, 16
        self.rect = (self.location[0], self.location[1], self.width, self.height)
        self.targetLocation = targetLocation
        self.speed = 4
        self.projectileMovement = self.physics.getMovement(self.location, self.targetLocation)
        self.sprite = animation.animator("images/missile.png", 1, 1)
        self.parentObject = startObject #keep track of what object the projectile came from

    #update the projectile for the frame
    def update(self, gameDisplay):
        self.location = (self.location[0] + self.projectileMovement[0] * self.speed, self.location[1] + self.projectileMovement[1] * self.speed)
        self.draw(gameDisplay)

    #detect if the projectile is offscreen
    def detectOffScreen(self, display_width, display_height):
        if self.location[0] > display_width or self.location[0] < 0 or self.location[1] > display_height or self.location[1] < 0:
            self.active == False