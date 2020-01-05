"""This is the module with the player class"""
import copy
import utility
from ship import CShip
from collection import Collection


class Player:
    fuel_cost = 1

    def __init__(self, name, skill_points, credit, curr_region):
        self.name = name
        self.pilot = skill_points[0]
        self.fighter = skill_points[1]
        self.merchant = skill_points[2]
        self.engineer = skill_points[3]
        self.credit = credit
        self.curr_region = curr_region
        self.ship = CShip()
        self.karma = 0
        self.collection = Collection()

    # END __init__

    @property
    def win(self):
        for item in self.ship.cargo:
            if item.id == 13:
                return True
        return False

    @property
    def lose(self):
        if self.ship.health_level == 0:
            return True
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
        cost = utility.repair_cost(repairs, self.engineer)
        if self.credit < cost:
            return "Not enough Money!"
        elif self.ship.health_level + repairs > self.ship.max_health:
            damage = self.ship.max_health - self.ship.health_level
            cost = utility.repair_cost(damage, self.engineer)
            self.credit -= cost
            self.ship.health_level = self.ship.max_health
            return "Success"
        else:
            self.credit -= cost
            self.ship.health_level += repairs
            return "Success"

    def purchase_fuel(self, fuel):
        cost = fuel * self.fuel_cost
        if self.credit < cost:
            return "Not enough cash"
        elif self.ship.fuel_level + fuel > self.ship.max_fuel:
            new_fuel = self.ship.max_fuel - self.ship.fuel_level
            cost = new_fuel * self.fuel_cost
            self.credit -= cost
            self.ship.fuel_level = self.ship.max_fuel
            return "Success"
        else:
            self.credit -= cost
            self.ship.refuel(fuel)
            return "Success"

    def trade_buy(self, item, amount):
        if item.amount < amount:
            return "Out of stock"
        elif self.ship.cargo_space < (item.size * amount):
            return "Not enough space!"
        elif self.credit < (item.b_price * amount):
            return "Not enough credits!"
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
            if not self.collection.check_item_in_set(bought):
                self.collection.add_and_update(bought)
            return "Success"

        # Index in cargo

    def trade_sell(self, cargo_item_index, amount):
        if self.ship.cargo[cargo_item_index].amount < amount:
            return "You dont have that many"
        elif self.ship.cargo[cargo_item_index].amount == amount:
            # player sells last one
            self.ship.cargo[cargo_item_index].amount -= amount
            self.credit += self.ship.cargo[cargo_item_index].s_price * amount
            self.ship.cargo.pop(cargo_item_index)
            return "Trade sucessful"
        else:
            # player has more of that item remaining
            self.credit += self.ship.cargo[cargo_item_index].s_price * amount
            self.ship.cargo[cargo_item_index].amount -= amount
            return "Trade sucessful"
