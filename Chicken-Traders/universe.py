"""This module contains the classes needed to create the universe and the universe class."""

import random
import enum
import math
from item import Item
from item import WinningItem


class TechLevel(enum.Enum):
    """This is the enum where the techlevel is distributed from"""

    PREAG = 1
    AGRICULTURE = 2
    MEDIEVAL = 3
    RENAISSANCE = 4
    INDUSTRIAL = 5
    MODERN = 6
    FUTURISTIC = 7


# END Enum


class Coordinates:
    """This is the coordinate class with the methods to
    regenerate and recreate the coordinates when the regions are created"""

    def __init__(self):
        self.x_position = random.randint(-65, 65)
        self.y_position = random.randint(-125, 125)

    # END init

    def recreate_x(self):
        """Recreates the x coordinate."""
        self.x_position = random.randint(-130, 130)

    # END reGenX

    def recreate_y(self):
        """Recreates the y coordinate."""
        self.y_position = random.randint(-250, 250)

    # END reGenY

    def set_coordinates(self, new_x, new_y):
        """Resets the coordinates."""
        self.x_position = new_x
        self.y_position = new_y

    # END setCoordinates


class Region:
    """This is the region class."""

    def __init__(self, tech_level, name):
        self.coordinates = Coordinates()
        self.tech_level = tech_level
        self.travel_cost = 0
        self.name = name
        self.news_multiplier = 1
        self.market = []
        # possible
        self.init_market()

        # END for

    def init_market(self):
        poss_items = Item.__subclasses__()
        # 12 item market limit
        while len(self.market) < 12:
            rand_index = random.randint(0, len(poss_items) - 1)
            # item too advanced for region
            if poss_items[rand_index].debut > self.tech_level.value:
                # remove from possible items in market
                poss_items.pop(rand_index)
            else:
                # region able to support item, add to market
                discard_int = random.randint(1, 12)
                # techlevel <= item debut, higher difference techlevel and debut, higher chance to discard
                # higher tech diff, higher chance to reroll item
                if discard_int > self.tech_level.value - poss_items[rand_index].debut:
                    self.market.append(poss_items[rand_index](random.randint(2, 10)))
                    poss_items.pop(rand_index)

    def compare_and_regen(self, other):
        """This method compares the coordinates to another
        and reacreates them based on the requirements."""
        regenerated = False
        if self.distance(other) <= 50:
            self.coordinates.recreate_x()
            self.coordinates.recreate_y()
            regenerated = True
        return regenerated
    

    # END compareAndRegen

    def distance(self, new_region):
        """Gets the distance between 2 regions"""
        x_1 = self.coordinates.x_position
        y_1 = self.coordinates.y_position
        x_2 = new_region.coordinates.x_position
        y_2 = new_region.coordinates.y_position
        return math.sqrt(((x_2 - x_1) ** 2) + ((y_2 - y_1) ** 2))


# END Region


class Universe:
    """This is the universe class when created it creates all the regions"""

    instance = None

    def __new__(cls):
        if not isinstance(cls.instance, cls):
            # THEN
            cls.instance = super(Universe, cls).__new__(cls)
        # END IF
        return cls.instance

    # END __new__

    def __init__(self):
        self.region_list = []
        self.names = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]
        while len(self.names) > 0:
            new_region = self.create_region()
            if len(self.region_list) == 0:
                self.region_list.append(new_region)
            else:
                self.reg_coord_check(new_region)
                self.region_list.append(new_region)

    def create_region(self):
        # name_index = random.randint(0, len(self.names) - 1)
        new_region = Region(TechLevel(random.randint(1, 7)), self.names[0])
        self.names.pop(0)
        return new_region
    
    def reg_coord_check(self, new_region):
        keep_comparing = True
        while keep_comparing:
            for reg in self.region_list:
                # compares coords of new reg and current region in list
                if new_region.compare_and_regen(reg):
                    self.reg_coord_check(new_region)
                    # check if regen coords are ok
                    break
            keep_comparing = False

    def insert_win(self, item_name):
        market = random.randint(0, len(self.region_list) - 1)
        self.region_list[market].market.append(WinningItem(item_name))
