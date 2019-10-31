import random
import utility
from ship import Ship, AShip, BShip, CShip
from item import Item
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
        self.itemList = self.selectItems()
    
    def selectItems(self):
        #gives the trader 3 random items, not determined 
        #by tech level b/c this happens while traveling
        list = []
        items = Item.__subclasses__()
        while (len(list) < 3):
            rand = random.randint(0, len(items) - 1)
            list.append(item[rand](rand.rantint(1, 3)))
            items.pop(rand)
        #END while
        return list
