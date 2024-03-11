import math
from pynput import keyboard
from IPython.display import clear_output










def get_level(poke_id: int):
    """
    A simple function that converts experience into level.

    Parameters:
        poke_id (int): The id of the pokemon you're getting the level for.
    """
    experience = poke_id [0]
    current_level = math.floor (experience**(1/3))
    print(current_level)
    return current_level
# get_level(poke_id=[])

def exp_gain(opponent_exp):
    experience_gain = math.ceil (opponent_exp/7)
    return experience_gain




master_id = 0
master_poke_dict = {}
def make_poke_id(poke_name, poke_moves, poke_exp):
    global master_id
    master_id +=1
    master_poke_dict[master_id] = {"name": poke_name, "exp": poke_exp, "moves": poke_moves, }









open_field = " _ "
wall = " X "

'''
The function, "coordinate_field" creates a grid like the one below, 
and also prints the location and movement of characters within the 
grid as the code runs. In future iterations, I intend to make the 
walls impassable, add momentum and battle functionality.

 X  X  X  X  X  X  X  X  X  X  X  X 
 X  _  _  _  _  _  _  _  _  _  _  X 
 X  _  _  _  _  _  _  _  _  _  _  X 
 X  _  _  _  _  _  _  _  _  _  _  X 
 X  _  _  _  _  _  _  _  _  _  _  X 
 X  _  _  _  _  _  _  _  _  _  _  X 
 X  _  _  _  _  _  _  _  _  _  _  X 
 X  _  _  _  _  _  _  _  _  _  _  X 
 X  _  _  _  _  _  _  _  _  _  _  X 
 X  _  _  _  _  _  _  _  _  _  _  X 
 X  _  _  _  _  _  _  _  _  _  _  X 
 X  X  X  X  X  X  X  X  X  X  X  X 
'''
def coordinate_field (p1_location, p2_location, p1_direction, p2_direction):
    x_coordinate = 0
    y_coordinate = 1
    field = ""
    ''' 
    The grid is 12*12.
    156 is 12*12+12 because adding each line break takes an
    iteration as well.
    '''
    for _ in range(156):
        x_coordinate += 1
        coordinate_point = [x_coordinate, y_coordinate]
        if x_coordinate > 12:
            field += "\n"
            x_coordinate -= 13
            y_coordinate += 1
        elif y_coordinate in [1,12] or x_coordinate in [1,12]:
            field += wall
        # The following elifs add the characters.
        elif coordinate_point == p1_location:
            field += p1_direction
        elif coordinate_point == p2_location:
            field += p2_direction
        else:
            field += open_field
    clear_output(wait=True)
    print(field)

p1_location = [4, 7]

'''
This following list will be joined before going in to the
function.
I think that it needs to be a list at this stage because 
p1_direction += "<" and such didn't seem to work in this context.
'''
p1_direction = ["-","-","-"]

def on_press(key):
    try:
        if key == keyboard.Key.enter:
            return False  # Stop listener
        elif key == keyboard.Key.left:
            p1_direction.append("<")
        elif key == keyboard.Key.right:
            p1_direction.append(">")
        elif key == keyboard.Key.up:
            p1_direction.append("^")
        elif key == keyboard.Key.down:
            p1_direction.append("v")
    except AttributeError:
        pass

move_dict = {
    "^": (1, -1, 1),
    "v": (1, 1, -1),
    "<": (0, -1, 1),
    ">": (0, 1, -1)
}

def movement (p1_direction):
    print ("Type three moves: ")

    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()

    # This loop guarantees that only the last three directional
    # inputs are counted.
    while len(p1_direction) > 3:
        p1_direction.remove(p1_direction[0])
    
    # This translates the inputs into motion.
    for i in range(len(p1_direction)):
        if p1_direction[i] in move_dict:
            p1_location[move_dict[p1_direction[i]][0]] += move_dict[p1_direction[i]][1]

        # Players can't go past the walls.
        if p1_location [0] > 11:
            p1_location [0] = 11
        if p1_location [0] < 2:
            p1_location [0] = 2
        if p1_location [1] > 11:
            p1_location [1] = 11
        if p1_location [1] < 2:
            p1_location [1] = 2
        

    # Finally, the list is joined, used as an argument in the 
    # coordinate_field function, and separated again.
    p1_direction = "".join(p1_direction)
    coordinate_field (p1_location, [7,5], p1_direction, "^^<")
    p1_direction = list(p1_direction)
    return p1_direction

# This function will someday be part of a larger game, but for
# now, I run it endlessly to test it.
# while True:
#     p1_direction = movement(p1_direction)

"12"

'''
 X  X  X  X  X  X  X  X  X  X  X  X 
 X  _  _  _  _  _  _  _  _  _  _  X 
 X  _  _  _  _  _  _  _  _  _  _  X 
 X  _  _  _  _  _  _  _  _  _  _  X 
 X  _  _  _  _  _  _  _  _  _  _  X 
 X  _  _  _  _  _  _  _  _  _  _  X 
 X  _  _  _  _  _  _  _  _  _  _  X 
 X  _  _  _  _  _  _  _  _  _  _  X 
 X  _  _  _  _  _  _  _  _  _  _  X 
 X  _  _  _  _  _  _  _  _  _  _  X 
 X  _  _  _  _  _  _  _  _  _  _  X 
 X  X  X  X  X  X  X  X  X  X  X  X 






 
 



 '''

class Pokemon:
    def __init__ (self, type1, type2, base_experience, height, weight, health, attack, defence, speed, special):
        self.name = self
        self.base_experience = base_experience
        self.type1 = type1
        self.type2 = type2
        self.height = height
        self.weight = weight

    # Base Stats
        self.base_health = health
        self.base_attack = attack
        self.base_defence = defence
        self.base_speed = speed

        # This game uses first gen statistics, including 'Special'.
        # Special takes the place of both special attack and special defense.
        self.base_special = special

class Bulbasaur(Pokemon):
    def __init__ (self):
        self.stats = Pokemon("Bulbasaur", 'grass', 'poison', 64, '2\'4\"', 15.0, 45, 49, 49, 45, 65)
    def your_bulbasaur_stats (self, experience):
        ''

pokemon_dict = {
    "Bulbasaur": {
        'types': ["grass", "poison"],
        'category': "Seed",
        'height': "2' 4\"",
        'weight': "15.0 lb",
        'catch_rate': "45 (6.0%)",
        'base_exp': 64,
        'exp_group': "Medium Slow",
        'evolves': {'level': 16, 'into': 'Ivysaur'},
        'base_stats': {"HP": 45, "Attack": 49, "Defense": 49, "Speed": 45, "Special": 65},
        'critical_hit_chance': "8.6%",
        'pokedex_entries': ["Red/Blue: A strange seed was planted on its back at birth. The plant sprouts and grows with this POKéMON.",
                        "Yellow: It can go for days without eating a single morsel. In the bulb on its back, it stores energy."],
        'level_up_learnset': {
            1: "Tackle",
            1: "Growl",
            7: "Leech Seed",
            13: "Vine Whip",
            20: "PoisonPowder",
            27: "Razor Leaf",
            34: "Growth",
            41: "Sleep Powder",
            48: "SolarBeam"
        },
        'tm_hm_learnset': {
            "TM03": "Swords Dance",
            "TM06": "Toxic",
            "TM08": "Body Slam",
            "TM09": "Take Down",
            "TM10": "Double-Edge",
            "TM20": "Rage",
            "TM21": "Mega Drain",
            "TM22": "SolarBeam",
            "TM31": "Mimic",
            "TM32": "Double Team",
            "TM33": "Reflect",
            "TM34": "Bide",
            "TM44": "Rest",
            "TM50": "Substitute",
            "HM01": "Cut"
        }
    
    }
}
