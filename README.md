# PredatorPrey
Simulation of PredatorPrey problem in Python

The PredatorPrey.py file contains three classes -- Animal, Preadtor, and Prey. The last two both inherit several methods and properties from Animal. This program uses a random walk method within certain bounds for both the Predators and the Prey. 

## Prey
* Move. Every time step, randomly try to move up, down, left, or right. If the cell in the selected direction is occupied or would move the ant off the grid, then the ant stays in the current cell.

* Breed. If a prey esurvives for three time steps, then at the end of the third time step (i.e., after moving), the ant will breed. This adds another prey at a random nearby cell. 

## Predators
*  Move. The predators follow the same random walk motion as the ants. Note that there is currently no intelligence in the predators movement. To be fixed in the next version.
*  Breed. If a predator  survives for eight time steps, then at the end of the time step, it will spawn off a new doodlebug in the same manner as the prey.

* Starve. If a predator has not eaten an ant within the last three time steps, then at the end of the third time step, it will starve and die. 

