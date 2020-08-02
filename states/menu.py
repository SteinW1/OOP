import sys
import pygame
import ui
from states import state

colors = {'black': (0, 0, 0, 255),
    'white': (255, 255, 255, 255),
    'light_blue': (53, 115, 255, 255),
    'red' : (200, 0, 0, 255),
    'green' : (0, 200, 0, 255),
    'bright_red' : (255, 0, 0, 255),
    'bright_green' : (0, 255, 0, 255),
    'sky_blue' : (184, 251, 255, 255)}

class Menu(state.State):
    def __init__(self, gameDisplay, window, gameClock):
        state.State.__init__(self, gameDisplay, window, gameClock)
        self.Title = None
        self.StartButton = ui.button(150, 450, 100, 50, colors['bright_green'], colors['green'], colors['black'], "comicsansms", 20, "Start")
        self.ExitButton = ui.button(550, 450, 100, 50, colors['bright_red'], colors['red'], colors['black'], "comicsansms", 20, "Exit")

        self.titleBackground = pygame.image.load('images/TitleBackground.png')
        self.titleBackground_width = 500
        self.titleBackground_height = 300

        #set the next states 'next' variables
        self.targetState = 'game'

    def cleanup(self):
        #method for cleaning up Menu state stuff
        print('Cleaning Up Menu State... \n    - Done.')
        self.isActive = False

    def startup(self):
        #method for starting Menu state stuff
        print('Starting Up Menu State...')
        
        #set the next state, defaults to the transition state
        self.next = self.previousState.targetState

    def get_event(self, event):
        if event.type == pygame.KEYDOWN:
            print('Menu State keydown')
        
    def update(self):
        self.Title = ui.textBox((self.window.windowSize[0]/2), (self.window.windowSize[1]/3), 'Trolls2', 'comicsansms', 115, 'center', self.gameDisplay)
        
        self.draw()
        
        # run the button idle loop and check if the button has been clicked
        if self.StartButton.idle(self.gameDisplay) == True:
            self.done = True
        if self.ExitButton.idle(self.gameDisplay) == True:
            pygame.quit()
            sys.exit()

    def draw(self):
        self.gameDisplay.fill(colors['white'])
        self.StartButton.drawButton(self.gameDisplay)
        self.ExitButton.drawButton(self.gameDisplay)
        self.gameDisplay.blit(self.titleBackground, ((self.window.windowSize[0]/2) - self.titleBackground_width/2, (self.window.windowSize[1]/3) - self.titleBackground_height/2))
        self.Title.drawTextBox(self.gameDisplay)
    