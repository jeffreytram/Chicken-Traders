"""This module contains the classes needed to create the universe and the universe class."""

import random
import enum
import math
from item import *


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
        self.x_position = random.randint(-200, 200)
        self.y_position = random.randint(-200, 200)

    # END init

    def recreate_x(self):
        """Recreates the x coordinate."""
        self.x_position = random.randint(-200, 200)

    # END reGenX

    def recreate_y(self):
        """Recreates the y coordinate."""
        self.y_position = random.randint(-200, 200)

    # END reGenY

    def compare_and_recreate(self, other):
        """This method compares the coordinates to another
        and reacreates them based on the requirements."""
        regenerated = False
        if abs(self.x_position - other.x_position) <= 5:
            self.recreate_x()
            regenerated = True
        if abs(self.y_position - other.y_position) <= 5:
            self.recreate_y()
            regenerated = True
        # END if and elif
        return regenerated

    # END compareAndReCreate

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
        self.name = name
        self.market = []
        #possible
        poss_items = Item.__subclasses__()
        while len(self.market) < 8:
        	rand_index = random.randint(0, len(poss_items) - 1)
        	if poss_items[rand_index].debut_cap[0] > tech_level.value:
        		poss_items.pop(rand_index)
        	else:
        		self.market.append(poss_items[rand_index](random.randint(10, 20)))
        		poss_items.pop(rand_index)
        #END for

    # END __init__

    def compare_and_regen(self, other):
        """This method calls the coordinate compare
        function so the region class can use it easily."""
        self.coordinates.compare_and_recreate(other.coordinates)

    # END compareAndRegen

    def distance(self, new_region):
        """Gets the distance between 2 regions"""
        x1 = self.coordinates.x_position
        y1 = self.coordinates.y_position
        x2 = new_region.coordinates.x_position
        y2 = new_region.coordinates.y_position
        return math.sqrt(((x2 - x1)**2) + ((y2 - y1)**2))




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
        self.names = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]
        while len(self.names) > 0:
            rand_name = random.randint(0, len(self.names) - 1)
            new_region = Region(
                TechLevel(random.randint(1, 7)), self.names[rand_name]
            )
            self.names.pop(rand_name)
            if len(self.region_list) == 0:
                self.region_list.append(new_region)
            else:
                keep_comparing = True
                while keep_comparing:
                    keep_comparing = False
                    for reg in self.region_list:
                        if new_region.compare_and_regen(reg):
                            keep_comparing = True
                            break
                        # END if
                    # END for
                    if not keep_comparing:
                        self.region_list.append(new_region)
                    # END if
                # END while
            # END if and else
        # END while
