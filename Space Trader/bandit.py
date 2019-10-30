from ship import Ship, AShip, BShip, CShip
import random
class Bandit:
    def __init__(self, name, demand, pilot, fighter):
        #Bandit doesn't need a ship, they don't need to have inventory or fuel
        rand = random.randint(1,3)
        if (rand == 1):
            self.name = "Lil Peep"
        elif (rand == 2):
            self.name = "Chicky G"
        else:
            self.name = "Cluck Boss"
        self.demand = random.randint(15, 40)
        self.pilot = random.randint(1, 5)
        self.fighter = random.randint(1, 5)


        


        
        


    