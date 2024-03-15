

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
    def __init__ (self, pid, name, types, base_experience, health, attack, defence, speed, special):
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

        # The formulas for IV calculation, as well as for the calculate_stats function are from this website: https://gamefaqs.gamespot.com/gameboy/367023-pokemon-red-version/faqs/64175/stat-determination
        self.iv = {
            'health': random.randint(0,15),
            'attack': random.randint(0,15),
            'defence': random.randint(0,15),
            'speed': random.randint(0,15),
            'special': random.randint(0,15)
        }
        

    def calculate_stats(self, experience, ev):
        iv = self.iv
        health = self.base_health
        attack = self.base_attack
        defence = self.base_defence
        speed = self.base_speed
        special = self.base_special
        level = math.floor (experience**(1/3))
        current_health = floor((health + iv['health']) * 2 + floor(ceil(sqrt(ev)) / 4) * level / 100) + level + 10 
        current_attack = floor((attack + iv['attack']) * 2 + floor(ceil(sqrt(ev)) / 4) * level / 100) + 5
        current_defence = floor((defence + iv['defence']) * 2 + floor(ceil(sqrt(ev)) / 4) * level / 100) + 5
        current_speed = floor((speed + iv['speed']) * 2 + floor(ceil(sqrt(ev)) / 4) * level / 100) + 5
        current_special = floor((special + iv['special']) * 2 + floor(ceil(sqrt(ev)) / 4) * level / 100) + 5

        
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




def create_pokemon(species, level):
    global pid
    pid += 1
    global existing_pokemon_dict
    existing_pokemon_dict[pid] = Pokemon (species, pid, pokemon_dict[species]['types'], pokemon_dict[species]['base_exp'], pokemon_dict[species]['base_stats']['HP'], pokemon_dict[species]['base_stats']['Attack'], pokemon_dict[species]['base_stats']['Defense'], pokemon_dict[species]['base_stats']['Speed'], pokemon_dict[species]['base_stats']['Special'])
    return 

def main():
    existing_pokemon_dict = {}
    pid = 0
    bulby = Bulbasaur(1)
    bulby_stats = bulby.calculate_stats(5**3+1, 0)
    print(bulby_stats)

    create_pokemon('Bulbasaur', 5)
    print(existing_pokemon_dict[pid].calculate_stats(5**3+1, 0))

if __name__ == '__main__':
    main()