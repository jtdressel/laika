class ship:
    def __init__(self, name, com, water, oxygen):
        self.name = name
        self.com_system_health = com
        self.water_system_health = water
        self.oxygen_garden_health = oxygen
        
    def apply_event(self, event):
        self.com_system_health = self.com_system_health + event.com_system_health_change
        self.water_system_health = self.water_system_health + event.water_system_health_change
        self.oxygen_garden_health = self.oxygen_garden_health + event.oxygen_garden_health_change
        
    def is_alive(self):
        if(self.water_system_health > 0 and self.oxygen_garden_health > 0):
            return True
        return False
        
    def __repr__(self):
        return self.name + \
            ":\n\t Water System: " + repr(self.water_system_health) +  \
            "\n\t Oxygen Garden: " + repr(self.oxygen_garden_health) +  \
            "\n\t Communications System: " + repr(self.com_system_health)