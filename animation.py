import math, random, sys
import pygame

class animator:
    def __init__(self, filename, columns, rows):
        self.sheet = pygame.image.load(filename).convert_alpha()
        self.columns = columns
        self.rows = rows
        self.totalCellCount = columns * rows
        self.rect = self.sheet.get_rect()
        self.cellWidth = self.rect.width / columns
        self.cellHeight = self.rect.height / rows
        self.location = (0,0)
        self.frame = 0

        # generate a list of all sprites in the spritesheet
        self.cells = []
        for row in range(rows):
            for column in range(columns):
                self.cells.append([column % columns * self.cellWidth, row % rows * self.cellHeight, self.cellWidth, self.cellHeight])

        # initialize the time to draw the next frame
        self.timeUntilNextFrame = 0.0

        # set index for cell to draw on startup/creation
        self.cellIndex = 0
        self.animationIndex = 0

    # function for moving through the frames of an animation
    def animate(self):
        self.update()
        if self.switchFrame == True:
            self.frame = (self.frame + 1) % self.framesInAnimation
        self.cellIndex = (self.frame + self.animationIndex) % self.totalCellCount

    # function for drawing one consistent sprite image through multiple frames
    def idle(self):
        self.frame = 0
        self.cellIndex = self.animationIndex
        self.update()

    # function for changing the animation that will be used. For example, it will be used when a player changes character direction.
    def setAnimationIndex(self, index, framesInAnimation):
        self.animationIndex = index
        self.framesInAnimation = framesInAnimation

    # update function must be called every frame in order to maintain the consistency of frame drawing
    def update(self):
        # check if enough time has passed since the last sprite frame switch and switch if necessary
        if pygame.time.get_ticks() > self.timeUntilNextFrame:
            self.switchFrame = True
            self.timeUntilNextFrame += 1000/self.framesInAnimation
        else:
            self.switchFrame = False

    def draw(self, surface, x, y):
        surface.blit(self.sheet, (x + self.location[0], y + self.location[1]), self.cells[self.cellIndex])