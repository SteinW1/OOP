import pygame

class State:
    def __init__(self):
        self.done = False
        self.next = None
        self.quit = False
        self.previous = None

'''class Menu(State):
    def __init__(self):
        State.__init__(self)
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

class Game(State):
    def __init__(self):
        State.__init__(self)
        self.next = 'menu'
    def cleanup(self):
        print('cleaning up Game state stuff')
    def startup(self):
        print('starting Game state stuff')
    def get_event(self, event):
        if event.type == pygame.KEYDOWN:
            print('Game State keydown')
        elif event.type == pygame.MOUSEBUTTONDOWN:
            self.done = True
    def update(self, screen, dt):
        self.draw(screen)
    def draw(self, screen):
        screen.fill((0,0,255))'''