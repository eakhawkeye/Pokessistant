# Pokessistant
Pokessistant
===================
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



Technincal Disclaimer
-------------
Written in a day, there is plenty to clean up and enhance but it works well for its usecase.

 * Linux: Built and testing in Linux
 * Windows: Untested but uses pathlib so it should work
 * Command line based tool only
 * Tool arguments are very flexible to provide the most convience (least typing / formatting).
 * Not using the pokeapi for now as their pokedex needs updating and this tool doesn't need that level of detail.
 * I SSH into my Linux VM via Terminus (mobile ssh) to quickly get details on encouters on the fly