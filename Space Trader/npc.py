import random
import utility
from ship import Ship, AShip, BShip, CShip
from item import Item, Computer, StrangeTalisman, Banana, Apple, Gun, BiggerGun, FartInAJar, Friendship, PocketRussia, InvincibilityStar, AlienChicken, AssortedAlienAnimalFurs
from universe import Universe, Region
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

class Trader(NPC):
    def __init__(self):
        self.name = "Trader Joe"
        self.fighter = random.randint(0, 3)
        self.merchant = random.randint(1, 5)
        self.itemList = self.selectItems([])
    
    def selectItems(self, list):
        #gives the trader 3 random items, not determined by tech level b/c this happens while traveling
        while (len(list) < 3):
            rand = random.randint(1, 12)
            if (rand == 1):
                item = Computer(1)
            elif (rand == 2):
                item = StrangeTalisman(1)
            elif (rand == 3):
                item = Banana(1)
            elif (rand == 4):
                item = Apple(1)
            elif (rand == 5):
                item = Gun(1)
            elif (rand == 6):
                item = BiggerGun(1)
            elif (rand == 7):
                item = FartInAJar(1)
            elif (rand == 8):
                item = Friendship(1)
            elif (rand == 9):
                item = PocketRussia(1)
            elif (rand == 10):
                item = InvincibilityStar(1)
            elif (rand == 11):
                item = AlienChicken(1)
            else:
                item = AssortedAlienAnimalFurs(1)
            #END if
            list.append(item)
        #END while
        return list

    
        
        





        
    


        


        
        


    