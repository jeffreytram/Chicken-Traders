class Item:
    def __init__(self, amount):
        self.amount = amount

#Make more items
class Computer(Item):
    """Framework for computer"""
    name = "Computer"
    category = "Rescources"
    debut_cap = [6, 8]
    size = 1
    base_price = 300
    description = "It's a Computer!"

class StrangeTalisman(Item):
    """Framework for Strange Talisman"""
    name = "Strange Talisman"
    category = "Misc"
    debut_cap = [1, 1]
    size = 1
    base_price = 5
    description = "A strange talisman from a wandering civilization. It feels warm."

class Banana(Item):
    """Framework for Banana"""
    name = "Banana"
    category = "Misc"
    debut_cap = [1, 8]
    size = 1
    base_price = 5
    description = "AHHHH. I am banana! Lots of potassium!!!!!"

class Apple(Item):
    """Framework for Apple"""
    name = "Apple"
    category = "Food"
    debut_cap = [1, 8]
    size = 1
    base_price = 5
    description = "yes. apples."

class Gun(Item):
    """Framework for Gun"""
    name = "Gun"
    category = "Weapon"
    debut_cap = [1, 8]
    size = 1
    base_price = 5
    description = "This is gun. BOOM! BOOM!"

class BiggerGun(Item):
    """Framework for Bigger Gun"""
    name = "Bigger Gun"
    category = "Weapon"
    debut_cap = [1, 8]
    size = 1
    base_price = 5
    description = "now with bigger \"BOOM! BOOM!\"'s"

class FartInAJar(Item):
    """Framework for Fart in a jar"""
    name = "Fart in a jar"
    category = "Weapon"
    debut_cap = [1, 8]
    size = 1
    base_price = 5
    description = "mmmm.... fresh air"

class Friendship(Item):
    """Framework for Friendship"""
    name = "Friendship"
    category = "Misc"
    debut_cap = [1, 8]
    size = 1
    base_price = 5
    description = "eeeeeeeeeeeeee friendship"

class Russia(Item):
    """Framework for Russia"""
    name = "Russia"
    category = "Country"
    debut_cap = [1, 8]
    size = 1
    base_price = 5
    description = "remember to share young comrade"
