# coding: utf-8
from PredatorPrey import Predator
from PredatorPrey import Prey
import random
import time
import sys

def mulDel(list_, args):
    args = sorted(args, reverse=True)
    for i in args:
        del list_[i]
    return list_

def search(prey, x, y):
	remove = []
	x = 0
	for i in xrange(0, len(prey)):
		if prey[i].xpos == x and prey[i].ypos == y:
			remove.append(i)

	for i in xrange(0, len(remove)):
		prey.pop(remove[i])

	if (len(remove) == 0):
		return 0
	return 1


def sim(width, height, numPredators, numPrey):
	prey = []
	predators = []
	xpos = 1
	ypos = 1
	for i in xrange(0, numPrey):
		xpos = random.randint(-width/2, width/2)
		ypos = random.randint(-height/2, height/2)
		prey.append(Prey(xpos, ypos))
				
	for i in xrange(0, numPredators):
		xpos = random.randint(-width/2, width/2)
		ypos = random.randint(-height/2, height/2)
		predators.append(Predator(xpos, ypos))
				
	while True:
		time.sleep(1)
		removePredators = []
		removePrey = []

		for i in xrange(0, len(predators)):
			predators[i].walk(width/2, height/2)
			eat = search(prey, predators[i].xpos, predators[i].ypos)
			if (eat == 1):
				predators[i].foodReset()
			if(predators[i].food == 3):
				removePredators.append(i)
				continue
			if (predators[i].lifetime == 8):
				xpos = random.randint(-width/2, width/2)
				ypos = random.randint(-height/2, height/2)
				predators.append(Predator(xpos, ypos))

		mulDel(predators, removePredators)
		removePredators = []

		for i in xrange(0, len(prey)): 
			prey[i].walk(width/2, height/2)
			xpos = random.randint(-width/2, width/2)
			ypos = random.randint(-height/2, height/2)
			if (prey[i].lifetime == 3):
				prey.append(Prey(xpos, ypos))

		print("Predators: %d\tPrey: %d" % (len(predators), len(prey)))
	return 0

def main():
	width = int(sys.argv[1])
	height = int(sys.argv[2])
	numPredators = int(sys.argv[3])
	numPrey = int(sys.argv[4])

	sim(width, height, numPredators, numPrey)

if __name__ == '__main__':
	main()

