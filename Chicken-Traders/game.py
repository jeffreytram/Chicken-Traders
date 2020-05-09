import random
import utility
from universe import Universe
from player import Player

class Game:
    def __init__(self, diff):
        self.diff = diff
        self.universe = None
        self.player = None
        self.time = 0
        self.day = 0
        self.news = []
        self.net_worth_data = []

    def start_game(self, name, skill_points, credit):
        self.universe = Universe()
        rand_int = random.randint(0, len(self.universe.region_list) - 1)
        self.player = Player(
            name, skill_points, credit, self.universe.region_list[rand_int]
        )
        self.net_worth_data.append(self.player.credit)
        self.universe.insert_win(self.player.name)
        utility.bprice_calc(self.player, self.player.curr_region)
        utility.sprice_calc(self.player, self.player.curr_region)

    # increases time
    def increment_time(self):
        self.time += 2
        if self.time % 6 == 0:
            # calculate net worth every 6 hr
            net_worth = self.calcNetWorth()
            self.net_worth_data.append(net_worth)
        if self.time >= 24:
            self.time = self.time % 24
            self.day += 1
            self.restock(self.universe.region_list)
    
    # replenishes stock of every item by 1
    def restock(self, region_list):
        for region in region_list:
            for item in region.market:
                if item.amount < item.max:
                    item.amount += 1

    def calcNetWorth(self):
        # net worth is number of credits plus base price of items
        net_worth = self.player.credit
        for item in self.player.ship.cargo:
            net_worth += item.amount * item.base_price
        return int(net_worth)

    @property
    def fuel_cost_constant(self):
        if self.diff == "easy":
            return 0.2
        elif self.diff == "med":
            return 0.3
        elif self.diff == "hard":
            return 0.4
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
