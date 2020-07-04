import pygame
import random
import math

class enemy:
    def __init__(self, display_width, display_height, img, speed):
        self.speed = speed
        self.width = 16
        self.height = 32
        #self.x = random.randrange(0, display_width - self.width)
        #self.y = - display_height
        self.location = (random.randrange(0, display_width - self.width), - display_height)
        self.timesHit = 0
        self.direction = random.randrange(0,4)
        self.img = img

    # detect if the enemy collides with the player or with a projectile
    def detectCollision(self, player, playerProjectiles, display_width, display_height):
        playerProjectilesCopy = playerProjectiles.copy()
        
        #detect collision with the projectiles
        for i in range(len(playerProjectilesCopy)):
            if self.location[0] < playerProjectilesCopy[i].location[0] < (self.location[0] + self.width) and self.location[1] < playerProjectilesCopy[i].location[1] < (self.location[1] + self.height):
                self.timesHit += 1
                self.randomSpawn(display_width, display_height)
                del(playerProjectiles[i])
        #detect collision with the player
        if player.location[1] < self.location[1] + self.height and player.location[1] > self.location[1]:
            if player.location[0] > self.location[0] and player.location[0] < self.location[0] + self.width or player.location[0] + player.width > self.location[0] and player.location[0] + player.width < self.location[0] + self.width:
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

    # update the (x,y) position of the enemy and respawn the enemy if it moves outside the screen
    def updateEnemyPosition(self, player, display_width, display_height):
        unitVector = self.getMovementVector(player)
        self.location = (self.location[0] + unitVector[0], self.location[1] + unitVector[1])

    #get the directional vector of the enemy as it moves toward the player and then calculate the unit movement vector
    def getMovementVector(self, player):
        positionDifference = (player.location[0] - self.location[0], player.location[1] - self.location[1])
        print(player.location, " : ", self.location)
        print(positionDifference)
        positionDifferenceLength = math.sqrt(positionDifference[0]**2 + positionDifference[1]**2)
        print(positionDifferenceLength)
        unitVector = (positionDifference[0]/positionDifferenceLength, positionDifference[1]/positionDifferenceLength)
        return unitVector

    #draw the enemy on the canvas
    def drawEnemy(self, gameDisplay):
        gameDisplay.blit(self.img, (round(self.location[0]), round(self.location[1])))

    def getTimesHit(self):
        return self.timesHit