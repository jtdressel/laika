from ship import ship
from event import event
from character import character
from item import item


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
    
    item_list.append(item("gun", "When used, a gun prevents the owner from being voted into the reactor"))
    
    
    # Loop to create characters
    num_players_str = raw_input("How many players: ")
    num_players = int(num_players_str)  
    for _ in xrange(num_players):
        #TODO add choice of character abilities
        name = raw_input("Name: ")
        character_a = character(name, 100.0, 2.0, 1.0, .1) #100 health 2 water, 1 oxygen, .1 com
        character_list.append(character_a)
    
    # Game Loop
    

if __name__ == '__main__':
    main()