class Player:
    def __init__(self, name, skillPoints, credit, currRegion):
        self.name = name
        self.pilot = skillPoints[0]
        self.fighter = skillPoints[1]
        self.merchant = skillPoints[2]
        self.engineer = skillPoints[3]
        self.credit = credit
        self.currRegion = currRegion

    # END __init__

    # Temporary travel method
    def travel(self, regionTo):
        self.currRegion = regionTo

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

    def setMerchant(self, merchant):
        self.merchant = merchant

    def setEngineer(self, engineer):
        self.engineer = engineer

    def setCredit(self, credit):
        self.credit = credit
