from ship import ship
from event import event
from character import character

laika = ship("Laika", 100.0, 100.0, 100.0)

event_solar_flare = event("Solar Flare", "Solar Flare hit, damaging com system", -10, 0, 0)
event_oxygen_fire = event("Fire in oxygen garden", "Oh god, fire in the oxygen garden.", 0, -3.0, -20.9)



character_a = character("Alex", 100.0, 2.0, 1.0, .1)
character_b = character("Samantha", 100.0, 2.0, 1.0, .1)
character_c = character("Chris", 100.0, 2.0, 1.0, 4.0)
character_d = character("Robertson", 100.0, 2.0, 1.0, .4)
character_e = character("Ted", 100.0, 2.0, 1.0, .4)


print event_solar_flare.name
print event_solar_flare.description
print event_solar_flare.com_system_health_change
print event_solar_flare.water_system_health_change
print event_solar_flare.oxygen_garden_health_change

laika.print_status()
laika.apply_event(event_solar_flare)
laika.print_status()
laika.apply_event(event_oxygen_fire)
laika.print_status()


# Loop to create characters

# Setup Loop

# Game Loop

# 