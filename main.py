import pygame
import sys
from states import menu, game, splash, transition, gameover

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
        self.gameDisplay = pygame.display.set_mode(self.size)
        self.display_width = self.size[0]
        self.display_height = self.size[1]
        self.screenSize = (self.display_width, self.display_height)
        self.gameClock = pygame.time.Clock()
        self.window = window

        # TODO: move state_dict dictionry to JSON file
        self.state_dict = {
            'transition': transition.Transition(self.gameDisplay, self.window),
            'menu': menu.Menu(self.gameDisplay, self.window),
            'game': game.Game(self.gameDisplay, self.window),
            'splash': splash.Splash(self.gameDisplay, self.window),
            'gameover': gameover.GameOver(self.gameDisplay, self.window),
        }

    def setup_states(self, start_state):
        self.state_name = start_state
        self.state = self.state_dict[self.state_name]

    def flip_state(self):
        self.state.done = False
        previous, self.previousState, self.state_name = self.state_name, self.state, self.state.next
        self.state.cleanup()
        self.state = self.state_dict[self.state_name]
        self.state.previous, self.state.previousState = previous, self.previousState
        self.state.startup()

    def update(self):
        if self.state.quit:
            self.done = True
        elif self.state.done:
            self.flip_state()
        #call the update method for the current active state
        self.state.update()

    def event_loop(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.done = True
            self.state.get_event(event)

    def main_game_loop(self):
        while not self.done:
            delta_time = self.gameClock.tick(self.window.fps)
            self.event_loop()
            self.update()
            pygame.display.update() 

if __name__ == '__main__':
    pygame.init()

    # TODO: move settings dictionary to JSON file
    settings = {
        'size':(800,600),
        'fps' :60,
        'WindowTitle' : 'Trolls2'
    }

    window = Window(800, 600, 'Trolls2', 60)
    Trolls2 = GameController(window)

    Trolls2.setup_states('splash')
    Trolls2.main_game_loop()
    pygame.quit()
    sys.exit()