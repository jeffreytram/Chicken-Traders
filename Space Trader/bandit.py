from game import Game
from ship import Ship, AShip, BShip, CShip
class Bandit:
    def __init__(self, name, ship, demand, pilotLevel, fighterLevel):
        self.name = name
        self.ship = ship
        self.demand = demand
        self.pilotLevel = pilotLevel
        self.fighterLevel = fighterLevel

class Rascal(Bandit):
    def __init__(self):
        super().__init__("Lil Peep", CShip(), 10, 2, 2)

class Thug(Bandit):
    def __init__(self):
        super().__init__("Chicky G", BShip(), 20, 3, 3)

class Mafia(Bandit):
    def __init__(self):
        super().__init__("Cluck Boss", AShip(), 30, 4, 4)
