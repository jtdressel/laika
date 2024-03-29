from laikia_core.ship import ship
from laikia_core.event import event
from laikia_core.character import character
from laikia_core.item import item
import random

REACTOR_CHANCE = 4 # 1 in 4 chance
NUMBER_OF_TURNS = 20

def perform_vote(character_list):
    print "Reactor needs maintenance."
    votes = dict()
    for x in character_list:#everyone starts with zero votes
        votes[x] = 0
    
    count = 0
    for x in character_list: # print list of crew
        print str(count) + ": " + x.name
        count = count + 1
    
    for x in character_list: # do voting
        print x.name + "'s Turn"
        i = raw_input("Enter the number of your vote: ")
        i = int(i)
        votes[character_list[i]] = votes[character_list[i]] + 1
    victim = max(votes, key=votes.get)
    print victim.name + " was voted into the reactor."
    victim.into_the_reactor()# this code is currently buggy
    if (victim.alive):
        pass
    else:
        print victim.name + " has died from radiation."
        character_list.remove(victim)
        
    return character_list

def choose_activity(character_list, ship):
    print "Choose Activity"
    print "0: Scavenge for items"
    print "1: Research the ship"
    print "2: Repair the water system"
    print "3: Repair the oxygen garden"
    print "4: Repair the communication system"
            
    for x in character_list: # do voting
        print x.name + "'s Turn"
        i = raw_input("Choice: ")
        i = int(i)
        if i == 0:
            print "No items found"
            #TODO give item
        elif i == 1:
            x.research()
        elif i == 2:
            ship.fix_water(x.get_water_skill())
        elif i == 3:
            ship.fix_oxygen(x.get_oxygen_skill())
        elif i == 4:
            ship.fix_com(x.get_com_skill())
            
def main():
    #Build ship
    laika = ship("Laika", 100.0, 100.0, 100.0)
    character_list = []
    event_list = []
    item_list = []
    
    #TODO load these from a file
    event_list.append(event("Solar Flare", \
                            "Solar Flare hit, damaging com system", \
                            -10, \
                            0, \
                            0))
    event_list.append(event("Fire in oxygen garden", \
                            "Oh god, fire in the oxygen garden.", \
                            0, \
                            -3.0, \
                            -20.9))
    event_list.append(event("Smooth Sailing", \
                            "Nothing bad happens", \
                            0, \
                            0, \
                            0))
    event_list.append(event("Smooth Sailing", \
                            "Nothing bad happens", \
                            0, \
                            0, \
                            0))
    
    item_list.append(item("gun", "When used, a gun prevents the owner from being voted into the reactor"))
    
    
    # Loop to create characters
    num_players_str = raw_input("How many players: ")
    num_players = int(num_players_str)  
    for _ in xrange(num_players):
        #TODO add choice of character abilities
        name = raw_input("Name: ")
        character_a = character(name, random.uniform(95,100), random.uniform(2,10), random.uniform(2,10), random.uniform(2,10))
        character_list.append(character_a)
    
    # Game Loop
    for _ in xrange(NUMBER_OF_TURNS):
        current_event = random.choice(event_list)
        print current_event
        laika.apply_event(current_event)
        if (laika.is_alive()):
            print laika
            
            if(random.randrange(REACTOR_CHANCE) is 0):
                #Does the reactor need matinence
                character_list = perform_vote(character_list)
            else:
                choose_activity(character_list, laika)
                # people get to choose activity
            
            #Choose Activites:
        else:
            print "The ship has exploded. Game Over"
            break
        

if __name__ == '__main__':
    main()