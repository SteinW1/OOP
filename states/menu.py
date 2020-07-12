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
    def __init__(self):
        state.State.__init__(self)
        self.Title = None
        self.StartButton = ui.button(150, 450, 100, 50, colors['bright_green'], colors['green'], colors['black'], "comicsansms", 20, self.update, "Start!")
        self.ExitButton = ui.button(550, 450, 100, 50, colors['bright_red'], colors['red'], colors['black'], "comicsansms", 20, pygame.quit, "Exit")
        self.next = 'game'
        self.isActive = True
        self.startup()

    def cleanup(self):
        #method for cleaning up Menu state stuff
        print('cleaning up menu')
        self.isActive = False

    def startup(self):
        #method for starting Menu state stuff
        print('starting up menu')
        self.isActive = True

    def get_event(self, event):
        if event.type == pygame.KEYDOWN:
            print('Menu State keydown')
        
    def update(self, gameDisplay, display_width, display_height):
        self.Title = ui.textBox((display_width/2), (display_height/3), 'Trolls2', 'comicsansms', 115, 'center', gameDisplay)
        
        self.draw(gameDisplay)
        
        # run the button idle loop and check if the button has been clicked
        if self.isActive == True:
            if self.StartButton.idle(gameDisplay) == True:
                self.done = True
            if self.ExitButton.idle(gameDisplay) == True:
                pygame.quit()
                sys.exit()

    def draw(self, gameDisplay):
        gameDisplay.fill(colors['white'])
        self.StartButton.drawButton(gameDisplay)
        self.ExitButton.drawButton(gameDisplay)
        self.Title.drawTextBox(gameDisplay)