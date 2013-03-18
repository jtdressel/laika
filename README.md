Last Flight of the Laika
========================

_Last Flight of the Laika_ is a game where players must keep their ship, the 
Laika, afloat, while, at the same time, they strive to survive the ordeal. 
The reactor is malfunctioning, and some players will be voted off the island, 
and into the reactor to allow survival of the ship. 

Each turn players choose how to spend their time, they can repair parts 
of the ship, they can learn more about the ship or they can scavenge for useful
items. Every so often the reactor goes critical, and someone will be voted 
inside to fix it. 

Gameplay
========

Currently _Laika_ is a text based game, so gameplay is rather simple. Run 
laika\_core/runme.py to start the game. 


Code Structure
==============

Most code currently lives in laikia\_core. In it there are several files, one
file per class. character.py has the character class, event.py has the event 
class, item.py is in the item class. The game loop is held in runme.py.

The code is desinged to be mostly object oriented.


Design Revisions
================
Due to lazyness and procrastination, I have not yet implemented the UI, so
gameplay is all text based. The essence of the game is on the decisions, so 
I don't believe it is a major deviance. 


License
-------

Licensed with the MIT License. See the LICENSE file for for information.
