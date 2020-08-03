import sys
import time
import pygame
import ui
from gamestates import state

class Splash(state.State):
    def __init__(self, gameDisplay, window, gameClock):
        state.State.__init__(self, gameDisplay, window, gameClock)
        self.next = 'transition'
        self.targetState = 'menu'
        self.counter = 0
        
        #initialize logo image
        self.logo = pygame.image.load('images/trollMain.png') #TODO: Add splash screen logos
        self.logoHeight = 90
        self.logoWidth = 232

    def cleanup(self):
        #method for cleaning up Splash state stuff
        print('Cleaning Up Splash State...')

    def startup(self):
        #method for starting Splash state stuff
        print('Starting Up Splash State...')

    def get_event(self, event):
        if event.type == pygame.KEYDOWN:
            print('Splash State keydown')
        elif event.type == pygame.MOUSEBUTTONDOWN:
            self.done = True
        
    def update(self):

        if self.counter < 60:
            self.counter += 1
        else:
            self.done = True

        self.draw()
        sleepTime = 1/60
        time.sleep(sleepTime)

    def draw(self):
        self.gameDisplay.fill((255, 255, 255, 255))
        self.gameDisplay.blit(self.logo, ((self.window.windowSize[0]/2) - self.logoWidth/2, (self.window.windowSize[1])- self.logoHeight/2))