import pygame
import math

#class for basic 2D movement and collisions
class physics:
    def __init__(self):
        pass

    #gets the position difference between objects. the objects must have (location = x,y) attribute for the method to work
    def getVector(self, position1, position2):
        vector = (position2[0] - position1[0], position2[1] - position1[1])
        return vector

    #get the hypotenuse of the movement vector to determine the vector length
    def getVectorLength(self, vector):
        VectorLength = math.sqrt(vector[0]**2 + vector[1]**2)
        return VectorLength

    #function for finding unit vector when given a vector and the vector's length
    def getUnitVector(self, vector, vectorLength):
        if vectorLength != 0:
            unitVector = (vector[0]/vectorLength, vector[1]/vectorLength)
        else:
            unitVector = 0,0
        return unitVector    
    
    #returns the unit vector of two positions
    def getMovement(self, position1, position2):
        print(position1, position2)
        vector = self.getVector(position1, position2)
        vectorLength = self.getVectorLength(vector)
        return self.getUnitVector(vector, vectorLength)
    
    #detect collision between two rectangular objects
    def detectCollision(self, rectangle1, rectangle2):
        pass