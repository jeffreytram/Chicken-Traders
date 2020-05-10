"""This is the module with the player class"""
import copy
import utility
from ship import CShip
from collection import Collection
from transaction import Transaction


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
        self.transaction_history = []

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
        elif self.ship.health_level == self.ship.max_health:
            return "Already fully repaired!"
        elif self.ship.health_level + repairs > self.ship.max_health:
            damage = self.ship.max_health - self.ship.health_level
            cost = utility.repair_cost(damage, self.engineer)
            self.credit -= cost
            self.ship.health_level = self.ship.max_health
            self.transaction_history.append(Transaction("repairs", cost, "repairs", "expenses"))
            return "Success"
        else:
            self.credit -= cost
            self.ship.health_level += repairs
            self.transaction_history.append(Transaction("repairs", cost, "repairs", "expenses"))
            return "Success"

    def purchase_fuel(self, fuel):
        cost = fuel * self.fuel_cost
        if self.credit < cost:
            return "Not enough cash"
        elif self.ship.fuel_level == self.ship.max_fuel:
            return "Already fully fueled!"
        elif self.ship.fuel_level + fuel > self.ship.max_fuel:
            new_fuel = self.ship.max_fuel - self.ship.fuel_level
            cost = new_fuel * self.fuel_cost
            self.credit -= cost
            self.ship.fuel_level = self.ship.max_fuel
            self.transaction_history.append(Transaction("fuel", cost, "fuel", "expenses"))
            return "Success"
        else:
            self.credit -= cost
            self.ship.refuel(fuel)
            self.transaction_history.append(Transaction("fuel", cost, "fuel", "expenses"))
            return "Success"

    def attempt_buy(self, item, amount):
        if item == None:
            return "No item selected!"
        elif self.credit < (item.b_price * amount):
            return "Not enough credits!"
        elif self.ship.cargo_space < (item.size * amount):
            # not enough space
            return "Not enough space!"
        elif item.amount < amount:
            item.amount < amount
            return "Out of stock!"
        else:
            # successful buy attempt
            return self.trade_buy(item, amount)

    def trade_buy(self, item, amount):
        new_transaction = Transaction(item.name, item.b_price, "trade", "expenses")
        self.transaction_history.append(new_transaction)
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
        item_to_sell = self.ship.cargo[cargo_item_index]
        sell_worth = item_to_sell.s_price * amount
        new_transaction = Transaction(item_to_sell.name, sell_worth, "trade", "earnings")
        if item_to_sell.amount < amount:
            return "You dont have that many"
        elif item_to_sell.amount == amount:
            # player sells last one
            item_to_sell.amount -= amount
            self.credit += sell_worth
            self.ship.cargo.pop(cargo_item_index)
            self.transaction_history.append(new_transaction)
            return "Trade sucessful"
        else:
            # player has more of that item remaining
            item_to_sell.amount -= amount
            self.credit += sell_worth
            self.transaction_history.append(new_transaction)
            return "Trade sucessful"
