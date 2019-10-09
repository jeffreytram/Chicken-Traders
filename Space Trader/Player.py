"""This is the module with the player class"""
class Player:
<<<<<<< HEAD
    """This is the player class"""
=======
>>>>>>> f7678e5259d901cb59e6226f7df0f88c1356cc2c
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
    def travel(self, region_to):
<<<<<<< HEAD
        """Moves players current region to another."""
        self.curr_region = region_to

    def get_name(self):
        """Return name"""
        return self.name

    def get_curr_region(self):
        """Returns the current region"""
        return self.curr_region

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
=======
        self.curr_region = region_to

    def get_name(self):
        return self.name

    def get_curr_region(self):
        return self.curr_region

    def get_credit(self):
        return self.credit

    def get_pilot(self):
        return self.pilot

    def get_fighter(self):
        return self.fighter

    def get_merchant(self):
        return self.merchant

    def get_engineer(self):
        return self.engineer

    def set_name(self, name):
        self.name = name

    def set_curr_region(self, curr_region):
        self.curr_region = curr_region

    def set_pilot(self, pilot):
        self.pilot = pilot

    def set_fighter(self, fighter):
        self.fighter = fighter

    def set_merchant(self, merchant):
        self.merchant = merchant

    def set_engineer(self, engineer):
        self.engineer = engineer

    def set_credit(self, credit):
>>>>>>> f7678e5259d901cb59e6226f7df0f88c1356cc2c
        self.credit = credit
