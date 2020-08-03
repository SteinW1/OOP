import sys
import pygame
from gamestates import state

class Transition(state.State):
    def __init__(self, gameDisplay, window, gameClock):
        state.State.__init__(self, gameDisplay, window, gameClock)
        self.backgroundAlphaColor = 0

        #set the next states 'next' variables
        self.targetState = 'transition'

    def cleanup(self):
        #method for cleaning up state stuff
        print('Cleaning Up Transition State...')

    def startup(self):
        #method for starting state stuff
        print('Starting Up Transition State...')
        self.backgroundAlphaColor = 0

        #set the next state that was determined by previous state's target
        self.next = self.previousState.targetState

    def get_event(self, event):
        if event.type == pygame.KEYDOWN:
            print('Transition State keydown')
        elif event.type == pygame.MOUSEBUTTONDOWN:
            self.done = True
        
    def update(self):
        if self.backgroundAlphaColor >= 255:
            self.done = True
        else:
            self.backgroundAlphaColor += 5
        self.draw()

    def draw(self):
        self.previousState.draw()
        fade = pygame.Surface((self.window.windowSize[0], self.window.windowSize[1])) 
        fade.set_alpha(self.backgroundAlphaColor)
        fade.fill((0, 0, 0))
        self.gameDisplay.blit(fade, (0,0))