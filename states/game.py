import sys
import pygame
import ui
import player
import enemy
from states import state

class Game(state.State):
    def __init__(self):
        state.State.__init__(self)
        self.next = 'menu'
        self.score = 0
        self.scoreText = 'Score: %s' % (self.score)
        #self.scoreText = ui.textBox(0, 0, 'Score: %s' % (self.score), 'comicsansms', 20, 'left', gameDisplay)

    def cleanup(self):
        #method for cleaning up Game state stuff
        print('Cleaning Up Game State...')
        pass

    def startup(self, screenSize):
        #method for starting Game state stuff
        print('Starting Up Game State...')

        #initialize the player
        self.player1 = player.player(screenSize)
    

        pass

    def get_event(self, event):
        if event.type == pygame.KEYDOWN:
            print('Game State keydown')
        #if event.type == pygame.MOUSEBUTTONDOWN:
            #playerProjectiles.append(projectile.projectile(player1, missileImg, 4))
        self.player1.getPlayerMovement(event)

    def update(self, gameDisplay, display_width, display_height):

        #update the score text
        self.score = self.getScore()
        self.scoreTextBox = ui.textBox(0, 0, 'Score: %s' % (self.score), 'comicsansms', 20, 'left', gameDisplay)
        self.player1.updatePlayer(display_width, display_height, gameDisplay)
        self.draw(gameDisplay)

    def draw(self, gameDisplay):
        gameDisplay.fill((0,0,255))
        self.scoreTextBox.drawTextBox(gameDisplay)
        self.player1.drawPlayer(gameDisplay)

    def getScore(self):
        pass