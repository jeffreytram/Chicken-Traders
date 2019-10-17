class Ship:
    def __init__(self, ship_type, max_cargo_space, fuel_capacity, max_health):
        self.ship_type = ship_type
        self.max_cargo_space = max_cargo_space
        self.fuel_capacity = fuel_capacity
        self.max_health = max_health
        self.fuel_level = fuel_capacity
        self.cargo_space = 0;
        self.health_level = max_health


    # @property
    # def cargo_space(self):
    #     return self.__cargo_space
    
    # @property
    # def fuel_level(self):
    #     return self._fuel_level
    
    # @property
    # def health_level(self):
    #     return self._health_level
    
    # @property
    # def ship_type(self):
    #     return self._ship_type

    def set_cargo_space(self, cargo_space):
        self.cargo_space = cargo_space

    def set_fuel_capacity(self, fuel_capacity):
        self.fuel_level = fuel_level

    def set_health(self, health_level):
        self.health_level = health_level


# 3 ship types, subclasses of ship
class A_Ship(Ship):
    def __init__(self):
        super().__init__("C", 1000, 1000, 100)

class B_Ship(Ship):
    def __init__(self):
        super().__init__("B", 750, 750, 75)

class C_Ship(Ship):
    def __init__(self):
        super().__init__("C", 500, 500, 50)
