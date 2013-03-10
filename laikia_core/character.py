class character:
    def __init__(self, name, health, water_skill, oxygen_skill, com_skill):
        self.name = name
        self.health = health
        self.water_skill = water_skill
        self.oxygen_skill = oxygen_skill
        self.com_skill = com_skill
        self.inventory = []
        
    def add_item(self, item):
        self.inventory.append(item)
        
    def __repr__(self):
        return self.name + ":\n \t Heath: " + str(float(self.health))+ \
            "%\n\t Water Skill: " + str(self.water_skill) + \
            "\n\t Oxygen Skill: " + str(self.oxygen_skill) + \
            "\n\t Com Systems Skill: " + str(self.com_skill)
            