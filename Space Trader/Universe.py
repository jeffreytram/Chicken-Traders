import random
import enum

class TechLevel(enum.Enum):
    PREAG = 1
    AGRICULTURE = 2
    MEDIEVAL = 3
    RENAISSANCE = 4
    INDUSTRIAL = 5
    MODERN = 6
    FUTURISTIC = 7
#END Enum

class Coordinates():
    def __init__(self):
        self.x = random.randint(-200, 201)
        self.y = random.randint(-200, 201)
    #END init

    def reGenX(self):
        self.x = random.randint(-200, 201)
    #END reGenX

    def reGenY(self):
        self.y = random.randint(-200, 201)
    #END reGenY

    def compareAndReCreate(self, other):
        regenerated = False
        if abs(self.x - other.x) <= 5:
            self.reGenX
            regenerated = True
        if abs(self.y - other.y) <= 5:
            self.reGenY
            regenerated = True
        #END if and elif
        return regenerated
    #END compareAndReCreate

    def setCoordinates(self, newX, newY):
        self.x = newX
        self.y = newY
    #END setCoordinates

class Region():
    def __init__(self, techLevel, name):
        self.coordinates = Coordinates()
        self.techLevel = techLevel
        self.name = name
    #END __init__

    def compareAndRegen(self, other):
        self.coordinates.compareAndReCreate(other.coordinates)
    #END compareAndRegen
#END Region

class Universe():
    isUniverse = None;
    regionList = []
    names = ['a','b','c','d','e','f','g','h','i','j']

    def __new__(cls):
        
        if not cls.isUniverse:
        #THEN
            cls.isUniverse = super(Universe, cls).__new__(cls)
        else:
            print("only one")
        #END IF
        return cls.isUniverse
    #END __new__

    def __init__(self):
        #names = ['a','b','c','d','e','f','g','h','i','j']
        while len(Universe.names) > 0:
            randName = random.randint(0, len(Universe.names) - 1)
            newRegion = Region(TechLevel
                (random.randint(1, 7)).name, Universe.names[randName])
            Universe.names.pop(randName)
            if len(Universe.regionList) == 0:
                Universe.regionList.append(newRegion)
            else:
                keepComparing = True
                while keepComparing:
                    keepComparing = False
                    for reg in Universe.regionList:
                        if newRegion.compareAndRegen(reg):
                            keepComparing = True
                            break
                        #END if
                    #END for
                    if not keepComparing:
                        Universe.regionList.append(newRegion)
                    #END if
                #END while
            #END if and else
        #END while