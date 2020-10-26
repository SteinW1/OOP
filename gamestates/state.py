import pygame

class State:
    def __init__(self, gameDisplay, window, gameClock):
        self.done = False
        self.next = None
        self.quit = False
        self.previous = None
        self.previousState = None
        self.gameDisplay = gameDisplay
        self.window = window
        self.display_width = self.window.windowSize[0]
        self.display_height = self.window.windowSize[1]
        self.clock = gameClock
'''
    def cleanup(self):
        #method for cleaning up Splash state stuff
        print('Cleaning Up %s State...' % self.name)

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
        self.gameDisplay.blit(self.logo, ((self.window.windowSize[0]/2) - self.logoWidth/2, (self.window.windowSize[1])- self.logoHeight/2))'''