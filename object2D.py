import physics2D
import animation

class Object2D:
    def __init__(self):
        self.active = True # active status determines if the object will be updated or will be deleted
        self.width = 0
        self.height = 0
        self.location = (0,0)
        self.rect = (self.location[0], self.location[1], self.width, self.height)
        self.physics = physics2D.physics()
        self.sprite = None
        print("Object Initialized...")

    def update(self, gameDisplay):
        pass

    def detectCollision(self):
        pass

    def detectActiveStatus(self):
        self.detectOffscreen()

    def detectOffscreen(self, display_width, display_height):
        pass
    
    def draw(self, gameDisplay):
        self.sprite.draw(gameDisplay, self.location[0], self.location[1])