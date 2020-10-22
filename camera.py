class camera:
    def __init__ (self, cameraFunction, width, height):
        self.cameraRect = (0, 0, width, height)

    # function for recalculating the position of an entity on the screen    
    def apply(self, target):
        target.rect = self.basicCamer(target.rect)

'''
        return target.rect.move(self.state.topleft)

    # function for a basic camera that displays and follows an object in the center of the screen
    def basicCamera(self, targetRect):
        targetRect
        #center the target rect
        x = -targetRect[0] + (self.cameraState[2] / 2)
        y = -targetRect[1] + (self.cameraState[3] / 2)

        #move the camera
        camera.topleft += (pygameVector2((x,y)) - pygame.Vector2(camera.topleft)) * 0.06 #0.06 adds smoothing to movement?

        #set max/min x/y so we don't see stuff outside teh world
        camera.x = max(-(camera.width-self.cameraState[2]), min(0, camera.x))
        camera.y = max(-(camera.height - self.cameraState[3]),min(0, camera.y))'''