class Player:
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
        self.credit = credit
