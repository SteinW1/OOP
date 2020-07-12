import pygame

'''
This file was made to contain UI objects such as text boxes, buttons, chat boxes, etc.
'''

colors = {'black': (0, 0, 0, 255),
    'white': (255, 255, 255, 255),
    'light_blue': (53, 115, 255, 255),
    'red' : (200, 0, 0, 255),
    'green' : (0, 200, 0, 255),
    'bright_red' : (255, 0, 0, 255),
    'bright_green' : (0, 255, 0, 255),
    'sky_blue' : (184, 251, 255, 255)}

class button:
    def __init__(self, x, y, w, h, activeColor, inactiveColor, textColor, font, fontSize, msg=None):
        self.x = x
        self.y = y
        self.width = w
        self.height = h
        self.message = msg
        self.activeColor = activeColor
        self.inactiveColor = inactiveColor
        self.font = font
        self.fontSize = fontSize
        self.messageText = pygame.font.SysFont(font, fontSize)
        self.textColor = textColor

    def idle(self, gameDisplay):

        #returns True if the button activity is a button click
        if self.detectButtonActivity(gameDisplay) == True:
            return True
        self.drawButton(gameDisplay)
        

    def detectButtonActivity(self, gameDisplay):
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        if self.x + self.width > mouse[0] > self.x and self.y + self.height > mouse[1] > self.y:
            pygame.draw.rect(gameDisplay, self.activeColor, (self.x, self.y, self.width, self.height))
            if click[0] == 1:
                return True
        else:
            pygame.draw.rect(gameDisplay, self.inactiveColor, (self.x, self.y, self.width, self.height))
    
    #draw the button object to the display
    def drawButton(self, gameDisplay):
        buttonText = textBox((self.x + (self.width/2)), (self.y + (self.height/2)), self.message, self.font, self.fontSize, 'center', gameDisplay)
        gameDisplay.blit(buttonText.textBoxSurface, buttonText.textBoxRect)

class textBox:
    # initializes with given inputs, alignment argument must be in list [left, center, right]
    def __init__(self, x, y, text, font, fontSize, alignment, gameDisplay):
        self.location = (x,y)
        self.fontObject = pygame.font.SysFont(font, fontSize) #object with a font and a font size
        self.textBoxSurface = self.fontObject.render(text, True, colors['black'])
        self.textBoxRect = self.textBoxSurface.get_rect()
        self.alignment = alignment

        #check for the requested text alignment
        if self.alignment.upper() == 'LEFT':
            self.textBoxRect.midright = x, y
        elif self.alignment.upper() == 'CENTER':
            self.textBoxRect.center = (x, y)
        elif self.alignment.upper() == 'RIGHT':
            self.textBoxRect.midleft = x, y
    
    #update the textbox for the frame
    def updateTextBox(self, gameDisplay):
        self.drawTextBox(gameDisplay)

    #draw the textbox onto the canvas
    def drawTextBox(self, gameDisplay):
        gameDisplay.blit(self.textBoxSurface, self.textBoxRect)