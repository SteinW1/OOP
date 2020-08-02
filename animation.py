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

        self.cellIndex = 0
        self.animationIndex = 0

    def setToIdle(self):
        self.framesInAnimation = 1
        self.frame = self.animationIndex

    def setAnimationIndex(self, index, framesInAnimation):
        self.animationIndex = index
        self.framesInAnimation = framesInAnimation

    def updateSpriteFrame(self, x, y, currentTime):
        # check if enough time has passed since the last sprite frame switch and switch if necessary
        if currentTime > self.timeUntilNextFrame:
            self.frame = (self.frame + 1) % self.framesInAnimation
            self.timeUntilNextFrame += 1000/self.framesInAnimation

        # get the index of the sprite frame that will be displayed
        self.cellIndex = (self.frame + self.animationIndex) % self.totalCellCount

        # print statement for debugging
        print("Frame: ", self.frame, " TotalCellCount: ", self.totalCellCount, " CellIndex: ", self.cellIndex)

    def draw(self, surface, x, y):
        surface.blit(self.sheet, (x + self.location[0], y + self.location[1]), self.cells[self.cellIndex])