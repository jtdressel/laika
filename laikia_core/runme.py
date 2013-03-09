from ship import ship
from event import event
from character import character
from item import item


def main():
    #Build ship
    laika = ship("Laika", 100.0, 100.0, 100.0)
    characters = []
        
    event_solar_flare = event("Solar Flare", "Solar Flare hit, damaging com system", -10, 0, 0)
    event_oxygen_fire = event("Fire in oxygen garden", "Oh god, fire in the oxygen garden.", 0, -3.0, -20.9)
    
    
    
    character_a = character("Alex", 100.0, 2.0, 1.0, .1)
    character_b = character("Samantha", 100.0, 2.0, 1.0, .1)
    character_c = character("Chris", 100.0, 2.0, 1.0, 4.0)
    character_d = character("Robertson", 100.0, 2.0, 1.0, .4)
    character_e = character("Ted", 100.0, 2.0, 1.0, .4)
    

    
    
    
    # Loop to create characters
    num_players_str = raw_input("How many players: ")
    num_players = int(num_players_str)


    
    for _ in xrange(num_players):
        #TODO add choice of character abilities
        name = raw_input()
        character_a = character(name, 100.0, 2.0, 1.0, .1) #100 health 2 water, 1 oxygen, .1 com
        characters.append(character_a)

    # Setup Loop
    
    gun = item("gun", "When used, a gun prevents the owner from being voted into the reactor")
    
    character_a.add_item(gun)#give character "a" a gun
    
    # Game Loop
    

if __name__ == '__main__':
    main()