import sys
#sys.path.insert(0,'..')

import pygame
import ui
from states import state

class Game(state.State):
    def __init__(self):
        state.State.__init__(self)
        self.next = 'menu'

    def cleanup(self):
        #method for cleaning up Game state stuff
        pass

    def startup(self):
        #method for starting Game state stuff
        pass

    def get_event(self, event):
        if event.type == pygame.KEYDOWN:
            print('Game State keydown')
        elif event.type == pygame.MOUSEBUTTONDOWN:
            self.done = True

    def update(self, gameDisplay, display_width, display_height):
        self.draw(gameDisplay)

    def draw(self, gameDisplay):
        gameDisplay.fill((0,0,255))