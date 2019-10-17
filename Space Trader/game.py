import random
from universe import Universe
from player import Player
from ship import Ship, A_Ship, B_Ship, C_Ship


class Game:
    def __init__(self, diff):
        self.diff = diff
        self.names = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]
        self.universe = None
        self.player = None
        self.ship = None

    def start_game(self, name, skill_points, credit):
        self.universe = Universe()
        rand_int = random.randint(0, len(self.universe.region_list) - 1)
        self.player = Player(
            name, skill_points, credit, self.universe.region_list[rand_int]
        )
        self.ship = C_Ship()
    # END startGame

    def fuelCostConstant(self):
        if self.diff == "easy":
            fuelCost = 0.2
        if self.diff == "medium":
            fuelCost = 0.35
        if self.diff == "hard":
            fuelCost = 0.5
        return fuelCost
    
    def travelSequence(self, new_region):
        hasTraveled = False
        while not hasTraveled:
            distance = new_region.distance(new_region, self)
            fuelCost = self.fuelCostConstant() * distance
            fuelAmount = self.ship.get_fuel_capacity()
            if fuelCost <= fuelAmount:
                self.player.travel(new_region)
                self.ship.set_fuel_capacity(fuelAmount - fuelCost)
                hasTraveled = True
                #"Traveled to new region succesfully"
            else:
                hasTraveled = False
                break
                #"Insufficient fuel. Try again?
                #Cancel button? Add break
            #END if
        #END while