class Item:
    name = ""
    debut = 0
    size = 0
    base_price = 0
    description = "This is an Item"

    def __init__(self, amount):
        self.name = self.name
        self.description = self.description
        self.size = self.size
        self.id = self.id
        self.debut = self.debut
        self.amount = amount
        self.max = self.amount
        self.b_price = 0
        self.s_price = 0

    def use(self, player):
        pass

    def __str__(self):
        return self.__class__.__name__ + ": " + str(self.amount)


class WinningItem:
    def __init__(self, name):
        self.id = 13
        self.name = name + "'s Universe"
        self.amount = 1
        self.max = 1
        self.category = "Misc"
        self.description = "Buy this and you win!"
        self.debut = 1
        self.size = 1
        self.base_price = 4500
        self.b_price = 0
        self.s_price = 0

# Make more items
class Computer(Item):
    """Framework for computer"""
    id = 1
    name = "Computer"
    category = "Technology"
    debut = 6
    size = 10
    base_price = 140
    description = "It's a computer!"

    def __str__(self):
        return super(Computer, self).__str__() + "."


class StrangeTalisman(Item):
    """Framework for Strange Talisman"""
    id = 2
    name = "Strange Talisman"
    category = "Misc"
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
    base_price = 45
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
    base_price = 70
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
    base_price = 30
    description = "mmmm.... fresh air."

    def __str__(self):
        return super(FartInAJar, self).__str__() + "."


class Friendship(Item):
    """Framework for Friendship"""

    id = 8
    name = "Friendship"
    category = "Misc"
    debut = 1
    size = 3
    base_price = 40
    description = "eeeeeeeeeeeeee friendship: Solidified."

    def __str__(self):
        return super(Friendship, self).__str__() + "."


class PocketRussia(Item):
    """Framework for Russia"""

    id = 9
    name = "Pocket Russia"
    category = "Misc"
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
    size = 10
    base_price = 450
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
    base_price = 60
    description = "A chicken from another planet."

    def __str__(self):
        return super(AlienChicken, self).__str__() + "."


class AssortedAlienAnimalFurs(Item):
    id = 12
    name = "Assorted Alien Animal Furs"
    category = "Animal"
    debut = 7
    size = 3
    base_price = 85
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
    base_price = 4
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
    category = "Animal"
    debut = 1
    size = 2
    base_price = 6
    description = "Don't flush it down the toilet, please."

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
    category = "Misc"
    debut = 3
    size = 5
    base_price = 20
    description = "A classic game."

    def __str__(self):
        return super(Chess, self).__str__() + "."

class Crown(Item):
    id = 26
    name = "Crown"
    category = "Misc"
    debut = 3
    size = 8
    base_price = 100
    description = "Very pretty."

    def __str__(self):
        return super(Crown, self).__str__() + "."

class BlackDeath(Item):
    id = 27
    name = "Black Death"
    category = "Misc"
    debut = 3
    size = 1
    base_price = 30
    description = "Call the plague doctor!"

    def __str__(self):
        return super(BlackDeath, self).__str__() + "."

class Compass(Item):
    id = 28
    name = "Compass"
    category = "Tool"
    debut = 4
    size = 4
    base_price = 45
    description = "Now with directions!"

    def __str__(self):
        return super(Compass, self).__str__() + "."

class MonaLisa(Item):
    id = 29
    name = "Mona Lisa"
    category = "Misc"
    debut = 4
    size = 4
    base_price = 350
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
    size = 60
    base_price = 200
    description = "A faster horse."

    def __str__(self):
        return super(Car, self).__str__() + "."

class MiniFactory(Item):
    id = 32
    name = "Mini Factory"
    category = "Technology"
    debut = 5
    size = 100
    base_price = 400
    description = "Mass production!"

    def __str__(self):
        return super(MiniFactory, self).__str__() + "."

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
    base_price = 130
    description = "A brick of technology."

    def __str__(self):
        return super(Phone, self).__str__() + "."

class Herbs(Item):
    id = 35
    name = "Herbs"
    category = "Medicine"
    debut = 1
    size = 2
    base_price = 9
    description = "It's natural!"

    def __str__(self):
        return super(Herbs, self).__str__() + "."

class StrangeVial(Item):
    id = 36
    name = "Strange Vial"
    category = "Medicine"
    debut = 2
    size = 3
    base_price = 13
    description = "I think it may make me feel better?"

    def __str__(self):
        return super(StrangeVial, self).__str__() + "."

class Bandage(Item):
    id = 37
    name = "Bandage"
    category = "Medicine"
    debut = 3
    size = 3
    base_price = 15
    description = "Now you can be a mummy!"

    def __str__(self):
        return super(Bandage, self).__str__() + "."

class FirstAidKit(Item):
    id = 38
    name = "First Aid Kit"
    category = "Medicine"
    debut = 5
    size = 5
    base_price = 35
    description = "All in one kit!"

    def __str__(self):
        return super(FirstAidKit, self).__str__() + "."

class Sheep(Item):
    id = 39
    name = "Sheep"
    category = "Animal"
    debut = 2
    size = 30
    base_price = 130
    description = "Lots and lots of wool!"

    def __str__(self):
        return super(Sheep, self).__str__() + "."

class Cattle(Item):
    id = 40
    name = "Cattle"
    category = "Animal"
    debut = 2
    size = 40
    base_price = 160
    description = "One beefy boi."

    def __str__(self):
        return super(Cattle, self).__str__() + "."

class Scythe(Item):
    id = 41
    name = "Scythe"
    category = "Tool"
    debut = 3
    size = 5
    base_price = 15
    description = "Cuts the grass."

    def __str__(self):
        return super(Scythe, self).__str__() + "."

class BoneTool(Item):
    id = 42
    name = "Bone Tool"
    category = "Tool"
    debut = 1
    size = 4
    base_price = 8
    description = "A tool of many uses!"

    def __str__(self):
        return super(BoneTool, self).__str__() + "."

class Glasses(Item):
    id = 43
    name = "Glasses"
    category = "Misc"
    debut = 4
    size = 3
    base_price = 40
    description = "I can finally see!"

    def __str__(self):
        return super(Glasses, self).__str__() + "."

class PumpkinSpiceLatte(Item):
    id = 44
    name = "Pumpkin Spice Latte"
    category = "Food"
    debut = 6
    size = 5
    base_price = 50
    description = "It's not fall without pumpkin spice!"

    def __str__(self):
        return super(PumpkinSpiceLatte, self).__str__() + "."

class Telescope(Item):
    id = 45
    name = "Telescope"
    category = "Technology"
    debut = 4
    size = 12
    base_price = 95
    description = "I can finally see further!"

    def __str__(self):
        return super(Telescope, self).__str__() + "."

class Clock(Item):
    id = 46
    name = "Clock"
    category = "Technology"
    debut = 4
    size = 7
    base_price = 40
    description = "Keeps track of time."

    def __str__(self):
        return super(Clock, self).__str__() + "."

class Battery(Item):
    id = 47
    name = "Battery"
    category = "Technology"
    debut = 5
    size = 5
    base_price = 45
    description = "Portable energy!"

    def __str__(self):
        return super(Battery, self).__str__() + "."

class TV(Item):
    id = 48
    name = "TV"
    category = "Technology"
    debut = 5
    size = 20
    base_price = 120
    description = "Moving pictures!"

    def __str__(self):
        return super(TV, self).__str__() + "."

class Camera(Item):
    id = 49
    name = "Camera"
    category = "Technology"
    debut = 5
    size = 5
    base_price = 80 
    description = "Still pictures!"

    def __str__(self):
        return super(Camera, self).__str__() + "."

class MoonRock(Item):
    id = 50
    name = "Moon Rock"
    category = "Resource"
    debut = 6
    size = 75
    base_price = 325 
    description = "Rocks from the moon!"

    def __str__(self):
        return super(MoonRock, self).__str__() + "."

class StarFragment(Item):
    id = 51
    name = "Star Fragment"
    category = "Resource"
    debut = 7
    size = 30
    base_price = 600
    description = "A piece from the stars..."

    def __str__(self):
        return super(StarFragment, self).__str__() + "."

class Steel(Item):
    id = 52
    name = "Steel"
    category = "Resource"
    debut = 3
    size = 7
    base_price = 20
    description = "Smelted iron!"

    def __str__(self):
        return super(Steel, self).__str__() + "."

class Wood(Item):
    id = 53
    name = "Wood"
    category = "Resource"
    debut = 1
    size = 5
    base_price = 15 
    description = "Trees."

    def __str__(self):
        return super(Wood, self).__str__() + "."

class Copper(Item):
    id = 54
    name = "Copper"
    category = "Resource"
    debut = 2
    size = 5
    base_price = 15
    description = "Into the bronze age!"

    def __str__(self):
        return super(Copper, self).__str__() + "."

class Iron(Item):
    id = 55
    name = "Iron"
    category = "Resource"
    debut = 2
    size = 5
    base_price = 15 
    description = "It's pretty gray."

    def __str__(self):
        return super(Iron, self).__str__() + "."

class Uranium(Item):
    id = 56
    name = "Uranium"
    category = "Resource"
    debut = 5
    size = 8
    base_price = 70
    description = "Lots of energy!"

    def __str__(self):
        return super(Uranium, self).__str__() + "."