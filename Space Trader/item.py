class Item:
    def __init__(self, amount):
        self.amount = amount

    def use(self, player):
        pass

    def __str__(self):
        return self.__class__.__name__ + ": " + str(self.amount)


# Make more items
class Computer(Item):
    """Framework for computer"""

    name = "Computer"
    category = "Technology"
    debut = 6
    size = 1
    base_price = 100
    description = "It's a Computer!"
    b_price = 0
    s_price = 0

    def __str__(self):
        return super(Computer, self).__str__() + "."


class StrangeTalisman(Item):
    """Framework for Strange Talisman"""

    name = "Strange Talisman"
    category = "Misc."
    debut = 1
    size = 1
    base_price = 5
    description = "A strange talisman from a wandering civilization. It feels warm."
    b_price = 0
    s_price = 0

    def __str__(self):
        return super(StrangeTalisman, self).__str__() + "."


class Banana(Item):
    """Framework for Banana"""

    name = "Banana"
    category = "Food"
    debut = 1
    size = 1
    base_price = 5
    description = "AHHHH. I am banana! Lots of potassium!!!!!"
    b_price = 0
    s_price = 0

    def __str__(self):
        return super(Banana, self).__str__() + "."


class Apple(Item):
    """Framework for Apple"""

    name = "Apple"
    category = "Food"
    debut = 1
    size = 1
    base_price = 5
    description = "yes. apples."
    b_price = 0
    s_price = 0

    def __str__(self):
        return super(Apple, self).__str__() + "."


class Gun(Item):
    """Framework for Gun"""

    name = "Gun"
    category = "Weapons"
    debut = 1
    size = 5
    base_price = 5
    description = "This is gun. BOOM! BOOM!"
    b_price = 0
    s_price = 0

    def __str__(self):
        return super(Gun, self).__str__() + "."


class BiggerGun(Item):
    """Framework for Bigger Gun"""

    name = "Bigger Gun"
    category = "Weapons"
    debut = 1
    size = 10
    base_price = 5
    description = 'now with bigger "BOOM! BOOM!"\'s.'
    b_price = 0
    s_price = 0

    def __str__(self):
        return super(BiggerGun, self).__str__() + "."


class FartInAJar(Item):
    """Framework for Fart in a jar"""

    name = "Fart in a jar"
    category = "Weapons"
    debut = 1
    size = 2
    base_price = 5
    description = "mmmm.... fresh air."
    b_price = 0
    s_price = 0

    def __str__(self):
        return super(FartInAJar, self).__str__() + "."


class Friendship(Item):
    """Framework for Friendship"""

    name = "Friendship"
    category = "Misc."
    debut = 1
    size = 3
    base_price = 15
    description = "eeeeeeeeeeeeee friendship: Solidified."
    b_price = 0
    s_price = 0

    def __str__(self):
        return super(Friendship, self).__str__() + "."


class PocketRussia(Item):
    """Framework for Russia"""

    name = "PocketRussia"
    category = "Country"
    debut = 1
    size = 1
    base_price = 20
    description = "Smaller Russia that fits in your pocket. Remember to share."
    b_price = 0
    s_price = 0

    def __str__(self):
        return super(PocketRussia, self).__str__() + "."


class InvincibilityStar(Item):
    name = "Invincibility Star"
    category = "Weapons"
    debut = 1
    size = 3
    base_price = 200
    description = "Use it to Evicerate any bandits that " \
    + "dare to challenge you and steal all the loot."
    b_price = 0
    s_price = 0

    def __str__(self):
        return super(InvincibilityStar, self).__str__() + "."


class AlienChicken(Item):
    name = "Alien Chicken"
    category = "Animal"
    debut = 2
    size = 3
    base_price = 40
    description = "A chicken from another planet."
    b_price = 0
    s_price = 0

    def __str__(self):
        return super(AlienChicken, self).__str__() + "."


class AssortedAlienAnimalFurs(Item):
    name = "Assorted Alien Animal Furs"
    category = "Animal"
    debut = 1
    size = 3
    base_price = 60
    description = "Assorted furs."
    b_price = 0
    s_price = 0

    def __str__(self):
        return super(AssortedAlienAnimalFurs, self).__str__() + "."
