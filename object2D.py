import math

class CharacterObject:
    def __init__(self):
        self.width = 0
        self.height = 0
        self.location = (0,0)
        self.rect = (self.location[0], self.location[1], self.width, self.height)
        self.physics = physics2D.physics()