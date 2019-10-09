import random
from universe import Universe
from player import Player


class Game:
    def __init__(self, diff):
        self.diff = diff
        self.names = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]
        self.universe = None
        self.player = None

    def start_game(self, name, skill_points, credit):
        self.universe = Universe()
        rand_int = random.randint(0, len(self.universe.region_list) - 1)
        self.player = Player(
            name, skill_points, credit, self.universe.region_list[rand_int]
        )

    # END startGame
