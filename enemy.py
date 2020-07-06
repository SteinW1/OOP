import pygame
import random
import math
import projectile

class enemy:
    def __init__(self, display_width, display_height, img, speed, projectileImg):
        self.speed = speed
        self.width = 16
        self.height = 32
        self.locatoin = ()
        self.randomSpawn(display_width, display_height)
        self.timesHit = 0
        self.direction = random.randrange(0,4)
        self.img = img
        self.projectileImg = projectileImg
        self.projectiles = []
        self.collided = False

    # update the all of the enemy processes for the frame.
    def updateEnemy(self, display_width, display_height, player, playerProjectiles, gameDisplay):
        #detectCollision(player, playerProjectiles, display_width, display_height)
        self.drawEnemy(gameDisplay)
        hitbox = (self.location[0], self.location[1], self.width, self.height)
        pygame.draw.rect(gameDisplay, (255,0,0), hitbox, 1)
        # this if statement updates the enemy position while it checks if the enemy will create a projectile
        if self.updateEnemyPosition(player, display_width, display_height) == True and len(self.projectiles) < 1:
            self.projectiles.append(projectile.projectile(self, self.projectileImg, 4))
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
        if player.location[1] < self.location[1] + self.height and player.location[1] > self.location[1]:
            if player.location[0] > self.location[0] and player.location[0] < self.location[0] + self.width or player.location[0] + player.width > self.location[0] and player.location[0] + player.width < self.location[0] + self.width:
                self.collided = True
                return True

        if player.location[0] <= (self.location[0] + self.width) and (player.location[0] + player.width) >= self.location[0] and player.location[1] <= (self.location[1] + self.height)
            self.collide = True
            return True

        


        
        #detect collision with the edge of screen
        if self.location[1] > display_height or self.location[1] < (0 - self.height)  or self.location[0] > display_width or self.location[0] < (0 - self.width):
            self.randomSpawn(display_width, display_height)

    #respawn the enemy with a random position outside the screen and with a random direction
    def randomSpawn(self, display_width, display_height):
        self.direction = random.randrange(0,4)
        
        #reset the collided boolean after respawn
        self.Collided = False

        #~~~~   0 = down, 1 = right, 2 = up, 3 = left
        if self.direction == 0:
            newX = random.randrange(0, display_width - self.width) 
            self.location = newX, 0 - self.height
            #return newX, 0 - self.height        
        elif self.direction == 1:                                           
            newY = random.randrange(0, display_height - self.height)
            self.location = 0 - self.width, newY
            #return 0 - self.width, newY
        elif self.direction == 2:
            newX = random.randrange(0 , display_width - self.width)
            self.location = newX, display_height
            #return newX, display_height
        elif self.direction == 3:
            newY = random.randrange(0, display_height - self.height)
            self.location = display_width, newY
            #return display_width, newY

    # update the (x,y) position of the enemy and respawn the enemy if it moves outside the screen
    def updateEnemyPosition(self, player, display_width, display_height):
        positionDifference = self.getPositionDifference(player)
        positionDifferenceLength = self.getPositionDifferenceLength(positionDifference)
        if positionDifferenceLength > 100:
            unitVector = self.getMovementUnitVector(positionDifference, positionDifferenceLength)
            #unitVector = self.getMovement(player)
            self.location = (self.location[0] + unitVector[0], self.location[1] + unitVector[1])
            return False
        else:
            return True

    #get the unit vector after being given a directional vector and its length
    def getMovementUnitVector(self, vector, vectorLength):
        unitVector = (vector[0]/vectorLength, vector[1]/vectorLength)
        return unitVector

    #get the hypotenuse of the movement vector to determine the vector length
    def getPositionDifferenceLength(self, vector):
        positionDifferenceLength = math.sqrt(vector[0]**2 + vector[1]**2)
        return positionDifferenceLength

    ''' Gets the position difference vector between the enemy and another object. 
        The 'otherObject' must have a (.location[x,y]) attribute for the method to work'''
    def getPositionDifference(self, otherObject):
        positionDifferenceVector = (otherObject.location[0] - self.location[0], otherObject.location[1] - self.location[1])
        return positionDifferenceVector

    #draw the enemy on the canvas
    def drawEnemy(self, gameDisplay):
        gameDisplay.blit(self.img, (round(self.location[0]), round(self.location[1])))

    def getTimesHit(self):
        return self.timesHit