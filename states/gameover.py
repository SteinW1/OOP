import sys
import time
import pygame
import ui
from states import state

class GameOver(state.State):
    def __init__(self, gameDisplay, window, gameClock):
        state.State.__init__(self, gameDisplay, window, gameClock)
        self.next = 'transition'
        self.targetState = 'menu'
        self.counter = 0

        self.gameOverText = ui.textBox((window.windowSize[0]/2), (window.windowSize[1]/3), 'Game Over', 'comicsansms', 115, 'center', self.gameDisplay)
        self.timer = pygame.time.Clock()

    def cleanup(self):
        #method for cleaning up Menu state stuff
        print('Cleaning Up Splash State...')

    def startup(self):
        #method for starting Menu state stuff
        print('Starting Up Splash State...')

    def get_event(self, event):
        if event.type == pygame.KEYDOWN:
            print('Splash State keydown')
        elif event.type == pygame.MOUSEBUTTONDOWN:
            self.done = True
        
    def update(self):
        
        if self.counter < 60:
            self.counter += 1
            self.timer.tick(self.window.fps/2)
        else:
            self.done = True

        self.draw()
        #time.sleep(2)

    def draw(self):
        self.previousState.draw()
        self.gameOverText.drawTextBox(self.gameDisplay)