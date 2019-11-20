class Item:
    name = ""
    debut = 0
    size = 0
    base_price = 0
    description = "This is an Item"

    def __init__(self, amount):
        self.amount = amount
        self.b_price = 0
        self.s_price = 0

    def use(self, player):
        pass

    def __str__(self):
        return self.__class__.__name__ + ": " + str(self.amount)


class WinningItem:
    id = 13
    def __init__(self, name):
        self.name = name + "'s Universe"
        self.amount = 1
        self.category = "Misc."
        self.base_price = 4000
        self.b_price = 0
        self.s_price = 0
        self.debut = 1
        self.size = 1

    @property
    def description(self):
        return self.name + ". Buy this and you win!"

# Make more items
class Computer(Item):
    """Framework for computer"""
    id = 1
    name = "Computer"
    category = "Technology"
    debut = 6
    size = 10
    base_price = 100
    description = "It's a Computer!"

    def __str__(self):
        return super(Computer, self).__str__() + "."


class StrangeTalisman(Item):
    """Framework for Strange Talisman"""
    id = 2
    name = "Strange Talisman"
    category = "Misc."
    debut = 1
    size = 4
    base_price = 5
    description = "A strange talisman from a wandering civilization. It feels warm."

    def __str__(self):
        return super(StrangeTalisman, self).__str__() + "."


class Banana(Item):
    """Framework for Banana"""
    id = 3
    name = "Banana"
    category = "Food"
    debut = 1
    size = 1
    base_price = 5
    description = "AHHHH. I am banana! Lots of potassium!!!!!"

    def __str__(self):
        return super(Banana, self).__str__() + "."


class Apple(Item):
    """Framework for Apple"""

    id = 4
    name = "Apple"
    category = "Food"
    debut = 1
    size = 1
    base_price = 5
    description = "yes. apples."

    def __str__(self):
        return super(Apple, self).__str__() + "."


class Gun(Item):
    """Framework for Gun"""

    id = 5
    name = "Gun"
    category = "Weapons"
    debut = 1
    size = 5
    base_price = 5
    description = "This is gun. BOOM! BOOM!"

    def __str__(self):
        return super(Gun, self).__str__() + "."


class BiggerGun(Item):
    """Framework for Bigger Gun"""

    id = 6
    name = "Bigger Gun"
    category = "Weapons"
    debut = 1
    size = 10
    base_price = 5
    description = 'now with bigger "BOOM! BOOM!"\'s.'

    def __str__(self):
        return super(BiggerGun, self).__str__() + "."


class FartInAJar(Item):
    """Framework for Fart in a jar"""

    id = 7
    name = "Fart in a jar"
    category = "Weapons"
    debut = 1
    size = 2
    base_price = 5
    description = "mmmm.... fresh air."

    def __str__(self):
        return super(FartInAJar, self).__str__() + "."


class Friendship(Item):
    """Framework for Friendship"""

    id = 8
    name = "Friendship"
    category = "Misc."
    debut = 1
    size = 3
    base_price = 15
    description = "eeeeeeeeeeeeee friendship: Solidified."

    def __str__(self):
        return super(Friendship, self).__str__() + "."


class PocketRussia(Item):
    """Framework for Russia"""

    id = 9
    name = "PocketRussia"
    category = "Country"
    debut = 1
    size = 1
    base_price = 20
    description = "Smaller Russia that fits in your pocket. Remember to share."

    def __str__(self):
        return super(PocketRussia, self).__str__() + "."


class InvincibilityStar(Item):

    id = 10
    name = "Invincibility Star"
    category = "Weapons"
    debut = 1
    size = 3
    base_price = 200
    description = (
        "Use it to Evicerate any bandits that "
        + "dare to challenge you and steal all the loot."
    )

    def __str__(self):
        return super(InvincibilityStar, self).__str__() + "."


class AlienChicken(Item):
    id = 11
    name = "Alien Chicken"
    category = "Animal"
    debut = 2
    size = 3
    base_price = 40
    description = "A chicken from another planet."

    def __str__(self):
        return super(AlienChicken, self).__str__() + "."


class AssortedAlienAnimalFurs(Item):
    id = 12
    name = "Assorted Alien Animal Furs"
    category = "Animal"
    debut = 1
    size = 3
    base_price = 60
    description = "Assorted furs."

    def __str__(self):
        return super(AssortedAlienAnimalFurs, self).__str__() + "."
