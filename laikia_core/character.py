import random
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
    def into_the_reactor(self):
        print "into the reactor"
        #todo factor in individual radiation resistance and items
        self.health = self.health - random.uniform(30, 50)
        self.health = -3
    
    def research(self):
        i = random.randrange(3)
        improvement = random.uniform(0.01, 3)
        if i == 0:
            print "water system repair skill improved by " + str(improvement)
            self.water_skill = self.water_skill + improvement
        elif i == 1:
            print "oxygen garden repair skill improved by " + str(improvement)
            self.oxygen_skill = self.oxygen_skill + improvement
        elif i == 2:
            print "communication system repair skill improved by " + str(improvement)
            self.com_skill = self.com_skill + improvement
    
    def get_water_skill(self):
        return self.water_skill
        
    def get_com_skill(self):
        return self.com_skill
    
    def get_oxygen_skill(self):
        return self.oxygen_skill
    
    def alive(self):
        if (self.healh > 0):
            return True
        else:
            return False