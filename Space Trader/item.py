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
        self.debut = 1
        self.size = 1
        self.base_price = 4000
        self.b_price = 0
        self.s_price = 0

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
    description = "It's a computer!"

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
    description = "Yes. Apples."

    def __str__(self):
        return super(Apple, self).__str__() + "."


class Gun(Item):
    """Framework for Gun"""

    id = 5
    name = "Gun"
    category = "Weapon"
    debut = 5
    size = 5
    base_price = 30
    description = "This is gun. BOOM! BOOM!"

    def __str__(self):
        return super(Gun, self).__str__() + "."


class BiggerGun(Item):
    """Framework for Bigger Gun"""

    id = 6
    name = "Bigger Gun"
    category = "Weapon"
    debut = 6
    size = 10
    base_price = 50
    description = 'Now with bigger "BOOM! BOOM!"\'s.'

    def __str__(self):
        return super(BiggerGun, self).__str__() + "."


class FartInAJar(Item):
    """Framework for Fart in a jar"""

    id = 7
    name = "Fart in a jar"
    category = "Weapon"
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
    name = "Pocket Russia"
    category = "Misc."
    debut = 1
    size = 1
    base_price = 20
    description = "Smaller Russia that fits in your pocket. Remember to share."

    def __str__(self):
        return super(PocketRussia, self).__str__() + "."


class InvincibilityStar(Item):

    id = 10
    name = "Invincibility Star"
    category = "Weapon"
    debut = 7
    size = 3
    base_price = 200
    description = (
        "Use it to eviscerate any bandits that "
        + "dare to challenge you and steal all the loot."
    )

    def __str__(self):
        return super(InvincibilityStar, self).__str__() + "."


class AlienChicken(Item):
    id = 11
    name = "Alien Chicken"
    category = "Animal"
    debut = 7
    size = 3
    base_price = 40
    description = "A chicken from another planet."

    def __str__(self):
        return super(AlienChicken, self).__str__() + "."


class AssortedAlienAnimalFurs(Item):
    id = 12
    name = "Assorted Alien Animal Furs"
    category = "Animal"
    debut = 7
    size = 3
    base_price = 60
    description = "Assorted furs."

    def __str__(self):
        return super(AssortedAlienAnimalFurs, self).__str__() + "."

class Spear(Item):
    id = 14
    name = "Spear"
    category = "Weapon"
    debut = 1
    size = 5
    base_price = 15
    description = "It's pretty pointy, I guess."

    def __str__(self):
        return super(Spear, self).__str__() + "."

class Berries(Item):
    id = 15
    name = "Berries"
    category = "Food"
    debut = 1
    size = 1
    base_price = 3
    description = "Sweety sweet berries."

    def __str__(self):
        return super(Berries, self).__str__() + "."

class FishingRod(Item):
    id = 16
    name = "Fishing Rod"
    category = "Tool"
    debut = 1
    size = 5
    base_price = 12
    description = "Fisherman at heart!"

    def __str__(self):
        return super(FishingRod, self).__str__() + "."

class Honey(Item):
    id = 17
    name = "Honey"
    category = "Food"
    debut = 1
    size = 2
    base_price = 7
    description = "\"I wasn't going to eat it. I was just going to taste it.\""

    def __str__(self):
        return super(Honey, self).__str__() + "."

class Bow(Item):
    id = 18
    name = "Bow"
    category = "Weapon"
    debut = 1
    size = 4
    base_price = 15
    description = "Where's the arrow?"

    def __str__(self):
        return super(Bow, self).__str__() + "."

class Fish(Item):
    id = 19
    name = "Fish"
    category = "Food"
    debut = 1
    size = 2
    base_price = 6
    description = "A fish outta water."

    def __str__(self):
        return super(Fish, self).__str__() + "."

class Maize(Item):
    id = 20
    name = "Maize"
    category = "Food"
    debut = 2
    size = 1
    base_price = 6
    description = "A-maize-ing"

    def __str__(self):
        return super(Maize, self).__str__() + "."

class Rice(Item):
    id = 21
    name = "Rice"
    category = "Food"
    debut = 2
    size = 1
    base_price = 6
    description = "RICE, RICE, RICE!"

    def __str__(self):
        return super(Rice, self).__str__() + "."

class Potato(Item):
    id = 22
    name = "Potato"
    category = "Food"
    debut = 2
    size = 1
    base_price = 6
    description = "This is a potato."

    def __str__(self):
        return super(Potato, self).__str__() + "."

class Sword(Item):
    id = 23
    name = "Sword"
    category = "Weapon"
    debut = 3
    size = 14
    base_price = 20
    description = "Very pointy."

    def __str__(self):
        return super(Sword, self).__str__() + "."

class Bread(Item):
    id = 24
    name = "Bread"
    category = "Food"
    debut = 3
    size = 3
    base_price = 11
    description = "Bready."

    def __str__(self):
        return super(Bread, self).__str__() + "."

class Chess(Item):
    id = 25
    name = "Chess"
    category = "Misc."
    debut = 3
    size = 5
    base_price = 20
    description = "A classic game."

    def __str__(self):
        return super(Chess, self).__str__() + "."

class Crown(Item):
    id = 26
    name = "Crown"
    category = "Misc."
    debut = 3
    size = 8
    base_price = 80
    description = "Very pretty."

    def __str__(self):
        return super(Crown, self).__str__() + "."

class BlackDeath(Item):
    id = 27
    name = "Black Death"
    category = "Misc."
    debut = 3
    size = 1
    base_price = 30
    description = "Call the plague doctor!"

    def __str__(self):
        return super(BlackDeath, self).__str__() + "."

class Compass(Item):
    id = 28
    name = "Compass"
    category = "Technology"
    debut = 4
    size = 4
    base_price = 45
    description = "Now with directions!"

    def __str__(self):
        return super(Compass, self).__str__() + "."

class MonaLisa(Item):
    id = 29
    name = "Mona Lisa"
    category = "Misc."
    debut = 4
    size = 4
    base_price = 70
    description = "Some painting."

    def __str__(self):
        return super(MonaLisa, self).__str__() + "."

class Gunpowder(Item):
    id = 30
    name = "Gunpowder"
    category = "Resource"
    debut = 4
    size = 2
    base_price = 18
    description = "Explosive!"

    def __str__(self):
        return super(Gunpowder, self).__str__() + "."

class Car(Item):
    id = 31
    name = "Car"
    category = "Technology"
    debut = 5
    size = 20
    base_price = 150
    description = "A faster horse."

    def __str__(self):
        return super(Car, self).__str__() + "."

class Factory(Item):
    id = 32
    name = "Factory"
    category = "Technology"
    debut = 5
    size = 30
    base_price = 400
    description = "Mass production!"

    def __str__(self):
        return super(Factory, self).__str__() + "."

class Coal(Item):
    id = 33
    name = "Coal"
    category = "Resource"
    debut = 5
    size = 5
    base_price = 30
    description = "Someone's been naughty!"

    def __str__(self):
        return super(Coal, self).__str__() + "."

class Phone(Item):
    id = 34
    name = "Phone"
    category = "Technology"
    debut = 6
    size = 10
    base_price = 100
    description = "A brick of technology."

    def __str__(self):
        return super(Phone, self).__str__() + "."