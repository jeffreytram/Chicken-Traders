import Random

class Universe():
    isUniverse = None;
    regionList = []
    techLevel = TechLevel()
    
    def __new__(cls):
        
        if cls.isUniverse == None:
        #THEN
            cls.isUniverse = super(Universe, cls).__new__(cls)
        #END IF
        return cls.isUniverse
    #END __new__

    def __init__(self, names):
        while len(names) > 0:
            randName = random.randint(0, len(names))
            newRegion = Region(techLevel
                (random.randint(1, 8)).name, names[randName])
            names.pop(randName)
            if len(regionList) == 0:
                regionList.append(newRegion)
            else:
                keepComparing = True
                while keepComparing:
                    keepComparing = False
                    for reg in regionList:
                        if newRegion.compareAndRegen(reg):
                            keepComparing = True
                            break
                        #END if
                    #END for
                    if not keepComparing:
                        regionList.append(newRegion)
                    #END if
                #END while
            #END if and else
        #END while

class Region():
    def __init__(self, techlevel, name):
        self.coordinates = Coordinates()
        self.techLevel = techLevel
        self.name = name
#END Region

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

    def compareAndRegen(self, other):
        regenerated = false
        if abs(self.x - other.x) <= 5:
            self.x.reGenX
            regenerated = true
        elif abs(self.y - other.y) <= 5:
            self.y.reGenY
            regenerated = true
        #END if and elif
        return regenerated
    #END compareAndRegen

    def setCoordinates(self, newX, newY):
        self.x = newX
        self.y = newY
    #END setCoordinates


import enum

class TechLevel(enum.Enum):
    PRE-AG = 1
    AGRICULTURE = 2
    MEDIEVAL = 3
    RENAISSANCE = 4
    INDUSTRIAL = 5
    MODERN = 6
    FUTURISTIC = 7
#END Enum
