import pygame
import random
import projectile
import object2D
import animation

class enemy(object2D.Object2D):
    #initialize the enemy object
    def __init__(self, display_width, display_height):
        object2D.Object2D.__init__(self) #initalize object2D parent class properties
        self.speed = 1
        self.width = 16
        self.height = 32
        self.location = 0
        self.randomSpawn(display_width, display_height)
        self.timesHit = 0
        self.startingSide = random.randrange(0,4)
        self.projectiles = 0
        self.projectilesList = []
        self.rect = (self.location[0], self.location[1], self.width, self.height)
        self.sprite = animation.animator("images/soldier.png", 1, 1)

        # Initialize hitbox. Hitbox offset and size are currently hardcoded and determined based on the sprite
        self.hitbox = self.physics.createHitbox(self.location[0], self.location[1], 3, 7, 12, 22)

    #update method for handling all enemy processes for the frame
    def update(self, display_width, display_height, player, entitiesList, gameDisplay):
        #!TODO: add super().update() for updating hitboxes and drawing the object
        
        #update enemy hitbox for the frame
        self.hitbox = self.physics.updateHitbox(self.location[0], self.location[1])
        pygame.draw.rect(gameDisplay, (255,0,0), self.hitbox, 1)

        #update position
        vector = self.physics.getVector(self.location, player.location)
        vectorLength = self.physics.getVectorLength(vector)

        #code for updating enemy location and creating enemy projectiles
        self.projectiles = len(self.projectilesList)
        if vectorLength > 100:  # update position if distance > 100, else stop moving and send projectile at enemy
            unitVector = self.physics.getUnitVector(vector, vectorLength)
            self.location = (self.location[0] + unitVector[0] * self.speed, self.location[1] + unitVector[1] * self.speed)
        elif self.projectiles < 1:
            self.projectiles += 1
            newProjectile = projectile.projectile(self, player.location)
            self.projectilesList.append(newProjectile)
            entitiesList.append(newProjectile)

    # update the all of the enemy processes for the frame.
    def updateEnemy(self, display_width, display_height, player, gameDisplay):
        
        #update the hitbox for the frame
        self.hitbox = self.physics.updateHitbox(self.location[0], self.location[1])
        #self.hitbox = (self.location[0] + 3, self.location[1] + 7, self.width - 6, self.height - 9)
        pygame.draw.rect(gameDisplay, (255,0,0), self.hitbox, 1)

        #update position
        vector = self.physics.getVector(self.location, player.location)
        vectorLength = self.physics.getVectorLength(vector)
        
        # code for creating projectiles
        if vectorLength > 100:  # update position if distance > 100, else stop moving and send projectile at enemy
            unitVector = self.physics.getUnitVector(vector, vectorLength)
            self.location = (self.location[0] + unitVector[0] * self.speed, self.location[1] + unitVector[1] * self.speed)
        elif len(self.projectiles) < 1: #check if projectile has already been fired
            self.projectiles.append(projectile.projectile(self, player.location))

        projectilesCopy = self.projectiles.copy()
        for i in range(len(projectilesCopy)):
            projectilesCopy[i].updateProjectile(gameDisplay)
            if projectilesCopy[i].detectOffScreen(display_width, display_height) == True:
                del self.projectiles[i]

    # detect if the enemy collides with the player or with a projectile or with the edge of the screen
    def detectCollision(self, player, playerProjectiles, display_width, display_height):
        #detect collision with the projectiles
        playerProjectilesCopy = playerProjectiles.copy()
        for i in range(len(playerProjectilesCopy)): # uses [:] to create a bopy of playerProjectiles to iterate through
            if self.location[0] < playerProjectilesCopy[i].location[0] < (self.location[0] + self.width) and self.location[1] < playerProjectilesCopy[i].location[1] < (self.location[1] + self.height):
                self.timesHit += 1
                self.randomSpawn(display_width, display_height)                
                del playerProjectiles[i]
                self.projectiles = []

        #detect collision with the player
        if self.physics.detectCollision(player.hitbox, self.hitbox) == True:
            return True

        #detect collision with the edge of screen
        if self.physics.detectCollision(self.hitbox, (0, 0, display_width, display_height)) == False:
            return True

    #respawn the enemy with a random position outside the screen and with a random direction
    def randomSpawn(self, display_width, display_height):
        self.startingSide = random.randrange(0,4)
        #~~~~   0 = down, 1 = right, 2 = up, 3 = left
        if self.startingSide == 0:
            newX = random.randrange(0, display_width - self.width) 
            self.location = newX, 0 - self.height  
        elif self.startingSide == 1:                                           
            newY = random.randrange(0, display_height - self.height)
            self.location = 0 - self.width, newY
        elif self.startingSide == 2:
            newX = random.randrange(0 , display_width - self.width)
            self.location = newX, display_height
        elif self.startingSide == 3:
            newY = random.randrange(0, display_height - self.height)
            self.location = display_width, newY