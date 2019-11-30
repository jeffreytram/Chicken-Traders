import random
import utility
from universe import Universe
from player import Player

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
        self.universe.insert_win(self.player.name)
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
    def encounter_factor(self):
        if self.diff == "easy":
            return 1
        elif self.diff == "med":
            return 1.5
        elif self.diff == "hard":
            return 2
        else:
            return -1
