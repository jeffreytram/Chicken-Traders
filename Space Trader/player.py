"""This is the module with the player class"""
from ship import Ship, AShip, BShip, CShip
class Player:
    def __init__(self, name, skill_points, credit, curr_region, ship):
        self.name = name
        self.pilot = skill_points[0]
        self.fighter = skill_points[1]
        self.merchant = skill_points[2]
        self.engineer = skill_points[3]
        self.credit = credit
        self.curr_region = curr_region
        self.ship = CShip()

    # END __init__

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
