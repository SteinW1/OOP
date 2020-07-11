import pygame

'''
This file was made to contain UI objects such as text boxes, buttons, chat boxes, etc.
'''

class button:
    def __init__(self, x, y, w, h, activeColor, inactiveColor, textColor, font, fontSize, action=None, msg=None):
        self.x = x
        self.y = y
        self.width = w
        self.height = h
        self.message = msg
        self.activeColor = activeColor
        self.inactiveColor = inactiveColor
        self.action = action
        self.messageText = pygame.font.SysFont(font, fontSize)
        self.textColor = textColor

    def idle(self, gameDisplay):
        self.detectButtonActivity(gameDisplay)
        self.drawButton(gameDisplay)

    def detectButtonActivity(self, gameDisplay):
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        if self.x + self.width > mouse[0] > self.x and self.y + self.height > mouse[1] > self.y:
            pygame.draw.rect(gameDisplay, self.activeColor, (self.x, self.y, self.width, self.height))
            if click[0] == 1 and self.action != None:
                self.action()
        else:
            pygame.draw.rect(gameDisplay, self.inactiveColor, (self.x, self.y, self.width, self.height))
        
    def drawButton(self, gameDisplay):
        textSurf = self.messageText.render(self.message, True, self.textColor)
        textRect =textSurf.get_rect()
        textRect.center = ((self.x + (self.width / 2)), (self.y + (self.height / 2)))
        gameDisplay.blit(textSurf, textRect)

class textBox:
    def __init__(self, x, y, text, font, fontSize, gameDisplay):
        self.location = (x,y)
        #self.textSize
        #self.font = font
        self.fontObject = pygame.font.SysFont(font, fontSize) #object with a font and a font size
        #self.textSize
        #self.surface = self.fontObject.render()
        largeText.render(text, True, colors['black'])
        #self.serfaceRectangle
    
    #update the textbox for the frame
    def updateTextBox(self, gameDisplay):
        self.drawTextBox(gameDisplay)

    #draw the textbox onto the canvas
    def drawTextBox(self, gameDisplay):
        gameDisplay.blit(self.surface, (self.location))