import random
import utility
from universe import Universe
from player import Player
from npc import Bandit, Trader

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
                utility.damage(self.player, bandit)
    
    def fleeBandit(self, bandit):
        if (self.player.pilot >= bandit.pilot):
            #travel back, lose fuel
            #WILL ADD AFTER RAND ENCOUNTER IMPLEMENTATION
            self.player.ship.fuel_level = -1 #temporary
        else:
            #lose all credits
            self.player.credit = 0
            #get damaged
            utility.damage(self.player, bandit)

    def fightBandit(self, bandit):
        if (self.player.fighter >= bandit.fighter):
            #continue to travel ADD AFTER RAND ENCOUNTER
            #get money (based off the bandit's demand, is less for higher difficulty)
            self.player.credits = self.player.credits + (100 - bandit.demand)
        else:
            self.player.credit = 0
            #get damaged
            utility.damage(self.player, bandit)