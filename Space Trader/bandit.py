from ship import Ship, AShip, BShip, CShip
class Bandit:
    def __init__(self, name, ship, demand, pilot, fighter):
        self.name = name
        self.ship = ship
        self.demand = demand
        self.pilot = pilot
        self.fighter = fighter

#easy bandit
class Rascal(Bandit):
    def __init__(self):
        super().__init__("Lil Peep", CShip(), 10, 2, 2)

#med
class Thug(Bandit):
    def __init__(self):
        super().__init__("Chicky G", BShip(), 20, 3, 3)

#hard
class Mafia(Bandit):
    def __init__(self):
        super().__init__("Cluck Boss", AShip(), 30, 4, 4)


        


        
        


    