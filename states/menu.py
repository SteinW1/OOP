import pygame
from Trolls2 import ui
from states import state

class Menu(state.State):
    def __init__(self):
        state.State.__init__(self)

        StartButton = button.button(150, 450, 100, 50, colors['bright_green'], colors['green'], colors['black'], "comicsansms", 20, game_loop, "Start!")
        ExitButton = button.button(550, 450, 100, 50, colors['bright_red'], colors['red'], colors['black'], "comicsansms", 20, quitGame, "Exit")

        self.next = 'game'
    def cleanup(self):
        print('cleaning up Menu state stuff')
    def startup(self):
        print('starting Menu state stuff')
    def get_event(self, event):
        if event.type == pygame.KEYDOWN:
            print('Menu State keydown')
        elif event.type == pygame.MOUSEBUTTONDOWN:
            self.done = True
    def update(self, screen, dt):






        self.draw(screen)
    def draw(self, screen):
        screen.fill((255,0,0))