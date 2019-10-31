from ship import Ship, AShip, BShip, CShip
import random
class NPC:
    def __init__(self, name, demand, pilot, fighter):
        self.name = name
        self.demand = demand
        self.pilot = pilot
        self.fighter = fighter

class Bandit(NPC):
    def __init__(self):
        #Bandit doesn't need a ship, they don't need to have inventory or fuel
        rand = random.randint(1,3)
        if (rand == 1):
            self.name = "Lil Peep"
            self.demand = random.randint(10, 20)
            self.pilot = random.randint(1, 3)
            self.fighter = random.randint(1, 3)
        elif (rand == 2):
            self.name = "Chicky G"
            self.demand = random.randint(20, 30)
            self.pilot = random.randint(2, 4)
            self.fighter = random.randint(2, 4)
        else:
            self.name = "Cluck Boss"
            self.demand = random.randint(30, 40)
            self.pilot = random.randint(3, 5)
            self.fighter = random.randint(3, 5)
        
    


        


        
        


    