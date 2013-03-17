class event:
#    name = ""
#    description = ""
#    com_system_health_change = 0
#    water_system_health_change = 0
#    oxygen_garden_health_change = 0
    def __init__(self, name, description, com, water, oxygen):
        self.name = name
        self.description = description
        self.com_system_health_change = com
        self.water_system_health_change = water
        self.oxygen_garden_health_change = oxygen
        
    def __repr__(self):
        return self.name + ":\n " + self.description