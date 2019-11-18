"""This is the module with the player class"""
import copy
import utility
from ship import CShip


class Player:
    fuel_cost = 3
    def __init__(self, name, skill_points, credit, curr_region):
        self.name = name
        self.pilot = skill_points[0]
        self.fighter = skill_points[1]
        self.merchant = skill_points[2]
        self.engineer = skill_points[3]
        self.credit = credit
        self.curr_region = curr_region
        self.ship = CShip()

    # END __init__

    @property
    def win(self):
        for item in self.ship.cargo:
            if item.name == self.name + "'s Universe.":
                return True
        return False
    
    @property
    def lose(self):
        if self.ship.health_level == 0:
            return True
        else:
            return False
    

    @property
    def credit(self):
        return self._credit

    @credit.setter
    def credit(self, credit):
        if credit < 0:
            self._credit = 0
        else:
            self._credit = credit


    def buy_repairs(self, repairs):
        if self.credit < (utility.repair_cost(repairs, self.engineer)):
            return "Not enough Money!"
        elif self.ship.health_level + repairs > self.ship.max_health:
            return "You're buying more than you can use??"
        else:
            self.ship.health_level += repairs
            return "Success"


    def purchase_fuel(self, fuel):
        if self.credit < (fuel * self.fuel_cost):
            return "Not enough cash"
        else:
            self.ship.refuel(fuel)
            return "Success"

    def trade_buy(self, item, amount):
        if item.amount < amount:
            return "Out of stock"
        elif self.ship.cargo_space < (item.size * amount):
            return "Your ship does not have enough space"
        elif self.credit < (item.b_price * amount):
            return "Not enough cash"
        else:
            self.credit -= item.b_price * amount
            for cargo in self.ship.cargo:
                if cargo.name == item.name:
                    cargo.amount += amount
                    item.amount -= amount
                    return "Success"
            bought = copy.deepcopy(item)
            bought.amount = amount
            item.amount -= amount
            self.ship.cargo.append(bought)
            return "Success"

        # Index in cargo

    def trade_sell(self, cargo_item_index, amount):
        if self.ship.cargo[cargo_item_index].amount < amount:
            return "You dont have that many"
        elif self.ship.cargo[cargo_item_index].amount == amount:
            self.credit += self.ship.cargo[cargo_item_index].s_price * amount
            self.ship.cargo.pop(cargo_item_index)
            return "Trade sucessful"
        else:
            self.credit += self.ship.cargo[cargo_item_index].s_price * amount
            self.ship.cargo[cargo_item_index].amount -= amount
            return "Trade sucessful"