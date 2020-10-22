import math
import physics2D

class Object2D:
    def __init__(self):
        self.width = 0
        self.height = 0
        self.location = (0,0)
        self.rect = (self.location[0], self.location[1], self.width, self.height)
        self.physics = physics2D.physics()
        print("object initialized")

    def draw(self, gameDisplay):
        gameDisplay.blit(self.img, (round(self.location[0]), round(self.location[1])))