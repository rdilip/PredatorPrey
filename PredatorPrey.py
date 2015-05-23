# coding: utf-8
import random
class Animal(object):
    def __init__(self, xpos, ypos):
        """ Defines an object of type Animal. 

        Both Predator and Prey inherit from Animal. 
        keyword arguments:
            xpos -- initial x position
            ypos -- intial y position
        """
        self.xpos = xpos
        self.ypos = ypos
        self.lifetime = 0
    
    def __str__(self):
        """Print format for an Animal based on position and lifetime"""
        return("(%d, %d) and lifetime %d" % (self.xpos, self.ypos,			self.lifetime))

    def walk(self, hbound, vbound):
        """ Random walk method

        Walk randomly within horizontal and vertical bounds.
        If an Animal Object is at a bound, it moves in the reverse
        of that bound's direction, back towards the center of the map.
        """
        xtemp = self.xpos
        ytemp = self.ypos
        curLife = self.lifetime

        walkDir = int(random.random() * 4) + 1

        if (xtemp == abs(hbound)):
            xtemp -= 1 * int(hbound / abs(hbound))
        if (ytemp == abs(vbound)):
            ytemp -= 1 * int(vbound / abs(vbound))

        elif (walkDir == 1):
            xtemp += 1
        elif (walkDir == 2):
            xtemp -= 1
        elif (walkDir == 3):
            ytemp += 1
        elif (walkDir == 4):
            ytemp -= 1

        self.xpos = xtemp
        self.ypos = ytemp
        
        curLife += 1
        self.lifetime = curLife
    
    def reset(self):
        """ Resets the Animal's lifetime to 0 """
        self.lifetime = 0
    
class Prey(Animal):
    def __init__(self, xpos, ypos):
        super(Prey, self).__init__(xpos, ypos)

    def __str__(self):
        return(super(Prey, self).__str__())

    def walk(self, hbound, vbound):
        super(Prey, self).walk(hbound, vbound)
    
    def breed(self, hbound, vbound):
        """ Breeds the Animal to a random open square. Uses the             same algorithm as the random walk method.
        """
        xtemp = self.xpos
        ytemp = self.ypos
        curLife = self.lifetime

        breedDir = int(random.random() * 4) + 1

        if (xtemp == abs(hbound)):
            xtemp -= 1 * int(hbound / abs(hbound))
        if (ytemp == abs(vbound)):
            ytemp -= 1 * int(vbound / abs(vbound))

        elif (breedDir == 1):
            xtemp += 1
        elif (breedDir == 2):
            xtemp -= 1
        elif (breedDir == 3):
            ytemp += 1
        elif (breedDir == 4):
            ytemp -= 1

        return(Prey(xtemp, ytemp))

class Predator(Animal):
    def __init__(self, xpos, ypos):
		self.food = 0
		super(Predator, self).__init__(xpos, ypos)

    def __str__(self):
        return(super(Predator, self).__str__())

    def walk(self, hbound, vbound):
		food = self.food;
		food += 1
		self.food = food
		super(Predator, self).walk(hbound, vbound)
    def foodReset(self):
        self.food = 0	    
    def breed(self, hbound, vbound):
        """ Breeds the Animal to a random open square. Uses the			same algorithm as the random walk method.
        """
        xtemp = self.xpos
        ytemp = self.ypos
        curLife = self.lifetime

        breedDir = int(random.random() * 4) + 1

        if (xtemp == abs(hbound)):
            xtemp -= 1 * int(hbound / abs(hbound))
        if (ytemp == abs(vbound)):
            ytemp -= 1 * int(vbound / abs(vbound))

        elif (breedDir == 1):
            xtemp += 1
        elif (breedDir == 2):
            xtemp -= 1
        elif (breedDir == 3):
            ytemp += 1
        elif (breedDir == 4):
            ytemp -= 1

        return(Predator(xtemp, ytemp))

if __name__ == '__main__':
	pass
