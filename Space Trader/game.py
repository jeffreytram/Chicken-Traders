import random
import utility
from universe import Universe
from player import Player
from bandit import Rascal, Thug, Mafia



class Game:
    def __init__(self, diff):
        self.diff = diff
        self.universe = None
        self.player = None

    def start_game(self, name, skill_points, credit):
        self.universe = Universe()
        rand_int = random.randint(0, len(self.universe.region_list) - 1)
        self.player = Player(
            name, skill_points, credit, self.universe.region_list[rand_int]
        )
        utility.bprice_calc(self.player, self.player.curr_region)
        utility.sprice_calc(self.player, self.player.curr_region)
    # END startGame

    @property
    def fuel_cost_constant(self):
        if self.diff == "easy":
            return 0.2
        elif self.diff == "med":
            return 0.35
        elif self.diff == "hard":
            return 0.5
        else:
            return -1

    @property
    def enounter_factor(self):
        if self.diff == "easy":
            return 1
        elif self.diff == "med":
            return 1.5
        elif self.diff == "hard":
            return 2
        else:
            return -1

    #so it still works in the meantime
    def travel_sequence(self, new_region):
        if utility.travel_check(self, new_region):
            utility.travel(self.player, new_region)
            return True
            #"Traveled to new region succesfully"
        return False

    """Bandit NPC methods"""
    def payBandit(self, bandit):
        #Try to pay bandit's demand (determined in constructor)
        if (self.player.credits >= bandit.demand):
            #successful payment
            self.player.credits = self.player.credits - bandit.demand
        else:
            if (self.player.ship.cargo.size != 0):
                #give up all inventory. Doesn't have to transfer to the bandit
                self.player.ship.cargo = []
            else:
                #Get damaged
                damage = bandit.fighterLevel * 100
                if (self.player.ship.health_level >= damage):
                    self.player.ship.health_level = self.player.ship.health_level - damage
                else:
                    self.player.ship.health_level = 0
