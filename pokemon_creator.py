

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
from poke_move_dict import *

class Pokemon:
    def __init__ (self, species, name, pid, types, base_experience, health, attack, defence, speed, special, moves, level):
        self.pid = pid
        self.species = species
        self.name = name
        self.base_exp = base_experience
        self.types = types

    # Base Stats
        self.base_stats = {'health': health,
                           'attack': attack,
                           'defence': defence,
                           'speed': speed,
                            # This game uses first gen statistics, including 'Special'.
                            # Special takes the place of both special attack and special defense.
                           'special': special}

        # The parameter for moves is a dictionary.
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
        health = self.base_stats['health']
        attack = self.base_stats['attack']
        defence = self.base_stats['defence']
        speed = self.base_stats['speed']
        special = self.base_stats['special']

        # Again, thanks to 
        # https://gamefaqs.gamespot.com/gameboy/367023-pokemon-red-version/faqs/64175/stat-determination
        # for these formulas.
        self.level = math.floor (self.experience**(1/3))
        self.current_health = floor((health + iv['health']) * 2 + floor(ceil(sqrt(self.ev)) / 4) * self.level / 100) + self.level + 10 
        self.current_attack = floor((attack + iv['attack']) * 2 + floor(ceil(sqrt(self.ev)) / 4) * self.level / 100) + 5
        self.current_defence = floor((defence + iv['defence']) * 2 + floor(ceil(sqrt(self.ev)) / 4) * self.level / 100) + 5
        self.current_speed = floor((speed + iv['speed']) * 2 + floor(ceil(sqrt(self.ev)) / 4) * self.level / 100) + 5
        self.current_special = floor((special + iv['special']) * 2 + floor(ceil(sqrt(self.ev)) / 4) * self.level / 100) + 5

    
    def rename(self, new_name):
        self.name = new_name

    def species_entry(self):
        '''
        This function returns all the stats of your Pokemon in a readable format.
        The only parameter is your Pokemon's PID, although at the time of making this function I
            haven't come up with a great way to find that after the PID iteration in pokemon_caught() 
            has moved on...so we'll see if I stick with "caught_id" as the parameter name or not.
        
        '''
        pokemon = pokemon_dict[self.name]
        print(f"\n{self.name.upper()}:")
        for key in pokemon:
            
            print()

            # The pokemon_dict() keys have underscores instead of spaces so voila! Underscore remover.
            for letter in key.title():
                if letter != "_":
                    print(letter, end='')
                else:
                    print(" ", end='')

            print(':')

            if type(pokemon[key]) in [list, dict]:
                # I don't name 'i' because it could be another key, or an item.
                for i in pokemon[key]:
                    
                    # I needed a 'try' here because lists don't take strings as keys and throw a hissy fit.
                    try:
                        if type(pokemon[key][i]) in [list, dict]:
                            for move in pokemon[key][i]:
                                print(f"\t{move} at level {i}")
                        else:
                            print(f"\t{i} {pokemon[key][i]}")
                    except:
                        try:
                            print("\t"+i.title())
                        except:
                            print("\t"+i)
                    
            else:
                print("\t"+str(pokemon[key]))
        print()


    def personal_entry(self):
        for key in vars(self):
            if key in pokemon_dict[self.name].keys() or key.lower() in ['pid', 'moves']:
                continue
            print()
            for letter in key.title():
                if letter != "_":
                    print(letter, end='')
                else:
                    print(" ", end='')
            print(':')
            if type(getattr(self, key)) is list:
                for i in getattr(self, key).keys():
                    print(f"\t{i}: {getattr(self, key)[i]}")
            elif type(getattr(self, key)) is dict:
                for i in getattr(self, key):
                    print(f"\t{i}:",end='')
                    
                    # if type(getattr(self, key)[i]) is dict:
                    #     for j in getattr(self, key)[i].keys():
                    #         print(f"\n\t\t{j}: {getattr(self, key)[i][j]}")
                    #         # for k in getattr(self, key)[i][j]:
                    #         #     print(f"\t\t{k}: {getattr(self, key)[i][j]}")
                    # else:
                    print(f" {getattr(self, key)[i]}")
            else:
                print(f"\t{getattr(self, key)}")

    def generic_entry(self, tabs, value):
        if isinstance(value, dict):
            ''
        

    def moves_entry(self):
        for key in vars(self):
            if type(getattr(self, key)) is dict and getattr(self, key) in poke_move_dict.keys:
                for i in getattr(self, key):
                    print(f"{i}:")
                    if type(getattr(self, key)[i]) is dict:
                        for j in getattr(self, key)[i].keys():
                            print(f"\t{j}: {getattr(self, key)[i][j]}")
    
                    




def create_pokemon(species, level, pid, caught_pokemon_dict):
    species = species.title()
    
    
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
    moves = {}
    for move_key in pokemon_dict[species]['level_up_learnset'].keys():
        # Appends the four highest level moves to the Pokemon's moveset.
        if move_key < level:
            for move in pokemon_dict[species]['level_up_learnset'][move_key]:
                # Some Pokemon learn the same move twice, but I don't want duplicates in a moveset.
                # For now, I'm removing all powerless moves, because they don't work yet.
                if move not in moves and poke_move_dict[move]['Power'] not in ['N/A', 'Var Dmg']:
                    moves[move] = poke_move_dict[move]
                    
                    # print(move)
        # Limits the number of moves to four.
        if len(moves) > 4:
            for i in moves:
                moves.pop(i)
                break
        
        
        
    

    # Creates the Pokemon using the Pokemon class, but only attributing the species' constant stats that
    # are necessary for stat calculation.
    caught_pokemon_dict[pid] = Pokemon (species, species, pid, pokemon_dict[species]['types'], pokemon_dict[species]['base_exp'], pokemon_dict[species]['base_stats']['HP'], pokemon_dict[species]['base_stats']['Attack'], pokemon_dict[species]['base_stats']['Defense'], pokemon_dict[species]['base_stats']['Speed'], pokemon_dict[species]['base_stats']['Special'], moves, level)
    caught_pokemon_dict[pid].calculate_stats()
    return caught_pokemon_dict



def pid_caught_pokemon_dict_initializer():

    global caught_pokemon_dict
    caught_pokemon_dict = {}

    # See the create_pokemon function for an explanation of pid.
    global pid
    pid = 0
    return pid



if __name__ == '__main__':
    pid_caught_pokemon_dict_initializer()