class Ship:
    def __init__(self, ship_type, cargo_space, fuel_capacity, health):
        self.ship_type = ship_type
        self.cargo_space = cargo_space
        self.fuel_capacity = fuel_capacity
        self.health = health
    

    def get_cargo_space(self):
        return self.cargo_space

    def get_fuel_capacity(self):
        return self.fuel_capacity

    def get_health(self):
        return self.health

    def get_ship_type(self):
        return self.ship_type

    def set_cargo_space(self, cargo_space):
        self.cargo_space = cargo_space

    def set_fuel_capacity(self, fuel_capacity):
        self.fuel_capacity = fuel_capacity

    def set_health(self, health):
        self.health = health


# 3 ship types, subclasses of ship
class A_Ship(Ship):
    def __init__(self):
        super().__init__("A", 1000, 1000, 100)

class B_Ship(Ship):
    def __init__(self):
        super().__init__("B", 750, 750, 75)

class C_Ship(Ship):
    def __init__(self):
        super().__init__("C", 500, 500, 50)
