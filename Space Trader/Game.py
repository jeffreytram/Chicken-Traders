from Universe import *
from Player import Player
import random
class Game():
    def __init__(self, diff):
        self.diff = diff
        self.names = ['a','b','c','d','e','f','g','h','i','j']
        self.universe = None
        self.player = None
    
    def startGame(self, name, skillPoints, credit):
        self.universe = Universe()
        self.player = Player(name, skillPoints, credit, self.universe.regionList
            [random.randint(0, len(self.universe.regionList)) - 1])
    #END startGame