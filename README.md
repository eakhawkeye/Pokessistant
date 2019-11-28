# Pokessistant
"Encounter analysis, pokemonn recommendation(s), and personal, light pokedex"

A tool for managing your pokemon team's capabilities and their encounters. Very useful for quickly chosing the most effective pokemon for Pokemon Sword / Shield raids. This is a single python3 script, self-contained, to make excution quick and easy. 

Capabilities:

 * Quickly analyize an encounter using target type(s)
 * Build your own persistent pokedex(es) of your active inventory
 * Get pokemon encounter recommendations based off the encounter and your available pokemon


How It Works
-------------
 1. Ensure you have a Python3 environment installed 
 2. Simply copy the script onto your system 
 3. Linux: chmod +Xx pokessistant.py`
 4. Run it with some argumennts.


Usage
-------------
```
usage: pokemon [-h] [--add_types ADD_TYPES [ADD_TYPES ...]]
               [--add_moves ADD_MOVES [ADD_MOVES ...]]
               [--add_nickname ADD_NICKNAME]
               [--add_official_name ADD_OFFICIAL_NAME] [--file FILE]
               [--pokedex POKEDEX] [--list] [--remove]
               [types | unique name [types | unique name ...]]

positional arguments:
  type(s) | unique name
                        type(s) or name of pokemon, space separated

optional arguments:
  -h, --help            show this help message and exit
  --add_types ADD_TYPES [ADD_TYPES ...], -t ADD_TYPES [ADD_TYPES ...]
                        add types to the pokemon named, space separated
  --add_moves ADD_MOVES [ADD_MOVES ...], -m ADD_MOVES [ADD_MOVES ...]
                        moves by type, space separated
  --add_nickname ADD_NICKNAME, -n ADD_NICKNAME
                        specify a nickname for the pokemon
  --add_official_name ADD_OFFICIAL_NAME, -o ADD_OFFICIAL_NAME
                        specify the official of the pokemon
  --file FILE, -f FILE  specific a shelve file
  --pokedex POKEDEX, -p POKEDEX
                        save multiple version of pokedex in a single shelve
  --list, -l            list personal pokemon
  --remove, -r          remove the named pokemon

```


Examples
-------------
Encounter: Assess and get Recommendations (if populated pokedex)
```
-$ pokessistant poison dragon

 Attack - poison
    [strong] grass, fairy
      [weak] poison, ground, rock, ghost
    [immune] steel

 Attack - dragon
    [strong] ghost, dragon
      [weak] steel
    [immune] fairy

Defense - combo
    [strong] fire, water, electric, grass, fighting, poison, bug
      [weak] ice, ground, psychic, dragon

Recommendations:
	[43] Ideal: ['Excadrill']
	[34] Ideal: ['Lucario']
	[33] Ideal: ['Bisharp', 'Corviknight']
```

Pokedex: Adding a pokemon
```
-$ pokessistant cinderance -t fire -m fire fighting normal
ADDED cinderace to your pokedex!
	Cinderace: Cinderace Cinderace types['fire'] moves['fire', 'fighting', 'normal']
```

Pokedex: Listing
```
-$ pokessistant --list
Pokedex pokedex from /home/username/.pokemon.shelf:
	Fringe: Fringe Hatterene types['psychic', 'fairy'] moves['psychic', 'fairy', 'ghost']
	Inteleon: Inteleon Inteleon types['water'] moves['water', 'bug']
	Shiftry: Shiftry Shiftry types['grass', 'dark'] moves['grass', 'dark']
	Bisharp: Bisharp Bisharp types['dark', 'steel'] moves['dark', 'steel', 'normal']
	Corviknight: Corviknight Corviknight types['flying', 'steel'] moves['steel', 'flying', 'dark']
	Gardevoir: Gardevoir Gardevoir types['psychic', 'fairy'] moves['psychic', 'fairy', 'ghost']
	Pangoro: Pangoro Pangoro types['fighting', 'dark'] moves['fighting', 'dark']
	Coalossal: Coalossal Coalossal types['rock', 'fire'] moves['rock', 'fire']
	Excadrill: Excadrill Excadrill types['ground', 'steel'] moves['ground', 'steel']
	Boltund: Boltund Boltund types['electric'] moves['electric', 'dark']
	Snip: Snip Togekiss types['fairy', 'flying'] moves['rock', 'fairy', 'flying', 'water']
	Zacian: Zacian Zacian types['fairy'] moves['steel', 'dark', 'fighting', 'fairy']
	Eternatus: Eternatus Eternatus types['poison', 'dragon'] moves['poison', 'dragon', 'fire']
	Lucario: Lucario Lucario types['fighting', 'steel'] moves['steel', 'dragon', 'normal', 'fighting']
	Glaceon: Glaceon Glaceon types['ice'] moves['ice', 'psychic', 'normal']
	Cinderace: Cinderace Cinderace types['fire'] moves['fire', 'fighting', 'normal']
```

Pokedex: Removing a pokemon
```
-$ pokessistant cinderance --remove
REMOVED cinderace from your pokdex
```

Pokedex: Updating pokemon data (move types example)
```
-$ pokessistant inteleon -m water bug grass
ADDED Inteleon to your pokedex!
	Inteleon: Inteleon Inteleon types['water'] moves['water', 'bug', 'grass']
```


Technincal Disclaimer
-------------
Written in a day, there is plenty to clean up and enhance but it works well for its usecase.

 * Linux: Built and testing in Linux
 * Windows: Untested but uses pathlib so it should work
 * Command line based tool only
 * Tool arguments are very flexible to provide the most convience (least typing / formatting).
 * Not using the pokeapi for now as their pokedex needs updating and this tool doesn't need that level of detail.
 * I SSH into my Linux VM via Terminus (mobile ssh) to quickly get details on encouters on the fly