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
        self.clock = gameClock