

# def get_level(poke_id: int):
#     """
#     A simple function that converts experience into level.

#     Parameters:
#         poke_id (int): The id of the pokemon you're getting the level for.
#     """
#     experience = poke_id [0]
#     current_level = math.floor (experience**(1/3))
#     print(current_level)
#     return current_level
# # get_level(poke_id=[])

# def exp_gain(opponent_exp):
#     experience_gain = math.ceil (opponent_exp/7)
#     return experience_gain




# master_id = 0
# master_poke_dict = {}
# def make_poke_id(poke_name, poke_moves, poke_exp):
#     global master_id
#     master_id +=1
#     master_poke_dict[master_id] = {"name": poke_name, "exp": poke_exp, "moves": poke_moves, }

import math
from math import *
from pokemon_dict import *
import random

class Pokemon:
    def __init__ (self, pid, name, types, base_experience, health, attack, defence, speed, special, moves, level):
        self.pid = pid
        self.name = name
        self.base_experience = base_experience
        self.types = types

    # Base Stats
        self.base_health = health
        self.base_attack = attack
        self.base_defence = defence
        self.base_speed = speed

        # This game uses first gen statistics, including 'Special'.
        # Special takes the place of both special attack and special defense.
        self.base_special = special

        self.moves = moves

        # The formulas for IV calculation, as well as for the calculate_stats function are from this 
        # website: 
        # https://gamefaqs.gamespot.com/gameboy/367023-pokemon-red-version/faqs/64175/stat-determination
        self.iv = {
            'health': random.randint(0,15),
            'attack': random.randint(0,15),
            'defence': random.randint(0,15),
            'speed': random.randint(0,15),
            'special': random.randint(0,15)
        }

        self.ev = 0
        self.level = level

        # I'm adding a plus one for now, because for some unfathomable reason, not doing so causes 
        # the level to return as lower than it was whenever calculate_stats is called.
        experience = level**3 + 1
        self.experience = experience
        

    def calculate_stats(self):
        iv = self.iv
        health = self.base_health
        attack = self.base_attack
        defence = self.base_defence
        speed = self.base_speed
        special = self.base_special

        # Again, thanks to 
        # https://gamefaqs.gamespot.com/gameboy/367023-pokemon-red-version/faqs/64175/stat-determination
        # for these formulas.
        level = math.floor (self.experience**(1/3))
        current_health = floor((health + iv['health']) * 2 + floor(ceil(sqrt(self.ev)) / 4) * level / 100) + level + 10 
        current_attack = floor((attack + iv['attack']) * 2 + floor(ceil(sqrt(self.ev)) / 4) * level / 100) + 5
        current_defence = floor((defence + iv['defence']) * 2 + floor(ceil(sqrt(self.ev)) / 4) * level / 100) + 5
        current_speed = floor((speed + iv['speed']) * 2 + floor(ceil(sqrt(self.ev)) / 4) * level / 100) + 5
        current_special = floor((special + iv['special']) * 2 + floor(ceil(sqrt(self.ev)) / 4) * level / 100) + 5

        
        return {
            'level': level,
            'health': current_health,
            'attack': current_attack,
            'defence': current_defence,
            'speed': current_speed,
            'special': current_special
        }
    
    def rename(self, new_name):
        self.name = new_name


def create_pokemon(species, level, pid):

    global caught_pokemon_dict
    
    '''
    This 'pid' stands for 'Pokemon ID' and is incremented every time a pokemon is created.
    The pid variable is used to append to the dictionary, but is not returned.
    The pid is only permanently incremented when a Pokemon is caught, so that knocked-
    out wild Pokemon are not recorded; the spot in the dictionary will be replaced by
    this function whenever a new Pokemon is encountered until the pid permanently changes.
    '''
    pid += 1

    '''
    I imitate the Pokemon games' collection of moves here, giving new Pokemon the most advanced 
    moves that they could have learned up to this point. 
    I will make a relearning option that is much more convenient that in the Pokemon games,
    and I might allow the learning of more than four moves.
    The following code appends the names of every move below the given level in ascending order,
    popping the first index every time the list grows longer than four items.
    '''
    moves = []
    for move_key in pokemon_dict[species]['level_up_learnset'].keys():
        # Appends the four highest level moves to the Pokemon's moveset.
        if move_key < level:
            for move in pokemon_dict[species]['level_up_learnset'][move_key]:
                # Some Pokemon learn the same move twice, but I don't want duplicates in a moveset.
                if move not in moves:
                    moves.append(move)
        # Limits the number of moves to four.
        if len(moves) > 4:
            moves.pop(0)
    

    # Creates the Pokemon using the Pokemon class, but only attributing the species' constant stats that
    # are necessary for stat calculation.
    caught_pokemon_dict[pid] = Pokemon (species, pid, pokemon_dict[species]['types'], pokemon_dict[species]['base_exp'], pokemon_dict[species]['base_stats']['HP'], pokemon_dict[species]['base_stats']['Attack'], pokemon_dict[species]['base_stats']['Defense'], pokemon_dict[species]['base_stats']['Speed'], pokemon_dict[species]['base_stats']['Special'], moves, level)
    return caught_pokemon_dict[pid]

def main():
    
    global caught_pokemon_dict
    caught_pokemon_dict = {}

    # See the create_pokemon function for an explanation of pid.
    pid = 0

    create_pokemon('Bulbasaur', 5, pid)
    print(caught_pokemon_dict[pid].calculate_stats())
    print(caught_pokemon_dict[pid])

if __name__ == '__main__':
    main()