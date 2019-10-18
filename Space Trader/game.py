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

    def start_game(self, name, skill_points, credit):
        self.universe = Universe()
        rand_int = random.randint(0, len(self.universe.region_list) - 1)
        self.player = Player(
            name, skill_points, credit, self.universe.region_list[rand_int]
        )
    # END startGame

    @property
    def fuel_cost_constant(self):
        if self.diff == "easy":
            return 0.2
        elif self.diff == "medium":
            return 0.35
        elif self.diff == "hard":
            return 0.5
        else:
            return -1

    def travelSequence(self, new_region):
        traveled = False
        distance = self.player.curr_region.distance(new_region)
        fuel_cost = self.fuel_cost_constant * distance * (1 - (self.player.pilot/75))
        fuel_amount = self.player.ship.fuel_level
        if fuel_cost <= fuel_amount:
            self.player.curr_region = new_region
            self.player.ship.fuel_level = int(fuel_amount - fuel_cost)
            traveled = True
            return traveled
            #"Traveled to new region succesfully"
        return hasTraveled
        #END if