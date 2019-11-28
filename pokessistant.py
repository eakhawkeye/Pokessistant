#!/usr/bin/python3
# 
# Pokemon Picker and Personal Light Pokedex
#   by EAKHawkeye
#

import argparse
import shelve
import sys
from pathlib import Path


# Global descriptors
glb_strong = 'strong'
glb_normal = 'normal'
glb_weak = 'weak'
glb_immune = 'immune'
glb_offense = 'attack'
glb_defense = 'defense'

# Type interaction
glb_dct_types = {
    'normal': {
        glb_offense: {'normal': 1,'fire': 1,'water': 1,'electric': 1,'grass': 1,'ice': 1,'fighting': 1,'poison': 1,'ground': 1,'flying': 1,'psychic': 1,'bug': 1,'rock': 0.5,'ghost': 0,'dragon': 1,'dark': 1,'steel': 0.5,'fairy': 1},
        glb_defense: {'normal': 1,'fire': 1,'water': 1,'electric': 1,'grass': 1,'ice': 1,'fighting': 2,'poison': 1,'ground': 1,'flying': 1,'psychic': 1,'bug': 1,'rock': 1,'ghost': 0,'dragon': 1,'dark': 1,'steel': 1,'fairy': 1},
    },
    'fire': {
        glb_offense: {'normal': 1,'fire': 0.5,'water': 0.5,'electric': 1,'grass': 2,'ice': 2,'fighting': 1,'poison': 1,'ground': 1,'flying': 1,'psychic': 1,'bug': 2,'rock': 0.5,'ghost': 1,'dragon': 0.5,'dark': 1,'steel': 2,'fairy': 1},
        glb_defense: {'normal': 1,'fire': 0.5,'water': 2,'electric': 1,'grass': 0.5,'ice': 0.5,'fighting': 1,'poison': 1,'ground': 2,'flying': 1,'psychic': 1,'bug': 0.5,'rock': 2,'ghost': 1,'dragon': 1,'dark': 1,'steel': 0.5,'fairy': 0.5},
    },
    'water': {
        glb_offense: {'normal': 1,'fire': 2,'water': 0.5,'electric': 1,'grass': 0.5,'ice': 1,'fighting': 1,'poison': 1,'ground': 2,'flying': 1,'psychic': 1,'bug': 1,'rock': 2,'ghost': 1,'dragon': 0.5,'dark': 1,'steel': 1,'fairy': 1},
        glb_defense: {'normal': 1,'fire': 0.5, 'water': 0.5, 'electric': 2, 'grass': 2, 'ice': 0.5, 'fighting': 1, 'poison': 1, 'ground': 1, 'flying': 1, 'psychic': 1, 'bug': 1, 'rock': 1, 'ghost': 1, 'dragon': 1, 'dark': 1, 'steel': 0.5, 'fairy': 1 }, 
        }, 
    'electric': { 
        glb_offense: { 'normal': 1, 'fire': 1, 'water': 2, 'electric': 0.5, 'grass': 0.5, 'ice': 1, 'fighting': 1, 'poison': 1, 'ground': 0, 'flying': 2, 'psychic': 1, 'bug': 1, 'rock': 1, 'ghost': 1, 'dragon': 0.5, 'dark': 1, 'steel': 1, 'fairy': 1 }, 
        glb_defense: { 'normal': 1, 'fire': 1, 'water': 1, 'electric': 0.5, 'grass': 1, 'ice': 1, 'fighting': 1, 'poison': 1, 'ground': 2, 'flying': 0.5, 'psychic': 1, 'bug': 1, 'rock': 1, 'ghost': 1, 'dragon': 1, 'dark': 1, 'steel': 0.5, 'fairy': 1 }, 
    }, 
    'grass': { 
        glb_offense: { 'normal': 1, 'fire': 0.5, 'water': 2, 'electric': 1, 'grass': 0.5, 'ice': 1, 'fighting': 1, 'poison': 0.5, 'ground': 2, 'flying': 0.5, 'psychic': 1, 'bug': 0.5, 'rock': 2, 'ghost': 1, 'dragon': 0.5, 'dark': 1, 'steel': 1, 'fairy': 1 }, 
        glb_defense: { 'normal': 1, 'fire': 2, 'water': 0.5, 'electric': 0.5, 'grass': 0.5, 'ice': 2, 'fighting': 1, 'poison': 2, 'ground': 0.5, 'flying': 2, 'psychic': 1, 'bug': 2, 'rock': 1, 'ghost': 1, 'dragon': 1, 'dark': 1, 'steel': 1, 'fairy': 1 }, 
    }, 
    'ice': { 
        glb_offense: { 'normal': 1, 'fire': 0.5, 'water': 0.5, 'electric': 1, 'grass': 2, 'ice': 0.5, 'fighting': 1, 'poison': 1, 'ground': 2, 'flying': 2, 'psychic': 1, 'bug': 1, 'rock': 1, 'ghost': 1, 'dragon': 2, 'dark': 1, 'steel': 0.5, 'fairy': 1 }, 
        glb_defense: { 'normal': 1, 'fire': 2, 'water': 1, 'electric': 1, 'grass': 1, 'ice': 0.5, 'fighting': 2, 'poison': 1, 'ground': 1, 'flying': 1, 'psychic': 1, 'bug': 1, 'rock': 2, 'ghost': 1, 'dragon': 1, 'dark': 1, 'steel': 2, 'fairy': 1 }, 
    }, 
    'fighting': { 
        glb_offense: { 'normal': 2, 'fire': 1, 'water': 1, 'electric': 1, 'grass': 1, 'ice': 2, 'fighting': 1, 'poison': 0.5, 'ground': 1, 'flying': 0.5, 'psychic': 0.5, 'bug': 0.5, 'rock': 2, 'ghost': 0, 'dragon': 1, 'dark': 2, 'steel': 2, 'fairy': 0.5 }, 
        glb_defense: { 'normal': 1, 'fire': 1, 'water': 1, 'electric': 1, 'grass': 1, 'ice': 1, 'fighting': 1, 'poison': 1, 'ground': 1, 'flying': 2, 'psychic': 2, 'bug': 0.5, 'rock': 0.5, 'ghost': 1, 'dragon': 1, 'dark': 0.5, 'steel': 1, 'fairy': 2 }, 
    }, 
    'poison': { 
        glb_offense: { 'normal': 1, 'fire': 1, 'water': 1, 'electric': 1, 'grass': 2, 'ice': 1, 'fighting': 1, 'poison': 0.5, 'ground': 0.5, 'flying': 1, 'psychic': 1, 'bug': 1, 'rock': 0.5, 'ghost': 0.5, 'dragon': 1, 'dark': 1, 'steel': 0, 'fairy': 2 }, 
        glb_defense: { 'normal': 1, 'fire': 1, 'water': 1, 'electric': 1, 'grass': 0.5, 'ice': 1, 'fighting': 0.5, 'poison': 0.5, 'ground': 2, 'flying': 1, 'psychic': 2, 'bug': 0.5, 'rock': 1, 'ghost': 1, 'dragon': 1, 'dark': 1, 'steel': 1, 'fairy': 0.5 }, 
    }, 
    'ground': { 
        glb_offense: { 'normal': 1, 'fire': 2, 'water': 1, 'electric': 2, 'grass': 0.5, 'ice': 1, 'fighting': 1, 'poison': 2, 'ground': 1, 'flying': 0, 'psychic': 1, 'bug': 0.5, 'rock': 2, 'ghost': 1, 'dragon': 1, 'dark': 1, 'steel': 2, 'fairy': 1 }, 
        glb_defense: { 'normal': 1, 'fire': 1, 'water': 2, 'electric': 0, 'grass': 2, 'ice': 2, 'fighting': 1, 'poison': 0.5, 'ground': 1, 'flying': 1, 'psychic': 1, 'bug': 1, 'rock': 0.5, 'ghost': 1, 'dragon': 1, 'dark': 1, 'steel': 1, 'fairy': 1 }, 
    }, 
    'flying': { 
        glb_offense: { 'normal': 1, 'fire': 1, 'water': 1, 'electric': 0.5, 'grass': 2, 'ice': 1, 'fighting': 2, 'poison': 1, 'ground': 1, 'flying': 1, 'psychic': 1, 'bug': 2, 'rock': 0.5, 'ghost': 1, 'dragon': 1, 'dark': 1, 'steel': 0.5, 'fairy': 1 }, 
        glb_defense: { 'normal': 1, 'fire': 1, 'water': 1, 'electric': 2, 'grass': 0.5, 'ice': 2, 'fighting': 0.5, 'poison': 1, 'ground': 0, 'flying': 1, 'psychic': 1, 'bug': 0.5, 'rock': 2, 'ghost': 1, 'dragon': 1, 'dark': 1, 'steel': 1, 'fairy': 1 }, 
    }, 
    'psychic': { 
        glb_offense: { 'normal': 1, 'fire': 1, 'water': 1, 'electric': 1, 'grass': 1, 'ice': 1, 'fighting': 2, 'poison': 2, 'ground': 1, 'flying': 1, 'psychic': 0.5, 'bug': 1, 'rock': 1, 'ghost': 1, 'dragon': 1, 'dark': 0, 'steel': 0.5, 'fairy': 1 }, 
        glb_defense: { 'normal': 1, 'fire': 1, 'water': 1, 'electric': 1, 'grass': 1, 'ice': 1, 'fighting': 0.5, 'poison': 1, 'ground': 1, 'flying': 1, 'psychic': 0.5, 'bug': 2, 'rock': 1, 'ghost': 2, 'dragon': 1, 'dark': 2, 'steel': 1, 'fairy': 1 }, 
    }, 
    'bug': { 
        glb_offense: { 'normal': 1, 'fire': 0.5, 'water': 1, 'electric': 1, 'grass': 2, 'ice': 1, 'fighting': 0.5, 'poison': 0.5, 'ground': 1, 'flying': 0.5, 'psychic': 2, 'bug': 1, 'rock': 1, 'ghost': 0.5, 'dragon': 1, 'dark': 2, 'steel': 0.5, 'fairy': 0.5 }, 
        glb_defense: { 'normal': 1, 'fire': 2, 'water': 1, 'electric': 1, 'grass': 0.5, 'ice': 1, 'fighting': 0.5, 'poison': 1, 'ground': 0.5, 'flying': 2, 'psychic': 1, 'bug': 1, 'rock': 2, 'ghost': 1, 'dragon': 1, 'dark': 1, 'steel': 1, 'fairy': 1 }, 
    }, 
    'rock': { 
        glb_offense: { 'normal': 1, 'fire': 2, 'water': 1, 'electric': 1, 'grass': 1, 'ice': 2, 'fighting': 0.5, 'poison': 1, 'ground': 0.5, 'flying': 2, 'psychic': 1, 'bug': 2, 'rock': 1, 'ghost': 0.5, 'dragon': 1, 'dark': 1, 'steel': 0.5, 'fairy': 1 }, 
        glb_defense: { 'normal': 0.5, 'fire': 0.5, 'water': 2, 'electric': 1, 'grass': 2, 'ice': 1, 'fighting': 2, 'poison': 0.5, 'ground': 2, 'flying': 0.5, 'psychic': 1, 'bug': 1, 'rock': 1, 'ghost': 1, 'dragon': 1, 'dark': 1, 'steel': 2, 'fairy': 1 }, 
    }, 
    'ghost': { 
        glb_offense: { 'normal': 0, 'fire': 1, 'water': 1, 'electric': 1, 'grass': 1, 'ice': 1, 'fighting': 1, 'poison': 1, 'ground': 1, 'flying': 1, 'psychic': 2, 'bug': 1, 'rock': 1, 'ghost': 2, 'dragon': 1, 'dark': 0.5, 'steel': 1, 'fairy': 1 }, 
        glb_defense: { 'normal': 0, 'fire': 1, 'water': 1, 'electric': 1, 'grass': 1, 'ice': 1, 'fighting': 0, 'poison': 0.5, 'ground': 1, 'flying': 1, 'psychic': 1, 'bug': 0.5, 'rock': 1, 'ghost': 2, 'dragon': 1, 'dark': 2, 'steel': 1, 'fairy': 1 }, 
    }, 
    'dragon': { 
        glb_offense: { 'normal': 1, 'fire': 1, 'water': 1, 'electric': 1, 'grass': 1, 'ice': 1, 'fighting': 1, 'poison': 1, 'ground': 1, 'flying': 1, 'psychic': 1, 'bug': 1, 'rock': 1, 'ghost': 2, 'dragon': 2, 'dark': 1, 'steel': 0.5, 'fairy': 0 }, 
        glb_defense: { 'normal': 1, 'fire': 0.5, 'water': 0.5, 'electric': 0.5, 'grass': 0.5, 'ice': 2, 'fighting': 1, 'poison': 1, 'ground': 1, 'flying': 1, 'psychic': 1, 'bug': 1, 'rock': 1, 'ghost': 1, 'dragon': 2, 'dark': 1, 'steel': 1, 'fairy': 2 }, 
    }, 
    'dark': { 
        glb_offense: { 'normal': 1, 'fire': 1, 'water': 1, 'electric': 1, 'grass': 1, 'ice': 1, 'fighting': 0.5, 'poison': 1, 'ground': 1, 'flying': 1, 'psychic': 2, 'bug': 1, 'rock': 1, 'ghost': 2, 'dragon': 1, 'dark': 0.5, 'steel': 1, 'fairy': 0.5 }, 
        glb_defense: { 'normal': 1, 'fire': 1, 'water': 1, 'electric': 1, 'grass': 1, 'ice': 1, 'fighting': 2, 'poison': 1, 'ground': 1, 'flying': 1, 'psychic': 0, 'bug': 2, 'rock': 1, 'ghost': 0.5, 'dragon': 1, 'dark': 0.5, 'steel': 1, 'fairy': 2 }, 
    }, 
    'steel': { 
        glb_offense: { 'normal': 1, 'fire': 0.5, 'water': 0.5, 'electric': 0.5, 'grass': 1, 'ice': 2, 'fighting': 1, 'poison': 1, 'ground': 1, 'flying': 1, 'psychic': 1, 'bug': 1, 'rock': 2, 'ghost': 2, 'dragon': 1, 'dark': 1, 'steel': 0.5, 'fairy': 2 }, 
        glb_defense: { 'normal': 0.5, 'fire': 2, 'water': 1, 'electric': 1, 'grass': 0.5, 'ice': 0.5, 'fighting': 2, 'poison': 0, 'ground': 2, 'flying': 0.5, 'psychic': 0.5, 'bug': 0.5, 'rock': 0.5, 'ghost': 1, 'dragon': 0.5, 'dark': 1, 'steel': 0.5, 'fairy': 0.5 }, 
    }, 
    'fairy': { 
        glb_offense: { 'normal': 1, 'fire': 0.5, 'water': 1, 'electric': 1, 'grass': 1, 'ice': 1, 'fighting': 2, 'poison': 0.5, 'ground': 1, 'flying': 1, 'psychic': 1, 'bug': 1, 'rock': 2, 'ghost': 2, 'dragon': 2, 'dark': 2, 'steel': 0.5, 'fairy': 1 }, 
        glb_defense: { 'normal': 1, 'fire': 1, 'water': 1, 'electric': 1, 'grass': 1, 'ice': 1, 'fighting': 0.5, 'poison': 2, 'ground': 1, 'flying': 1, 'psychic': 1, 'bug': 0.5, 'rock': 1, 'ghost': 1, 'dragon': 0, 'dark': 0.5, 'steel': 2, 'fairy': 1 }, 
    }
}
glb_lst_damage_types = [ key for key in glb_dct_types ]



def build_pokemon(pokemon_name, types, moves=[], pokemon_nickname=None, pokemon_official=None):
    # Create the pokemon dictionary
    # input: pokemon_name (str), types (lst), moves (lst)
    # output: dct_pokemon
    dct_pokemon = { 
        pokemon_name: {
            'nickname': pokemon_nickname, 
            'official': pokemon_official, 
            'types': types, 
            'moves': moves 
        }
    }
    return dct_pokemon


def save(shelve_file, shelve_pokedex, dct_pokedex):
    # Save the data
    # input: shelve file name, shelve pokedex name, dct_pokedex, dct_pokemon
    try:
        with shelve.open(shelve_file, 'c') as shelf:
            shelf[shelve_pokedex] = dct_pokedex
    except OSError as error:
        if error.errno == 11:  # Cache open by another person/program
            # print('Cache unavailable, skipping save')
            pass
        else:
            raise error


def load(shelve_file, shelve_pokedex):
    # Load the saved data
    # input: shelve filename
    # output: dictionary of shelve file contents
    try:
        with shelve.open(shelve_file, 'c') as shelve_db:
            # Return the proper pokedex. create if needed
            if not shelve_pokedex in shelve_db:
                shelve_db[shelve_pokedex] = {}
            return shelve_db[shelve_pokedex]
    except OSError as error:
        if error.errno == 11:
            raise KeyError( 'shelve file could not be opened.')
        else:
            raise


def pokedex_get_key(pokemon_name, dct_pokedex):
    # return the key name for the pokemon name in the pokedex
    title_pokemon_name = pokemon_name.title()
    for key_name in dct_pokedex:
        if (
            title_pokemon_name == key_name or
            title_pokemon_name == dct_pokedex[key_name]['nickname'] or
            title_pokemon_name == dct_pokedex[key_name]['official']
            ):
            return key_name
    return None


def validate_type(poke_type):
    # input: string of type
    # output: boolean
    if poke_type in glb_lst_damage_types:
        return True
    return False


def pokemon_add(pokemon_name, pokemon_nickname, pokemon_official, lst_add_types, lst_add_moves, dct_pokedex, shelve_file, shelve_pokedex):
    # Add a pokemon to the pokedex
    # outpput: dictionary of pokedex

    # Load any previous instance of the pokemon
    pokemon_key = pokedex_get_key(pokemon_name, dct_pokedex)
    if pokemon_key:
        pokemon_name = pokemon_key
        pokemon_nickname = dct_pokedex[pokemon_name]['nickname']
        pokemon_official = dct_pokedex[pokemon_name]['official']
        lst_add_types = dct_pokedex[pokemon_name]['types'] if not lst_add_types else lst_add_types
        lst_add_moves = dct_pokedex[pokemon_name]['moves'] if not lst_add_moves else lst_add_moves
    else:
        pokemon_nickname = pokemon_nickname if pokemon_nickname else pokemon_name
        pokemon_official = pokemon_official if pokemon_official else pokemon_name

    # Validate the various types
    for poke_type in lst_add_types + lst_add_moves:
        if not validate_type(poke_type):
            print('Type:', poke_type, 'is not a valid type')
            sys.exit(1)
        
    # Create the pokemon dictionary, update the pokedex, then save the file
    dct_pokemon = build_pokemon(pokemon_name.title(), lst_add_types, lst_add_moves, pokemon_nickname.title(), pokemon_official.title())
    dct_pokedex.update(dct_pokemon)
    save(shelve_file, shelve_pokedex, dct_pokedex)
    print('ADDED %s to your pokedex!' % (pokemon_name))
    
    return load(shelve_file, shelve_pokedex)


def pokemon_remove(pokemon_name, dct_pokedex, shelve_file, shelve_pokedex):
    # Remove a pokemon from the pokedex
    # input: lots
    # output: dictionry of pokedex
    pokemon_key = pokedex_get_key(pokemon_name, dct_pokedex)
    if pokemon_key:
        del dct_pokedex[pokemon_key]
        save(shelve_file, shelve_pokedex, dct_pokedex)
        print('REMOVED %s from your pokdex' % (pokemon_name))

    return load(shelve_file, shelve_pokedex)


def compute_combination(lst_query_types):
    # Compile the results
    # imput: list of types (<=2)
    # output: {position: {type: {strong: [], weak: [], immune: [], normal: []}}}
    query_type1 = lst_query_types[0]
    query_type2 = lst_query_types[1] if len(lst_query_types) > 1 else None

    # Prepare the results dictionary
    dct_results = {
        glb_offense: {}, 
        glb_defense: {
            'combo': { glb_strong: [], glb_weak: [], glb_immune: [], glb_normal: []}
        }
    }
    for poke_type in lst_query_types:
        dct_results[glb_offense].update( { poke_type: { glb_strong: [], glb_weak: [], glb_immune: [], glb_normal: [] }} )

    # Build results for attack
    position = glb_offense
    for poke_type in dct_results[position]:
        for damage_type, value in glb_dct_types[poke_type][position].items():
            if value == 0:
                dct_results[position][poke_type][glb_immune].append(damage_type)
            elif value > 1:
                dct_results[position][poke_type][glb_strong].append(damage_type)
            elif value == 1:
                dct_results[position][poke_type][glb_normal].append(damage_type)
            elif value < 1:
                dct_results[position][poke_type][glb_weak].append(damage_type)

    # Build results for defense
    position = glb_defense
    # Iterate through the damage_types
    for damage_type in glb_lst_damage_types:
        # Compute combined type values
        value = glb_dct_types[query_type2][position][damage_type] if query_type2 else 1
        value *= glb_dct_types[query_type1][position][damage_type]

        # Build results based on combined values
        if value == 0:
            dct_results[position]['combo'][glb_immune].append(damage_type)
        elif value < 1:
            dct_results[position]['combo'][glb_strong].append(damage_type)
        elif value == 1:
            dct_results[position]['combo'][glb_normal].append(damage_type)
        elif value > 1:
            dct_results[position]['combo'][glb_weak].append(damage_type)

    # return the results
    return dct_results


def compute_encounter_score(dct_results, dct_pokedex):
    # Here we come up with a score
    # based on the previous encounter details
    # input: dct_results = {offense/defense: {type/combo: {strong: [], weak: [], immune: []}, normal: []}}
    #        dct_pokedex = {pokemon_name {types:[], moves[]}}
    # output: dictionary{score: [ pokemon ]}
    dct_tally = {}

    # Scoring: We match the types in categories then compute a score
    # Higher Score is better. Weighted toward survival
    #   Target Attack vs player types
    #       strong = -20, normal = 0, weak = 10, immune = 20
    #   Target Defense vs player moves
    #       immune = -1, strong = 0, normal = 1, weak = 2
    # Results could be:
    #   Ideal: => 21
    #   Good: > 11
    #   Risky: > 1
    #   Nope: < 0
    dct_scoring = {
        glb_offense: {
            glb_strong: -20,
            glb_normal: 0,
            glb_weak: 10,
            glb_immune: 20
        },
        glb_defense: {
            glb_immune: -1,
            glb_strong: 0,
            glb_normal: 1,
            glb_weak: 2,
        }
    }

    # A pairint of attributes
    lst_attr = [ ('types', glb_offense), ('moves', glb_defense) ]

    # Let's calculate!!!!
    # Iterate {pokemon: {}}
    for pokemon_key in dct_pokedex:
        running_score = 0
        # Iterate through lst [ (pokemon, target), (pokemon, target) ]
        for poke_attr, target_position in lst_attr:
            # iterate {pokemon: {types:[], moves:{}}}
            for poke_type in dct_pokedex[pokemon_key][poke_attr]:
                # iterate  {attack/defense: {type/combo:{}}}
                for target_type in dct_results[target_position]:
                    # Iterate {attack/defense: {type/combo:{strong: [], weak: [], etc}}}
                    for target_attribute in dct_results[target_position][target_type]:
                        if poke_type in dct_results[target_position][target_type][target_attribute]:
                            running_score += dct_scoring[target_position][target_attribute] 

        # Add the score to the dictionary
        if running_score in dct_tally:
            dct_tally[running_score].append(pokemon_key)
        else:
            dct_tally[running_score] = [ pokemon_key ]

    return dct_tally


def print_pokemon(pokemon_name, dct_pokedex):
    # Print out the list of pokemon and their attribute
    pokemon_name = pokedex_get_key(pokemon_name, dct_pokedex)
    if pokemon_name:
        print(
            '\t' + pokemon_name + ':',
            dct_pokedex[pokemon_name]['nickname'],
            dct_pokedex[pokemon_name]['official'],
            'types' + str(dct_pokedex[pokemon_name]['types']),
            'moves' + str(dct_pokedex[pokemon_name]['moves'])
        )


def print_results(dct_results):
    # output the results
    for position in dct_results:
        for poke_type in dct_results[position]:
            print('\n%7s - %s' % (position.title(), poke_type))    
            for impact in dct_results[position][poke_type]:
                if impact == glb_normal:
                    continue
                if not dct_results[position][poke_type][impact]:
                    continue
                impact_lbl = "%9s" % ('[' + impact + ']')
                print('  ', impact_lbl, ', '.join(dct_results[position][poke_type][impact]))


def print_recommendations(dct_tally):
    # print the recommendations
    print('\nRecommendations:')
    for tally_key in sorted(dct_tally, reverse=True):
        if tally_key > 21:
            print('\t[%d] Ideal: %s' % (tally_key, dct_tally[tally_key]))
        elif tally_key > 11:
            print('\t[%d] Good : %s' % (tally_key, dct_tally[tally_key]))
    print('')


def main():
    # Variables and such
    lst_query_types = []
    pokemon_name = None

    # Parse user arguments
    parser = argparse.ArgumentParser()
    parser.add_argument("dynamic",
                        default=None,
                        metavar='type(s) | unique name', 
                        nargs='*',
                        help='type(s) or name of pokemon, space separated')
    parser.add_argument("--add_types", "-t",
                        default=[],
                        nargs='+',
                        help="add types to the pokemon named, space separated")
    parser.add_argument("--add_moves", "-m",
                        default=[],
                        nargs='+',
                        help="moves by type, space separated")
    parser.add_argument("--add_nickname", "-n",
                        default=None,
                        type=str,
                        help="specify a nickname for the pokemon")
    parser.add_argument("--add_official_name", "-o",
                        default=None,
                        type=str,
                        help="specify the official of the pokemon")
    parser.add_argument("--file", "-f",
                        type=lambda p: Path(p).absolute(),
                        default=Path.home().absolute() / ".pokemon.shelf",
                        required=False,
                        help="specific a shelve file")
    parser.add_argument("--pokedex", "-p",
                        default="pokedex",
                        type=str,
                        required=False,
                        help="save multiple version of pokedex in a single shelve")
    parser.add_argument("--list", "-l",
                        default=False,
                        action='store_true',
                        help="list personal pokemon")
    parser.add_argument("--remove", "-r",
                        default=False,
                        action='store_true',
                        help='remove the named pokemon')
    args = parser.parse_args()

    # Sort dynamic user input
    for item in args.dynamic:
        if validate_type(item):
            lst_query_types.append(str(item))
        else:
            pokemon_name = str(item).split()[0] if not None else None

    # Assign arguments to variables
    lst_add_types = args.add_types
    lst_add_moves = args.add_moves
    shelve_pokedex = args.pokedex
    pokemon_nickname = args.add_nickname
    pokemon_official = args.add_official_name
    do_list = args.list
    do_removal = args.remove

    # shelve doesn't like path objects?
    shelve_file = str(args.file)

    # Load my poke dex
    dct_pokedex = load(shelve_file, shelve_pokedex)

    # Ensure the pokemon_name is defined then find the official entry
    pokemon_name = pokemon_nickname if not pokemon_name else pokemon_name
    pokemon_name = pokemon_official if not pokemon_name else pokemon_name

    # Remove pokemon from pokedex
    if do_removal:
        dct_pokedex = pokemon_remove(
                            pokemon_name, 
                            dct_pokedex,
                            shelve_file,
                            shelve_pokedex
                        )

    # if changes need to be made, make this first
    if pokemon_name and (lst_add_types or lst_add_moves):
        dct_pokedex = pokemon_add(
                            pokemon_name, 
                            pokemon_nickname, 
                            pokemon_official, 
                            lst_add_types, 
                            lst_add_moves, 
                            dct_pokedex,
                            shelve_file,
                            shelve_pokedex
                        )
        print_pokemon(pokemon_name, dct_pokedex)
       
    # Distplay personal pokemon from pokedex
    if do_list and len(dct_pokedex.keys()) > 0:
        if pokemon_name:
            print_pokemon(pokemon_name, dct_pokedex)
        else:
            print('Pokedex %s from %s:' % (shelve_pokedex, shelve_file))
            for name in dct_pokedex:
                print_pokemon(name, dct_pokedex)

    # Combine types aand output
    if len(lst_query_types) > 0:
        dct_results = compute_combination(lst_query_types)
        dct_tally = compute_encounter_score(dct_results, dct_pokedex)
        print_results(dct_results)
        print_recommendations(dct_tally)
    

if __name__ == "__main__":
    main()