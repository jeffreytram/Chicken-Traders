"""This is the module with the player class"""
import utility
from ship import CShip
import copy
class Player:
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

    def trade_buy(self, item, amount):
        if item.amount < amount:
            return "Too many items"
        elif self.ship.cargo_space < (item.size * amount):
            return "Your ship does not have enough space"
        elif self.credit < (item.b_price * amount):
            return "Not enough cash"
        else:
            self.credit -= (item.b_price * amount)
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

        #Index in cargo
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

    def set_name(self, name):
        """Sets the player name"""
        self.name = name

    def set_pilot(self, pilot):
        """Sets the pilot skill points"""
        self.pilot = pilot

    def set_fighter(self, fighter):
        """Sets the fighter skill points"""
        self.fighter = fighter

    def set_merchant(self, merchant):
        """Sets the merchant skill points"""
        self.merchant = merchant

    def set_engineer(self, engineer):
        """Sets the engineer skill points"""
        self.engineer = engineer

    def set_credit(self, credit):
        """Sets the players skill points"""
        self.credit = credit

    def set_ship(self, ship):
        self.ship = ship
