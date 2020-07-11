import pygame
import sys
import time
from states import menu, game

class Window:
    def __init__(self, width, height, name, fps):
        self.windowSize = width, height
        self.display = pygame.display.set_mode(self.windowSize)
        self.fps = fps
        
        #set the window name
        pygame.display.set_caption(name)

    def quit(self):
        pygame.quit()
        quit()
  
class GameController:
    def __init__(self, window):
        self.__dict__.update(settings)
        self.done = False
        self.screen = pygame.display.set_mode(self.size)
        self.clock = pygame.time.Clock()
    def setup_states(self, state_dict, start_state):
        self.state_dict = state_dict
        self.state_name = start_state
        self.state = self.state_dict[self.state_name]
    def flip_state(self):
        self.state.done = False
        previous,self.state_name = self.state_name, self.state.next
        self.state.cleanup()
        self.state = self.state_dict[self.state_name]
        self.state.startup()
        self.state.previous = previous
    def update(self):
        if self.state.quit:
            self.done = True
        elif self.state.done:
            self.flip_state()
        self.state.update(self.screen)
    def event_loop(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.done = True
            self.state.get_event(event)
    def main_game_loop(self):
        while not self.done:
            delta_time = self.clock.tick(self.fps)
            self.event_loop() #
            self.update()
            pygame.display.update() 

if __name__ == '__main__':
    # TODO: move settings dictionary to JSON file
    settings = {
        'size':(600,400),
        'fps' :60,
        'WindowTitle' : 'Trolls2'
    }

    window = Window(600, 400, 'Trolls2', 60)
    #Trolls2 = GameController(**settings)
    Trolls2 = GameController(window)

    # TODO: move state_dict dictionry to JSON file
    state_dict = {
        'menu': menu.Menu(),
        'game': game.Game()
    }
    Trolls2.setup_states(state_dict, 'menu')
    Trolls2.main_game_loop()
    pygame.quit()
    sys.exit()