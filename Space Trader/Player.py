"""This is the module with the player class"""
class Player:
    """This is the player class"""
    def __init__(self, name, skill_points, credit, curr_region):
        self.name = name
        self.pilot = skill_points[0]
        self.fighter = skill_points[1]
        self.merchant = skill_points[2]
        self.engineer = skill_points[3]
        self.credit = credit
        self.curr_region = curr_region

    # END __init__

    # Temporary travel method
    def travel(self, regionTo):
        """Moves players current region to another."""
        self.currRegion = regionTo

    def get_name(self):
        """Return name"""
        return self.name

    def get_curr_region(self):
        """Returns the current region"""
        return self.currRegion

    def get_credit(self):
        """Returns the players credit"""
        return self.credit

    def get_pilot(self):
        """Returns the pilot skill points"""
        return self.pilot

    def get_fighter(self):
        """Returns the fighter skill points."""
        return self.fighter

    def get_merchant(self):
        """Returns the merchant skillpoints"""
        return self.merchant

    def get_engineer(self):
        """Returns the engineer skill points"""
        return self.engineer

    def set_name(self, name):
        """Sets the player name"""
        self.name = name

    def set_pilot(self, pilot):
        """Sets the pilot skill points"""
        self.pilot = pilot

    def set_fighter(self, fighter):
        """Sets the fighter skill points"""
        self.fighter = fighter

    def set_merchant(self, merchant):
        """Sets the merchant skill points"""
        self.merchant = merchant

    def set_engineer(self, engineer):
        """Sets the engineer skill points"""
        self.engineer = engineer

    def set_credit(self, credit):
        """Sets the players skill points"""
        self.credit = credit
