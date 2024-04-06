
def get_category(player, opponent, move_name):
    if poke_move_dict[move_name]['Category'] == 'Physical':
        attack_stat = player.current_attack
        defense_stat = opponent.current_defence
    elif poke_move_dict[move_name]['Category'] == 'Special':
        attack_stat = player.current_special
        defense_stat = opponent.current_special
    else:
        attack_stat = 0
        defense_stat = 0
    return [attack_stat, defense_stat]

class move:
    def __init__ (self, name):
        self.name = name
        dict_entry = poke_move_dict[self.name]
        self.damage = dict_entry['Power']
        self.type = dict_entry['Type']
        self.accuracy = dict_entry['Accuracy']
        self.category = dict_entry['Category']
        self.pp = dict_entry['PP']


poke_move_dict = {
    "Absorb": {
        "Effect": "Restores the user's HP by 1/2 of the damage inflicted on the target.",
        "Type": "Grass",
        "PP": 20,
        "Power": 20,
        "Accuracy": "100%",
        "Category": "Special"
    },
    "Acid": {
        "Effect": "Has a ~10% chance to lower the target's Defense by 1 stage.",
        "Type": "Poison",
        "PP": 30,
        "Power": 40,
        "Accuracy": "100%",
        "Category": "Special"
    },
    "Acid Armor": {
        "Effect": "Raises the user's Defense by 2 stages.",
        "Type": "Poison",
        "PP": 40,
        "Power": "N/A",
        "Accuracy": "N/A",
        "Category": "Status"
    },
    "Agility": {
        "Effect": "Raises the user's Speed by 2 stages.",
        "Type": "Psychic",
        "PP": 30,
        "Power": "N/A",
        "Accuracy": "N/A",
        "Category": "Status"
    },
    "Amnesia": {
        "Effect": "Raises the user's Special by 2 stages.",
        "Type": "Psychic",
        "PP": 20,
        "Power": "N/A",
        "Accuracy": "N/A",
        "Category": "Status"
    },
    "Aurora Beam": {
        "Effect": "Has a ~10% chance to lower the target's Attack by 1 stage.",
        "Type": "Ice",
        "PP": 20,
        "Power": 65,
        "Accuracy": "100%",
        "Category": "Special"
    },
    "Barrage": {
        "Effect": "Attacks 2-5 times in one turn; if one of these attacks breaks a target's Substitute, the target will take damage for the rest of the hits. This move has a 3/8 chance to hit twice, a 3/8 chance to hit three times, a 1/8 chance to hit four times and a 1/8 chance to hit five times.",
        "Type": "Normal",
        "PP": 20,
        "Power": 15,
        "Accuracy": "85%",
        "Category": "Physical"
    },
    "Barrier": {
        "Effect": "Raises the user's Defense by 2 stages.",
        "Type": "Psychic",
        "PP": 30,
        "Power": "N/A",
        "Accuracy": "N/A",
        "Category": "Status"
    },
    "Bide": {
        "Effect": "The user absorbs all damage for 2-3 turns and then inflicts twice the absorbed damage on its target. This move ignores the target's type but still cannot hit Ghost-type Pokemon.",
        "Type": "Normal",
        "PP": 10,
        "Power": "Var Dmg",
        "Accuracy": "100%",
        "Category": "Physical"
    },
    "Bind": {
        "Effect": "The user becomes uncontrollable and attacks for 2-5 consecutive turns; the target cannot make attacks of its own during this time, but it may switch out, use items or run away.",
        "Type": "Normal",
        "PP": 20,
        "Power": 15,
        "Accuracy": "75%",
        "Category": "Physical"
    },
    "Bite": {
        "Effect": "Has a ~10% chance to make the target flinch.",
        "Type": "Normal",
        "PP": 25,
        "Power": 60,
        "Accuracy": "100%",
        "Category": "Physical"
    },
    "Blizzard": {
        "Effect": "Has a ~10% chance to freeze the target.",
        "Type": "Ice",
        "PP": 5,
        "Power": 120,
        "Accuracy": "90%",
        "Category": "Special"
    },
    "Body Slam": {
        "Effect": "Has a ~30% chance to paralyze the target.",
        "Type": "Normal",
        "PP": 15,
        "Power": 85,
        "Accuracy": "100%",
        "Category": "Physical"
    },
    "Bone Club": {
        "Effect": "Has a ~10% chance to make the target flinch.",
        "Type": "Ground",
        "PP": 20,
        "Power": 65,
        "Accuracy": "85%",
        "Category": "Physical"
    },
    "Bonemerang": {
        "Effect": "Strikes twice; if the first hit breaks the target's Substitute, the real Pokemon will take damage from the second hit.",
        "Type": "Ground",
        "PP": 10,
        "Power": 50,
        "Accuracy": "90%",
        "Category": "Physical"
    },
    "Bubble": {
        "Effect": "Has a ~10% chance to lower the target's Speed by 1 stage.",
        "Type": "Water",
        "PP": 30,
        "Power": 20,
        "Accuracy": "100%",
        "Category": "Special"
    },
    "Bubblebeam": {
        "Effect": "Has a ~10% chance to lower the target's Speed by 1 stage.",
        "Type": "Water",
        "PP": 20,
        "Power": 65,
        "Accuracy": "100%",
        "Category": "Special"
    },
    "Clamp": {
        "Effect": "The user becomes uncontrollable and attacks for 2-5 consecutive turns; the target cannot make attacks of its own during this time, but it may switch out, use items or run away.",
        "Type": "Water",
        "PP": 10,
        "Power": 35,
        "Accuracy": "75%",
        "Category": "Physical"
    },
    "Comet Punch": {
        "Effect": "Attacks 2-5 times in one turn; if one of these attacks breaks a target's Substitute, the target will take damage for the rest of the hits. This move has a 3/8 chance to hit twice, a 3/8 chance to hit three times, a 1/8 chance to hit four times and a 1/8 chance to hit five times.",
        "Type": "Normal",
        "PP": 15,
        "Power": 18,
        "Accuracy": "85%",
        "Category": "Physical"
    },
    "Confuse Ray": {
        "Effect": "Confuses the target.",
        "Type": "Ghost",
        "PP": 10,
        "Power": "N/A",
        "Accuracy": "100%",
        "Category": "Status"
    },
    "Confusion": {
        "Effect": "Has a ~10% chance to confuse the target.",
        "Type": "Psychic",
        "PP": 25,
        "Power": 50,
        "Accuracy": "100%",
        "Category": "Special"
    },
    "Constrict": {
        "Effect": "Has a ~10% chance to lower the target's Speed by 1 stage.",
        "Type": "Normal",
        "PP": 35,
        "Power": 10,
        "Accuracy": "100%",
        "Category": "Physical"
    },
    "Conversion": {
        "Effect": "The user's type changes to match the type of one of its four attacks. This move fails if the user cannot change its type under this condition.",
        "Type": "Normal",
        "PP": 30,
        "Power": "N/A",
        "Accuracy": "N/A",
        "Category": "Status"
    },
    "Counter": {
        "Effect": "Almost always goes last; if an opponent strikes with a Normal- or Fighting-type attack before the user's turn, the user retaliates for twice the damage it had endured.",
        "Type": "Fighting",
        "PP": 20,
        "Power": "Var Dmg",
        "Accuracy": "100%",
        "Category": "Physical"
    },
    "Crabhammer": {
        "Effect": "Has a high critical hit ratio.",
        "Type": "Water",
        "PP": 10,
        "Power": 90,
        "Accuracy": "85%",
        "Category": "Physical"
    },
    "Cut": {
        "Effect": "Damages the target.",
        "Type": "Normal",
        "PP": 30,
        "Power": 50,
        "Accuracy": "95%",
        "Category": "Physical"
    },
    "Defense Curl": {
        "Effect": "Raises the user's Defense by 1 stage.",
        "Type": "Normal",
        "PP": 40,
        "Power": "N/A",
        "Accuracy": "N/A",
        "Category": "Status"
    },
    "Dig": {
        "Effect": "On the first turn, the user digs underground, becoming uncontrollable, and evades all attacks. Swift may still hit a Pokemon underground. On the second turn, the user attacks.",
        "Type": "Ground",
        "PP": 10,
        "Power": 100,
        "Accuracy": "100%",
        "Category": "Physical"
    },
    "Disable": {
        "Effect": "One randomly selected move of the target's cannot be selected for 1-7 turns. Disable only works on one move at a time. The target does nothing if it is about to use a move that becomes disabled.",
        "Type": "Normal",
        "PP": 20,
        "Power": "N/A",
        "Accuracy": "55%",
        "Category": "Status"
    },
    "Dizzy Punch": {
        "Effect": "Damages the target.",
        "Type": "Normal",
        "PP": 10,
        "Power": 70,
        "Accuracy": "100%",
        "Category": "Physical"
    },
    "Double Kick": {
        "Effect": "Strikes twice; if the first hit breaks the target's Substitute, the real Pokemon will take damage from the second hit.",
        "Type": "Fighting",
        "PP": 30,
        "Power": 30,
        "Accuracy": "100%",
        "Category": "Physical"
    },
    "Double Team": {
        "Effect": "Raises the user's Evasion by 1 stage.",
        "Type": "Normal",
        "PP": 15,
        "Power": "N/A",
        "Accuracy": "N/A",
        "Category": "Status"
    },
    "Double-edge": {
        "Effect": "The user receives 1/4 recoil damage.",
        "Type": "Normal",
        "PP": 15,
        "Power": 100,
        "Accuracy": "100%",
        "Category": "Physical"
    },
    "Doubleslap": {
        "Effect": "Attacks 2-5 times in one turn; if one of these attacks breaks a target's Substitute, the target will take damage for the rest of the hits. This move has a 3/8 chance to hit twice, a 3/8 chance to hit three times, a 1/8 chance to hit four times and a 1/8 chance to hit five times.",
        "Type": "Normal",
        "PP": 10,
        "Power": 15,
        "Accuracy": "85%",
        "Category": "Physical"
    },
    "Dragon Rage": {
        "Effect": "Always deals 40 points of damage.",
        "Type": "Dragon",
        "PP": 10,
        "Power": "Set",
        "Accuracy": "100%",
        "Category": "Special"
    },
    "Dream Eater": {
        "Effect": "Restores the user's HP by 1/2 of the damage inflicted on the target but only works on a sleeping target.",
        "Type": "Psychic",
        "PP": 15,
        "Power": 100,
        "Accuracy": "100%",
        "Category": "Special"
    },
    "Drill Peck": {
        "Effect": "Damages the target.",
        "Type": "Flying",
        "PP": 20,
        "Power": 80,
        "Accuracy": "100%",
        "Category": "Physical"
    },
    "Earthquake": {
        "Effect": "Damages the target.",
        "Type": "Ground",
        "PP": 10,
        "Power": 100,
        "Accuracy": "100%",
        "Category": "Physical"
    },
    "Egg Bomb": {
        "Effect": "Damages the target.",
        "Type": "Normal",
        "PP": 10,
        "Power": 100,
        "Accuracy": "75%",
        "Category": "Physical"
    },
    "Ember": {
        "Effect": "Has a ~10% chance to burn the target.",
        "Type": "Fire",
        "PP": 25,
        "Power": 40,
        "Accuracy": "100%",
        "Category": "Special"
    },
    "Explosion": {
        "Effect": "The Defense stat of other Pokemon is halved against this attack, essentially doubling the move's base power; causes the user to faint.",
        "Type": "Normal",
        "PP": 5,
        "Power": 170,
        "Accuracy": "100%",
        "Category": "Physical"
    },
    "Fire Blast": {
        "Effect": "Has a ~30% chance to burn the target.",
        "Type": "Fire",
        "PP": 5,
        "Power": 120,
        "Accuracy": "85%",
        "Category": "Special"
    },
    "Fire Punch": {
        "Effect": "Has a ~10% chance to burn the target.",
        "Type": "Fire",
        "PP": 15,
        "Power": 75,
        "Accuracy": "100%",
        "Category": "Physical"
    },
    "Fire Spin": {
        "Effect": "The user becomes uncontrollable and attacks for 2-5 consecutive turns; the target cannot make attacks of its own during this time, but it may switch out, use items or run away.",
        "Type": "Fire",
        "PP": 15,
        "Power": 15,
        "Accuracy": "70%",
        "Category": "Special"
    },
    "Fissure": {
        "Effect": "The target faints; doesn't work on faster or higher-leveled Pokemon.",
        "Type": "Ground",
        "PP": 5,
        "Power": "KO",
        "Accuracy": "30%",
        "Category": "Physical"
    },
    "Flamethrower": {
        "Effect": "Has a ~10% chance to burn the target.",
        "Type": "Fire",
        "PP": 15,
        "Power": 95,
        "Accuracy": "100%",
        "Category": "Special"
    },
    "Flash": {
        "Effect": "Lowers the target's Accuracy by 1 stage.",
        "Type": "Normal",
        "PP": 20,
        "Power": "N/A",
        "Accuracy": "70%",
        "Category": "Status"
    },
    "Fly": {
        "Effect": "On the first turn, the user flies into the air, becoming uncontrollable, and evades most attacks. Swift may still hit a Pokemon in the air. On the second turn, the user attacks.",
        "Type": "Flying",
        "PP": 15,
        "Power": 70,
        "Accuracy": "95%",
        "Category": "Physical"
    },
    "Focus Energy": {
        "Effect": "Decreases critical hit ratio in-game, but raises it in Pokemon Stadium.",
        "Type": "Normal",
        "PP": 30,
        "Power": "N/A",
        "Accuracy": "N/A",
        "Category": "Status"
    },
    "Fury Attack": {
        "Effect": "Attacks 2-5 times in one turn; if one of these attacks breaks a target's Substitute, the target will take damage for the rest of the hits. This move has a 3/8 chance to hit twice, a 3/8 chance to hit three times, a 1/8 chance to hit four times and a 1/8 chance to hit five times.",
        "Type": "Normal",
        "PP": 20,
        "Power": 15,
        "Accuracy": "85%",
        "Category": "Physical"
    },
    "Fury Swipes": {
        "Effect": "Attacks 2-5 times in one turn; if one of these attacks breaks a target's Substitute, the target will take damage for the rest of the hits. This move has a 3/8 chance to hit twice, a 3/8 chance to hit three times, a 1/8 chance to hit four times and a 1/8 chance to hit five times.",
        "Type": "Normal",
        "PP": 15,
        "Power": 10,
        "Accuracy": "80%",
        "Category": "Physical"
    },
    "Glare": {
        "Effect": "Paralyzes the target. This move works on Ghost-type Pokemon.",
        "Type": "Normal",
        "PP": 30,
        "Power": "N/A",
        "Accuracy": "75%",
        "Category": "Status"
    },
    "Growl": {
        "Effect": "Lowers the target's Attack by 1 stage.",
        "Type": "Normal",
        "PP": 40,
        "Power": "N/A",
        "Accuracy": "100%",
        "Category": "Status"
    },
    "Growth": {
        "Effect": "Raises the user's Special by 1 stage.",
        "Type": "Normal",
        "PP": 40,
        "Power": "N/A",
        "Accuracy": "N/A",
        "Category": "Status"
    },
    "Guillotine": {
        "Effect": "The target faints; doesn't work on faster or higher-leveled Pokemon.",
        "Type": "Normal",
        "PP": 5,
        "Power": "KO",
        "Accuracy": "30%",
        "Category": "Physical"
    },
    "Gust": {
        "Effect": "Damages the target.",
        "Type": "Normal",
        "PP": 35,
        "Power": 40,
        "Accuracy": "100%",
        "Category": "Special"
    },
    "Harden": {
        "Effect": "Raises the user's Defense by 1 stage.",
        "Type": "Normal",
        "PP": 30,
        "Power": "N/A",
        "Accuracy": "N/A",
        "Category": "Status"
    },
    "Haze": {
        "Effect": "Eliminates any stat modifiers from all active Pokemon. Also removes Leech Seed, Reflect and Light Screen from either Pokemon and cures the opponent of any status conditions (including Toxic). If the user of Haze has Toxic poisoning, it will be downgraded to regular poisoning.",
        "Type": "Ice",
        "PP": 30,
        "Power": "N/A",
        "Accuracy": "N/A",
        "Category": "Status"
    },
    "Headbutt": {
        "Effect": "Has a ~30% chance to make the target flinch.",
        "Type": "Normal",
        "PP": 15,
        "Power": 70,
        "Accuracy": "100%",
        "Category": "Physical"
    },
    "Hi Jump Kick": {
        "Effect": "If this attack misses the target, the user receives 1 HP of damage.",
        "Type": "Fighting",
        "PP": 20,
        "Power": 85,
        "Accuracy": "90%",
        "Category": "Physical"
    },
    "Horn Attack": {
        "Effect": "Damages the target.",
        "Type": "Normal",
        "PP": 25,
        "Power": 65,
        "Accuracy": "100%",
        "Category": "Physical"
    },
    "Horn Drill": {
        "Effect": "The target faints; doesn't work on faster or higher-leveled Pokemon.",
        "Type": "Normal",
        "PP": 5,
        "Power": "KO",
        "Accuracy": "30%",
        "Category": "Physical"
    },
    "Hydro Pump": {
        "Effect": "Damages the target.",
        "Type": "Water",
        "PP": 5,
        "Power": 120,
        "Accuracy": "80%",
        "Category": "Special"
    },
    "Hyper Beam": {
        "Effect": "In Stadium, the user becomes uncontrollable during its next turn. Otherwise, the user attacks on turn one but it doesn't recharge on turn two if it KOs the target, breaks its Substitute or misses entirely.",
        "Type": "Normal",
        "PP": 5,
        "Power": 150,
        "Accuracy": "90%",
        "Category": "Special"
    },
    "Hyper Fang": {
        "Effect": "Has a ~10% chance to make the target flinch.",
        "Type": "Normal",
        "PP": 15,
        "Power": 80,
        "Accuracy": "90%",
        "Category": "Physical"
    },
    "Hypnosis": {
        "Effect": "Puts the target to sleep.",
        "Type": "Psychic",
        "PP": 20,
        "Power": "N/A",
        "Accuracy": "60%",
        "Category": "Status"
    },
    "Ice Beam": {
        "Effect": "Has a ~10% chance to freeze the target.",
        "Type": "Ice",
        "PP": 10,
        "Power": 95,
        "Accuracy": "100%",
        "Category": "Special"
    },
    "Ice Punch": {
        "Effect": "Has a ~10% chance to freeze the target.",
        "Type": "Ice",
        "PP": 15,
        "Power": 75,
        "Accuracy": "100%",
        "Category": "Physical"
    },
    "Jump Kick": {
        "Effect": "If this attack misses the target, the user receives 1 HP of damage.",
        "Type": "Fighting",
        "PP": 10,
        "Power": 70,
        "Accuracy": "95%",
        "Category": "Physical"
    },
    "Karate Chop": {
        "Effect": "Has a high critical hit ratio.",
        "Type": "Fighting",
        "PP": 25,
        "Power": 50,
        "Accuracy": "100%",
        "Category": "Physical"
    },
    "Kinesis": {
        "Effect": "Lowers the target's Accuracy by 1 stage.",
        "Type": "Psychic",
        "PP": 15,
        "Power": "N/A",
        "Accuracy": "80%",
        "Category": "Status"
    },
    "Leech Life": {
        "Effect": "Restores the user's HP by 1/2 of the damage inflicted on the target.",
        "Type": "Bug",
        "PP": 15,
        "Power": 20,
        "Accuracy": "100%",
        "Category": "Physical"
    },
    "Leech Seed": {
        "Effect": "The target loses 1/8 of its max HP each turn and the user gains the same amount. Grass-types are unaffected.",
        "Type": "Grass",
        "PP": 10,
        "Power": "N/A",
        "Accuracy": "90%",
        "Category": "Status"
    },
    "Leer": {
        "Effect": "Lowers the target's Defense by 1 stage.",
        "Type": "Normal",
        "PP": 30,
        "Power": "N/A",
        "Accuracy": "100%",
        "Category": "Status"
    },
    "Lick": {
        "Effect": "Has a ~30% chance to paralyze the target.",
        "Type": "Ghost",
        "PP": 30,
        "Power": 20,
        "Accuracy": "100%",
        "Category": "Physical"
    },
    "Light Screen": {
        "Effect": "Halves the damage received from Special moves for 5 turns.",
        "Type": "Psychic",
        "PP": 30,
        "Power": "N/A",
        "Accuracy": "N/A",
        "Category": "Status"
    },
    "Lovely Kiss": {
        "Effect": "Puts the target to sleep.",
        "Type": "Normal",
        "PP": 10,
        "Power": "N/A",
        "Accuracy": "75%",
        "Category": "Status"
    },
    "Low Kick": {
        "Effect": "Inflicts more damage to heavier targets.",
        "Type": "Fighting",
        "PP": 20,
        "Power": "Var Dmg",
        "Accuracy": "100%",
        "Category": "Physical"
    },
    "Meditate": {
        "Effect": "Raises the user's Attack by 1 stage.",
        "Type": "Psychic",
        "PP": 40,
        "Power": "N/A",
        "Accuracy": "N/A",
        "Category": "Status"
    },
    "Mega Drain": {
        "Effect": "Restores the user's HP by 1/2 of the damage inflicted on the target.",
        "Type": "Grass",
        "PP": 10,
        "Power": 40,
        "Accuracy": "100%",
        "Category": "Special"
    },
    "Mega Kick": {
        "Effect": "Damages the target.",
        "Type": "Normal",
        "PP": 5,
        "Power": 120,
        "Accuracy": "75%",
        "Category": "Physical"
    },
    "Mega Punch": {
        "Effect": "Damages the target.",
        "Type": "Normal",
        "PP": 20,
        "Power": 80,
        "Accuracy": "85%",
        "Category": "Physical"
    },
    "Metronome": {
        "Effect": "Randomly selects any move in the game, except for moves such as Counter and Metronome itself.",
        "Type": "Normal",
        "PP": 10,
        "Power": "N/A",
        "Accuracy": "N/A",
        "Category": "Status"
    },
    "Mimic": {
        "Effect": "The user copies a random move from the target's four moves, replacing Mimic for the rest of the battle. It can be used on the first turn. However, the user cannot mimic Transform, Struggle, Sky Drop, moves exclusive to another generation, and any moves that have already been copied.",
        "Type": "Normal",
        "PP": 10,
        "Power": "N/A",
        "Accuracy": "N/A",
        "Category": "Status"
    },
    "Minimize": {
        "Effect": "Raises the user's Evasion by 1 stage.",
        "Type": "Normal",
        "PP": 20,
        "Power": "N/A",
        "Accuracy": "N/A",
        "Category": "Status"
    },
    "Mirror Move": {
        "Effect": "The user copies the target's last move, including its type and max PP.",
        "Type": "Flying",
        "PP": 20,
        "Power": "N/A",
        "Accuracy": "N/A",
        "Category": "Status"
    },
    "Mist": {
        "Effect": "Eliminates any stat modifiers from the user's side of the field. Mist also prevents stat reduction moves and Accuracy reduction moves on the user's side for 5 turns.",
        "Type": "Ice",
        "PP": 30,
        "Power": "N/A",
        "Accuracy": "N/A",
        "Category": "Status"
    },
    "Night Shade": {
        "Effect": "Always deals damage equal to the user's level.",
        "Type": "Ghost",
        "PP": 15,
        "Power": "Var Dmg",
        "Accuracy": "100%",
        "Category": "Special"
    },
    "Pay Day": {
        "Effect": "Increases money earned after defeating a Pokemon by 2x.",
        "Type": "Normal",
        "PP": 20,
        "Power": 40,
        "Accuracy": "100%",
        "Category": "Physical"
    },
    "Peck": {
        "Effect": "Damages the target.",
        "Type": "Flying",
        "PP": 35,
        "Power": 35,
        "Accuracy": "100%",
        "Category": "Physical"
    },
    "Petal Dance": {
        "Effect": "The user becomes uncontrollable and attacks for 2-5 consecutive turns; the user cannot switch out and falls asleep immediately upon finishing.",
        "Type": "Grass",
        "PP": 10,
        "Power": 90,
        "Accuracy": "100%",
        "Category": "Special"
    },
    "Pin Missile": {
        "Effect": "Attacks 2-5 times in one turn; if one of these attacks breaks a target's Substitute, the target will take damage for the rest of the hits. This move has a 3/8 chance to hit twice, a 3/8 chance to hit three times, a 1/8 chance to hit four times and a 1/8 chance to hit five times.",
        "Type": "Bug",
        "PP": 20,
        "Power": 14,
        "Accuracy": "85%",
        "Category": "Physical"
    },
    "Poison Gas": {
        "Effect": "Poisons the target.",
        "Type": "Poison",
        "PP": 40,
        "Power": "N/A",
        "Accuracy": "55%",
        "Category": "Status"
    },
    "Poison Powder": {
        "Effect": "Poisons the target.",
        "Type": "Poison",
        "PP": 35,
        "Power": "N/A",
        "Accuracy": "75%",
        "Category": "Status"
    },
    "Poison Sting": {
        "Effect": "Has a ~20% chance to poison the target.",
        "Type": "Poison",
        "PP": 35,
        "Power": 15,
        "Accuracy": "100%",
        "Category": "Physical"
    },
    "Poisonpowder": {
        "Effect": "Poisons the target.",
        "Type": "Poison",
        "PP": 35,
        "Power": "N/A",
        "Accuracy": "75%",
        "Category": "Status"
    },
    "Pound": {
        "Effect": "Damages the target.",
        "Type": "Normal",
        "PP": 35,
        "Power": 40,
        "Accuracy": "100%",
        "Category": "Physical"
    },
    "Psybeam": {
        "Effect": "Has a ~10% chance to confuse the target.",
        "Type": "Psychic",
        "PP": 20,
        "Power": 65,
        "Accuracy": "100%",
        "Category": "Special"
    },
    "Psychic": {
        "Effect": "Has a ~30% chance to lower the target's Special by 1 stage.",
        "Type": "Psychic",
        "PP": 10,
        "Power": 90,
        "Accuracy": "100%",
        "Category": "Special"
    },
    "Psywave": {
        "Effect": "Deals damage between 1 and 1.5x the user's level.",
        "Type": "Psychic",
        "PP": 15,
        "Power": "Var Dmg",
        "Accuracy": "100%",
        "Category": "Special"
    },
    "Quick Attack": {
        "Effect": "Damages the target.",
        "Type": "Normal",
        "PP": 30,
        "Power": 40,
        "Accuracy": "100%",
        "Category": "Physical"
    },
    "Rage": {
        "Effect": "If the user is hit after using Rage, its Attack rises by 1 stage (up to +6) and it will automatically use Rage every turn (even if it misses or is already using it) until it faints or leaves battle.",
        "Type": "Normal",
        "PP": 20,
        "Power": "Var Dmg",
        "Accuracy": "100%",
        "Category": "Physical"
    },
    "Razor Leaf": {
        "Effect": "Has a high critical hit ratio.",
        "Type": "Grass",
        "PP": 25,
        "Power": 55,
        "Accuracy": "95%",
        "Category": "Physical"
    },
    "Razor Wind": {
        "Effect": "The user becomes uncontrollable and attacks for 2 consecutive turns; the user cannot switch out.",
        "Type": "Normal",
        "PP": 10,
        "Power": 80,
        "Accuracy": "75%",
        "Category": "Special"
    },
    "Recover": {
        "Effect": "Restores the user's HP by 1/2 of its max HP.",
        "Type": "Normal",
        "PP": 20,
        "Power": "N/A",
        "Accuracy": "N/A",
        "Category": "Status"
    },
    "Reflect": {
        "Effect": "Halves the damage received from Physical moves for 5 turns.",
        "Type": "Psychic",
        "PP": 20,
        "Power": "N/A",
        "Accuracy": "N/A",
        "Category": "Status"
    },
    "Rest": {
        "Effect": "The user falls asleep and restores all of its HP, ending all major status conditions in the process.",
        "Type": "Psychic",
        "PP": 10,
        "Power": "N/A",
        "Accuracy": "N/A",
        "Category": "Status"
    },
    "Roar": {
        "Effect": "Forces the target to switch out and be replaced with a random Pokemon.",
        "Type": "Normal",
        "PP": 20,
        "Power": "N/A",
        "Accuracy": "100%",
        "Category": "Status"
    },
    "Rock Slide": {
        "Effect": "Has a ~30% chance to make the target flinch.",
        "Type": "Rock",
        "PP": 10,
        "Power": 75,
        "Accuracy": "90%",
        "Category": "Physical"
    },
    "Rock Throw": {
        "Effect": "Damages the target.",
        "Type": "Rock",
        "PP": 15,
        "Power": 50,
        "Accuracy": "90%",
        "Category": "Physical"
    },
    "Rolling Kick": {
        "Effect": "Has a ~30% chance to make the target flinch.",
        "Type": "Fighting",
        "PP": 15,
        "Power": 60,
        "Accuracy": "85%",
        "Category": "Physical"
    },
    "Sand Attack": {
        "Effect": "Lowers the target's Accuracy by 1 stage.",
        "Type": "Ground",
        "PP": 15,
        "Power": "N/A",
        "Accuracy": "100%",
        "Category": "Status"
    },
    "Scratch": {
        "Effect": "Damages the target.",
        "Type": "Normal",
        "PP": 35,
        "Power": 40,
        "Accuracy": "100%",
        "Category": "Physical"
    },
    "Screech": {
        "Effect": "Lowers the target's Defense by 2 stages.",
        "Type": "Normal",
        "PP": 40,
        "Power": "N/A",
        "Accuracy": "85%",
        "Category": "Status"
    },
    "Seismic Toss": {
        "Effect": "Deals damage equal to the user's level.",
        "Type": "Fighting",
        "PP": 20,
        "Power": "Var Dmg",
        "Accuracy": "100%",
        "Category": "Physical"
    },
    "Selfdestruct": {
        "Effect": "The Defense stat of other Pokemon is halved against this attack, essentially doubling the move's base power; causes the user to faint.",
        "Type": "Normal",
        "PP": 5,
        "Power": 200,
        "Accuracy": "100%",
        "Category": "Physical"
    },
    "Sharpen": {
        "Effect": "Raises the user's Attack by 1 stage.",
        "Type": "Normal",
        "PP": 30,
        "Power": "N/A",
        "Accuracy": "N/A",
        "Category": "Status"
    },
    "Sing": {
        "Effect": "Puts the target to sleep.",
        "Type": "Normal",
        "PP": 15,
        "Power": "N/A",
        "Accuracy": "55%",
        "Category": "Status"
    },
    "Skull Bash": {
        "Effect": "On the first turn, the user raises its Defense by 1 stage. On the second turn, the user attacks.",
        "Type": "Normal",
        "PP": 15,
        "Power": 100,
        "Accuracy": "100%",
        "Category": "Physical"
    },
    "Sky Attack": {
        "Effect": "On the first turn, the user flies into the air, becoming uncontrollable, and evades most attacks. Swift may still hit a Pokemon in the air. On the second turn, the user attacks.",
        "Type": "Flying",
        "PP": 5,
        "Power": 140,
        "Accuracy": "90%",
        "Category": "Physical"
    },
    "Slam": {
        "Effect": "Damages the target.",
        "Type": "Normal",
        "PP": 20,
        "Power": 80,
        "Accuracy": "75%",
        "Category": "Physical"
    },
    "Slash": {
        "Effect": "Has a high critical hit ratio.",
        "Type": "Normal",
        "PP": 20,
        "Power": 70,
        "Accuracy": "100%",
        "Category": "Physical"
    },
    "Sleep Powder": {
        "Effect": "Puts the target to sleep.",
        "Type": "Grass",
        "PP": 15,
        "Power": "N/A",
        "Accuracy": "75%",
        "Category": "Status"
    },
    "Sludge": {
        "Effect": "Has a ~30% chance to poison the target.",
        "Type": "Poison",
        "PP": 20,
        "Power": 65,
        "Accuracy": "100%",
        "Category": "Special"
    },
    "Smog": {
        "Effect": "Has a ~40% chance to poison the target.",
        "Type": "Poison",
        "PP": 20,
        "Power": 30,
        "Accuracy": "70%",
        "Category": "Special"
    },
    "Smokescreen": {
        "Effect": "Lowers the target's Accuracy by 1 stage.",
        "Type": "Normal",
        "PP": 20,
        "Power": "N/A",
        "Accuracy": "100%",
        "Category": "Status"
    },
    "Soft-Boiled": {
        "Effect": "Restores 1/2 of the user's max HP.",
        "Type": "Normal",
        "PP": 10,
        "Power": "N/A",
        "Accuracy": "N/A",
        "Category": "Status"
    },
    "Solar Beam": {
        "Effect": "On the first turn, the user charges up and cannot make a move. On the second turn, the user attacks.",
        "Type": "Grass",
        "PP": 10,
        "Power": 120,
        "Accuracy": "100%",
        "Category": "Special"
    },
    "Sonic Boom": {
        "Effect": "Always deals 20 HP of damage to the target.",
        "Type": "Normal",
        "PP": 20,
        "Power": 20,
        "Accuracy": "90%",
        "Category": "Special"
    },
    "Spike Cannon": {
        "Effect": "Attacks 2-5 times in one turn; if one of these attacks breaks a target's Substitute, the target will take damage for the rest of the hits. This move has a 3/8 chance to hit twice, a 3/8 chance to hit three times, a 1/8 chance to hit four times and a 1/8 chance to hit five times.",
        "Type": "Normal",
        "PP": 15,
        "Power": 20,
        "Accuracy": "100%",
        "Category": "Physical"
    },
    "Splash": {
        "Effect": "Does absolutely nothing.",
        "Type": "Normal",
        "PP": 40,
        "Power": "N/A",
        "Accuracy": "N/A",
        "Category": "Status"
    },
    "Spore": {
        "Effect": "Puts the target to sleep.",
        "Type": "Grass",
        "PP": 15,
        "Power": "N/A",
        "Accuracy": "100%",
        "Category": "Status"
    },
    "Stomp": {
        "Effect": "Has a ~30% chance to make the target flinch.",
        "Type": "Normal",
        "PP": 20,
        "Power": 65,
        "Accuracy": "100%",
        "Category": "Physical"
    },
    "Strength": {
        "Effect": "Damages the target.",
        "Type": "Normal",
        "PP": 15,
        "Power": 80,
        "Accuracy": "100%",
        "Category": "Physical"
    },
    "String Shot": {
        "Effect": "Lowers the target's Speed by 1 stage.",
        "Type": "Bug",
        "PP": 40,
        "Power": "N/A",
        "Accuracy": "95%",
        "Category": "Status"
    },
    "Struggle": {
        "Effect": "When a Pokemon has no usable moves, it uses Struggle. Struggle deals 1/4 of the user's max HP in damage to the target and the user receives 1/2 of the damage it inflicted in recoil.",
        "Type": "Normal",
        "PP": "N/A",
        "Power": 50,
        "Accuracy": "N/A",
        "Category": "Physical"
    },
    "Stun Spore": {
        "Effect": "Paralyzes the target.",
        "Type": "Grass",
        "PP": 30,
        "Power": "N/A",
        "Accuracy": "75%",
        "Category": "Status"
    },
    "Submission": {
        "Effect": "The user receives 1/4 of the damage inflicted as recoil.",
        "Type": "Fighting",
        "PP": 25,
        "Power": 80,
        "Accuracy": "80%",
        "Category": "Physical"
    },
    "Substitute": {
        "Effect": "The user spends 1/4 of its max HP to create a Substitute, which receives the damage inflicted by the opponent's attack before being destroyed. Substitute blocks the effects of moves like Thunder Wave, Leech Seed, Toxic and Rest, but the user will still be put to sleep and receive damage if Rest was already used. Substitute will also block the effects of status conditions such as burn, poison, freeze and paralysis for as long as it remains active, unless the opponent is using a move that inflicts additional damage such as Night Shade. Substitute will also protect the user from additional effects of attacks like Hyper Beam and Sky Attack.",
        "Type": "Normal",
        "PP": 10,
        "Power": "N/A",
        "Accuracy": "N/A",
        "Category": "Status"
    },
    "Super Fang": {
        "Effect": "Always deals damage equal to 1/2 of the target's current HP.",
        "Type": "Normal",
        "PP": 10,
        "Power": "Var Dmg",
        "Accuracy": "90%",
        "Category": "Physical"
    },
    "Supersonic": {
        "Effect": "Confuses the target.",
        "Type": "Normal",
        "PP": 20,
        "Power": "N/A",
        "Accuracy": "55%",
        "Category": "Status"
    },
    "Surf": {
        "Effect": "Damages the target.",
        "Type": "Water",
        "PP": 15,
        "Power": 95,
        "Accuracy": "100%",
        "Category": "Special"
    },
    "Swift": {
        "Effect": "Never misses the target, unless it is in the semi-invulnerable turn of a move such as Dig or Fly.",
        "Type": "Normal",
        "PP": 20,
        "Power": 60,
        "Accuracy": "N/A",
        "Category": "Special"
    },
    "Swords Dance": {
        "Effect": "Raises the user's Attack by 2 stages.",
        "Type": "Normal",
        "PP": 20,
        "Power": "N/A",
        "Accuracy": "N/A",
        "Category": "Status"
    },
    "Tackle": {
        "Effect": "Damages the target.",
        "Type": "Normal",
        "PP": 35,
        "Power": 40,
        "Accuracy": "100%",
        "Category": "Physical"
    },
    "Tail Whip": {
        "Effect": "Lowers the target's Defense by 1 stage.",
        "Type": "Normal",
        "PP": 30,
        "Power": "N/A",
        "Accuracy": "100%",
        "Category": "Status"
    },
    "Take Down": {
        "Effect": "The user receives 1/4 of the damage inflicted as recoil.",
        "Type": "Normal",
        "PP": 20,
        "Power": 90,
        "Accuracy": "85%",
        "Category": "Physical"
    },
    "Teleport": {
        "Effect": "Allows the user to flee from any wild Pokemon battle without fail.",
        "Type": "Psychic",
        "PP": 20,
        "Power": "N/A",
        "Accuracy": "N/A",
        "Category": "Status"
    },
    "Thrash": {
        "Effect": "The user becomes uncontrollable and attacks for 2-3 consecutive turns; the user cannot switch out.",
        "Type": "Normal",
        "PP": 10,
        "Power": 120,
        "Accuracy": "100%",
        "Category": "Physical"
    },
    "Thunder": {
        "Effect": "Has a ~30% chance to paralyze the target.",
        "Type": "Electric",
        "PP": 10,
        "Power": 110,
        "Accuracy": "70%",
        "Category": "Special"
    },
    "Thunder Wave": {
        "Effect": "Paralyzes the target.",
        "Type": "Electric",
        "PP": 20,
        "Power": "N/A",
        "Accuracy": "100%",
        "Category": "Status"
    },
    "Thunderbolt": {
        "Effect": "Has a ~10% chance to paralyze the target.",
        "Type": "Electric",
        "PP": 15,
        "Power": 90,
        "Accuracy": "100%",
        "Category": "Special"
    },
    "Thunderpunch": {
        "Effect": "Has a ~10% chance to paralyze the target.",
        "Type": "Electric",
        "PP": 15,
        "Power": 75,
        "Accuracy": "100%",
        "Category": "Physical"
    },
    "Thundershock": {
        "Effect": "Has a ~10% chance to paralyze the target.",
        "Type": "Electric",
        "PP": 30,
        "Power": 40,
        "Accuracy": "100%",
        "Category": "Special"
    },
    "Toxic": {
        "Effect": "Badly poisons the target.",
        "Type": "Poison",
        "PP": 10,
        "Power": "N/A",
        "Accuracy": "90%",
        "Category": "Status"
    },
    "Transform": {
        "Effect": "The user transforms into the target. Transform copies the target's species, gender, cry, stats, moves, stat changes (other than HP) and types. Using Transform also resets the user's current stat modifiers to the target's stat modifiers. The user cannot copy the target if the user is a different species or has Transformed already. Transform does not copy the target's catch rate or level.",
        "Type": "Normal",
        "PP": 10,
        "Power": "N/A",
        "Accuracy": "N/A",
        "Category": "Status"
    },
    "Tri Attack": {
        "Effect": "Has a ~20% chance to burn, freeze or paralyze the target.",
        "Type": "Normal",
        "PP": 10,
        "Power": 80,
        "Accuracy": "100%",
        "Category": "Special"
    },
    "Twineedle": {
        "Effect": "Attacks 2 times in one turn; if one of these attacks breaks a target's Substitute, the target will take damage for the rest of the hits. This move has a 20% chance to poison the target.",
        "Type": "Bug",
        "PP": 20,
        "Power": 25,
        "Accuracy": "100%",
        "Category": "Physical"
    },
    "Vice Grip": {
        "Effect": "Damages the target.",
        "Type": "Normal",
        "PP": 30,
        "Power": 55,
        "Accuracy": "100%",
        "Category": "Physical"
    },
    "Vine Whip": {
        "Effect": "Damages the target.",
        "Type": "Grass",
        "PP": 25,
        "Power": 35,
        "Accuracy": "100%",
        "Category": "Physical"
    },
    "Water Gun": {
        "Effect": "Damages the target.",
        "Type": "Water",
        "PP": 25,
        "Power": 40,
        "Accuracy": "100%",
        "Category": "Special"
    },
    "Waterfall": {
        "Effect": "Has a ~20% chance to make the target flinch.",
        "Type": "Water",
        "PP": 15,
        "Power": 80,
        "Accuracy": "100%",
        "Category": "Physical"
    },
    "Whirlwind": {
        "Effect": "Forces the target to switch out and be replaced with a random Pokemon.",
        "Type": "Normal",
        "PP": 20,
        "Power": "N/A",
        "Accuracy": "N/A",
        "Category": "Status"
    },
    "Wing Attack": {
        "Effect": "Damages the target.",
        "Type": "Flying",
        "PP": 35,
        "Power": 60,
        "Accuracy": "100%",
        "Category": "Physical"
    },
    "Withdraw": {
        "Effect": "Raises the user's Defense by 1 stage.",
        "Type": "Water",
        "PP": 40,
        "Power": "N/A",
        "Accuracy": "N/A",
        "Category": "Status"
    },
    "Wrap": {
        "Effect": "Damages the target. After attacking, the move traps the target for 2-5 turns, making it unable to use moves, items or flee.",
        "Type": "Normal",
        "PP": 20,
        "Power": 15,
        "Accuracy": "90%",
        "Category": "Physical"
    }
}
