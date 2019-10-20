class Item:
    def __init__(self, amount):
        self.amount = amount

    def use(self, player):
        pass

    def __str__(self):
        return self.__class__.__name__ + ": " + str(self.amount)

#Make more items
class Computer(Item):
    """Framework for computer"""
    name = "Computer"
    category = "Rescources"
    debut_cap = [6, 8]
    size = 1
    base_price = 300
    description = "It's a Computer!"

    def __str__(self):
        return super(Computer, self).__str__()

class StrangeTalisman(Item):
    """Framework for Strange Talisman"""
    name = "Strange Talisman"
    category = "Misc"
    debut_cap = [1, 1]
    size = 1
    base_price = 5
    description = "A strange talisman from a wandering civilization. It feels warm."

    def __str__(self):
        return super(StrangeTalisman, self).__str__()

class Banana(Item):
    """Framework for Banana"""
    name = "Banana"
    category = "Misc"
    debut_cap = [1, 8]
    size = 1
    base_price = 5
    description = "AHHHH. I am banana! Lots of potassium!!!!!"

    def __str__(self):
        return super(Banana, self).__str__()

class Apple(Item):
    """Framework for Apple"""
    name = "Apple"
    category = "Food"
    debut_cap = [1, 8]
    size = 1
    base_price = 5
    description = "yes. apples."

    def __str__(self):
        return super(Apple, self).__str__()

class Gun(Item):
    """Framework for Gun"""
    name = "Gun"
    category = "Weapon"
    debut_cap = [1, 8]
    size = 1
    base_price = 5
    description = "This is gun. BOOM! BOOM!"

    def __str__(self):
        return super(Gun, self).__str__()

class BiggerGun(Item):
    """Framework for Bigger Gun"""
    name = "Bigger Gun"
    category = "Weapon"
    debut_cap = [1, 8]
    size = 1
    base_price = 5
    description = "now with bigger \"BOOM! BOOM!\"'s"

    def __str__(self):
        return super(BiggerGun, self).__str__()

class FartInAJar(Item):
    """Framework for Fart in a jar"""
    name = "Fart in a jar"
    category = "Weapon"
    debut_cap = [1, 8]
    size = 1
    base_price = 5
    description = "mmmm.... fresh air"

    def __str__(self):
        return super(FartInAJar, self).__str__()

class Friendship(Item):
    """Framework for Friendship"""
    name = "Friendship"
    category = "Misc"
    debut_cap = [1, 8]
    size = 1
    base_price = 5
    description = "eeeeeeeeeeeeee friendship"

    def __str__(self):
        return super(Friendship, self).__str__()

class Russia(Item):
    """Framework for Russia"""
    name = "Russia"
    category = "Country"
    debut_cap = [1, 8]
    size = 1
    base_price = 5
    description = "remember to share young comrade"

    def __str__(self):
        return super(Russia, self).__str__()
