import sys
import pygame
import ui
import player
import enemy
import projectile
from states import state

class Game(state.State):
    def __init__(self):
        state.State.__init__(self)
        self.next = 'menu'
        self.score = 0
        self.scoreText = 'Score: %s' % (self.score)

    def cleanup(self):
        #method for cleaning up Game state stuff
        print('Cleaning Up Game State...')
        pass

    def startup(self, screenSize):
        #method for starting Game state stuff
        print('Starting Up Game State...')

        #initialize the player
        self.player1 = player.player(screenSize)
        self.playerProjectiles = []

        #initialize enemies
        self.enemies = []
        numberEnemies = 8
        for i in range(0, numberEnemies):
            self.enemies.append(enemy.enemy(screenSize[0], screenSize[1]))
        pass

    def get_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            self.playerProjectiles.append(projectile.projectile(self.player1))
        self.player1.getPlayerMovement(event)

    def update(self, gameDisplay, display_width, display_height):

        #update the score text
        self.getScore()
        self.scoreTextBox = ui.textBox(0, 0, 'Score: %s' % (self.score), 'comicsansms', 20, 'left', gameDisplay)
        self.player1.updatePlayer(display_width, display_height, gameDisplay)
        self.draw(gameDisplay)

        #enemies loop
        for i in self.enemies:
            i.updateEnemy(display_width, display_height, self.player1, gameDisplay)
            if i.detectCollision(self.player1, self.playerProjectiles, display_width, display_height) == True:
                print('Collision')
                self.done == True
                #crash(player1)

        print(len(self.playerProjectiles))
        
        #player projectiles loop
        playerProjectilesCopy = self.playerProjectiles.copy()
        for i in range(len(playerProjectilesCopy)):
            playerProjectilesCopy[i].updateProjectile(gameDisplay)
            if playerProjectilesCopy[i].detectOffScreen(display_width, display_height) == True:
                del self.playerProjectiles[i]

    def draw(self, gameDisplay):
        gameDisplay.fill((255, 255, 255, 255))
        self.scoreTextBox.drawTextBox(gameDisplay)
        self.player1.drawPlayer(gameDisplay)

        for i in self.playerProjectiles:
            i.drawProjectile(gameDisplay)

        for i in self.enemies:
            i.drawEnemy(gameDisplay)
        
        #draw score
        self.scoreTextBox.drawTextBox(gameDisplay)
        self.score = 0

    def getScore(self):
        for i in self.enemies:
            self.score += i.timesHit