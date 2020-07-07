import pygame
import random
import projectile
import physics2D

class enemy:
    #initialize the enemy object
    def __init__(self, display_width, display_height, img, speed, projectileImg):
        self.speed = speed
        self.width = 16
        self.height = 32
        self.location = ()
        self.randomSpawn(display_width, display_height)
        self.timesHit = 0
        self.direction = random.randrange(0,4)
        self.img = img
        self.projectileImg = projectileImg
        self.projectiles = []
        self.physics = physics2D.physics()

    # update the all of the enemy processes for the frame.
    def updateEnemy(self, display_width, display_height, player, playerProjectiles, gameDisplay):
        self.drawEnemy(gameDisplay)
        #update the hitbox for the frame
        hitbox = (self.location[0], self.location[1], self.width, self.height)
        pygame.draw.rect(gameDisplay, (255,0,0), hitbox, 1)
        #update position
        vector = self.physics.getVector(self.location, player.location)
        vectorLength = self.physics.getVectorLength(vector)
        
        if vectorLength > 100:  # update position if distance > 100, else stop moving and send projectile at enemy
            unitVector = self.physics.getUnitVector(vector, vectorLength)
            self.location = (self.location[0] + unitVector[0] * self.speed, self.location[1] + unitVector[1] * self.speed)
        elif len(self.projectiles) < 1: #check if projectile has already been fired
            self.projectiles.append(projectile.projectile(self, self.projectileImg, 4))
        
        #draw projectiles
        for i in self.projectiles:
            i.drawProjectile(gameDisplay)

    # detect if the enemy collides with the player or with a projectile or with the edge of the screen
    def detectCollision(self, player, playerProjectiles, display_width, display_height):
        playerProjectilesCopy = playerProjectiles.copy()
        
        #detect collision with the projectiles
        for i in range(len(playerProjectilesCopy)):
            if self.location[0] < playerProjectilesCopy[i].location[0] < (self.location[0] + self.width) and self.location[1] < playerProjectilesCopy[i].location[1] < (self.location[1] + self.height):
                self.timesHit += 1
                self.randomSpawn(display_width, display_height)
                del(playerProjectiles[i])
                self.projectiles = []

        #detect collision with the player
        if (player.location[0] <= (self.location[0] + self.width) and (player.location[0] + player.width) >= self.location[0] and player.location[1] <= (self.location[1] + self.height) and (player.location[1] + player.height) >= self.location[1]):
            self.collide = True
            return True

        #detect collision with the edge of screen
        if self.location[1] > display_height or self.location[1] < (0 - self.height)  or self.location[0] > display_width or self.location[0] < (0 - self.width):
            self.randomSpawn(display_width, display_height)

    #respawn the enemy with a random position outside the screen and with a random direction
    def randomSpawn(self, display_width, display_height):
        self.direction = random.randrange(0,4)
        #~~~~   0 = down, 1 = right, 2 = up, 3 = left
        if self.direction == 0:
            newX = random.randrange(0, display_width - self.width) 
            self.location = newX, 0 - self.height  
        elif self.direction == 1:                                           
            newY = random.randrange(0, display_height - self.height)
            self.location = 0 - self.width, newY
        elif self.direction == 2:
            newX = random.randrange(0 , display_width - self.width)
            self.location = newX, display_height
        elif self.direction == 3:
            newY = random.randrange(0, display_height - self.height)
            self.location = display_width, newY


    #draw the enemy on the canvas
    def drawEnemy(self, gameDisplay):
        gameDisplay.blit(self.img, (round(self.location[0]), round(self.location[1])))