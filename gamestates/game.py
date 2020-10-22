import sys
import pygame
import ui
import player
import enemy
import projectile
import physics2D
from camera import camera
from gamestates import state

class Game(state.State):
    def __init__(self, gameDisplay, window, gameClock):
        state.State.__init__(self, gameDisplay, window, gameClock)
        self.score = 0
        self.scoreText = 'Score: %s' % (self.score)
        self.display_width = self.window.windowSize[0]
        self.display_height = self.window.windowSize[1]
        self.targetState = 'menu'

    def cleanup(self):
        #method for cleaning up Game state stuff
        print('Cleaning Up Game State...')
        pass

    def startup(self):
        #method for starting Game state stuff
        print('Starting Up Game State...')

        #set the next state, defaults to the transition state
        self.next = self.previousState.targetState

        #initialize the player
        self.player1 = player.player(self.window.windowSize)
        self.playerProjectiles = []

        #initialize the camera
        #self.camera1 = camera('basicCamera', self.levelWidth, self.levelHeight)

        #initialize enemies
        self.enemies = []
        numberEnemies = 5
        for i in range(0, numberEnemies):
            self.enemies.append(enemy.enemy(self.window.windowSize[0], self.window.windowSize[1]))
        pass

    def get_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            self.playerProjectiles.append(projectile.projectile(self.player1, pygame.mouse.get_pos()))
        self.player1.getPlayerMovement(event)

    ##### MAIN GAME LOOP #####
    #update function for the current game loop
    def update(self):
        #update the score text
        self.getScore()
        self.scoreTextBox = ui.textBox(0, 0, 'Score: %s' % (self.score), 'comicsansms', 20, 'left', self.gameDisplay)
        
        if self.player1.updatePlayer(self.display_width, self.display_height, self.gameDisplay) == True:
            self.next = 'gameover'
            self.done = True
        self.draw()

        #update camera offset to follow the player
        #self.camera1.update(self.player1)

        #enemies loop
        for i in self.enemies:
            i.updateEnemy(self.display_width, self.display_height, self.player1, self.gameDisplay)
            if i.detectCollision(self.player1, self.playerProjectiles, self.display_width, self.display_height) == True:
                self.next = 'gameover'
                self.done = True
        
        #player projectiles loop
        playerProjectilesCopy = self.playerProjectiles.copy()
        for i in range(len(playerProjectilesCopy)):
            playerProjectilesCopy[i].updateProjectile(self.gameDisplay)
            if playerProjectilesCopy[i].detectOffScreen(self.display_width, self.display_height) == True:
                del self.playerProjectiles[i]
    ##### END MAIN GAME LOOP #####

    def draw(self):
        self.gameDisplay.fill((255, 255, 255, 255))
        self.scoreTextBox.drawTextBox(self.gameDisplay)
        self.player1.drawPlayer(self.gameDisplay)

        for i in self.playerProjectiles:
            i.drawProjectile(self.gameDisplay)

        for i in self.enemies:
            i.drawEnemy(self.gameDisplay)
        
        #draw score
        self.scoreTextBox.drawTextBox(self.gameDisplay)
        self.score = 0

    def getScore(self):
        for i in self.enemies:
            self.score += i.timesHit