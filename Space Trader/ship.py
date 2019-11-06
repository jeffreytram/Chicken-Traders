class Ship:
    def __init__(self, name, ship_type, max_cargo, max_fuel, max_health):
        self.name = name
        self.ship_type = ship_type
        self.max_cargo = max_cargo
        self.max_fuel = max_fuel
        self.max_health = max_health
        self.cargo = []
        self.fuel_level = max_fuel
        self.health_level = max_health

    @property
    def health_level(self):
        return self._health_level

    @health_level.setter
    def health_level(self, value):
        if value < 0:
            self._health_level = 0
        else:
            self._health_level = value

    @property
    def cargo_space(self):
        size_sum = 0
        for merchendise in self.cargo:
            size_sum += merchendise.size * merchendise.amount
        return self.max_cargo - size_sum

    @property
    def cargo_size(self):
        size_sum = 0
        for merch in self.cargo:
            size_sum += merch.size * merch.amount
        return size_sum

    @property
    def health_display(self):
        return str(self.health_level) + "/" + str(self.max_health)

    def set_max_cargo(self, max_cargo):
        self.max_cargo = max_cargo

    def set_max_fuel(self, max_fuel):
        self.max_fuel = max_fuel

    def set_max_health(self, max_health):
        self.max_health = max_health

    def add_item(self, item):
        pass


# 3 ship types, subclasses of ship
class AShip(Ship):
    def __init__(self):
        super().__init__("Ok Ship", "A", 1000, 1000, 100)


class BShip(Ship):
    def __init__(self):
        super().__init__("Meh Ship", "B", 750, 750, 75)


class CShip(Ship):
    def __init__(self):
        super().__init__("Yucky Ship", "C", 500, 500, 50)
