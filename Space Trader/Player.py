class Player():
    def __init__(self, name, pilot, fighter, merchant, engineer, currRegion, credit):
        self.name = name
        self.pilot = pilot
        self.fighter = fighter
        self.merchant = merchant
        self.engineer = engineer
        self.currRegion = currRegion
        self.credit = credit


    def getName(self):
        return self.name

    def getCurrRegion(self):
        return self.currRegion

    def getCredit(self):
        return self.credit

    def getPilot(self):
        return self.pilot

    def getFighter(self):
        return self.fighter

    def getMerchant(self):
        return self.merchant

    def getEngineer(self):
        return self.engineer

    def setName(self, name):
        self.name = name

    def setCurrRegion(self, currRegion):
        self.currRegion = currRegion

    def setPilot(self, pilot):
        self.pilot = pilot

    def setFighter(self, fighter):
        self.fighter = fighter

    
