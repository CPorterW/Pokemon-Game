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
    },
    "Ivysaur": {
        'types': ["grass", "poison"], 
        'category': "Seed",
        'height': "3' 3\"",
        'weight': "29.0 lbs",
        'catch_rate': "45 (6.0%)",
        'base_exp': 141,
        'exp_group': "Medium Slow", 
        'evolves': {'level': 32, 'into': 'Venusaur'},
        'base_stats': {"HP": 60, "Attack": 62, "Defense": 63, "Speed": 60, "Special": 80},
        'critical_hit_chance': "11.7%", 
        'pokedex_entries': ["Red/Blue: When the bulb on its back grows large, it appears to lose the ability to stand on its hind legs.",
                            "Yellow: The bulb on its back grows by drawing energy. It gives off an aroma when it is ready to bloom."],
        'level_up_learnset': {
            1: ["Tackle", "Growl", "Leech Seed"], 
            7: ["Leech Seed"], 
            13: ["Vine Whip"], 
            22: ["Poison Powder"], 
            30: ["Razor Leaf"], 
            38: ["Growth"], 
            46: ["Sleep Powder"], 
            54: ["Solar Beam"]},
        'tm_hm_learnset': {
            "TM03": "Swords Dance", 
            "TM06": "Toxic", 
            "TM08": "Body Slam", 
            "TM09": "Take Down",
            "TM10": "Double-Edge", 
            "TM20": "Rage", 
            "TM21": "Mega Drain", 
            "TM22": "Solar Beam",
            "TM31": "Mimic", 
            "TM32": "Double Team", 
            "TM33": "Reflect", 
            "TM34": "Bide", 
            "TM44": "Rest", 
            "TM50": "Substitute", 
            "HM01": "Cut"}
    },
    "Venusaur": {
        'types': ["grass", "poison"],
        'category': "Seed",
        'height': "6' 7\"",
        'weight': "220.5 lbs",
        'catch_rate': "45 (6.0%)",
        'base_exp': 208,
        'exp_group': "Medium Slow",
        'base_stats': {"HP": 80, "Attack": 82, "Defense": 83, "Speed": 80, "Special": 100},
        'critical_hit_chance': "15.6%",
        'pokedex_entries': ["Red/Blue: The plant blooms when it is absorbing solar rays. It stays on the move to line up its bud with the sun's rays.",
        "Yellow: By absorbing solar rays during the day and metabolizing nutrients at night, its large petals grow."],
        'level_up_learnset': {
            1: ["Tackle", "Growl"], 
            7: ["Leech Seed"], 
            13: ["Vine Whip"], 
            22: ["Poison Powder"],
            30: ["Razor Leaf"], 
            43: ["Growth"], 
            51: ["Sleep Powder"], 
            64: ["Solar Beam"]},
        'tm_hm_learnset': {
            "TM03": "Swords Dance", 
            "TM06": "Toxic", 
            "TM08": "Body Slam", 
            "TM09": "Take Down",
            "TM10": "Double-Edge", 
            "TM15": "Hyper Beam", 
            "TM20": "Rage", 
            "TM21": "Mega Drain",
            "TM22": "Solar Beam", 
            "TM31": "Mimic", 
            "TM32": "Double Team", 
            "TM33": "Reflect",
            "TM34": "Bide", 
            "TM36": "Substitute", 
            "HM01": "Cut"}
        },
    "Charmander": {
        'types': ["fire"],
        'category': "Lizard",
        'height': "2' 0\"",
        'weight': "18.7 lbs",
        'catch_rate': "45 (6.9%)",
        'base_exp': 62,
        'exp_group': "Medium Slow", 
        'evolves': {'level': 16, 'into': 'Charmeleon'},
        'base_stats': {"HP": 39, "Attack": 52, "Defense": 43, "Speed": 65, "Special": 60},
        'critical_hit_chance': "8.6%", 
        'pokedex_entries': ["Red/Blue: Obviously prefers hot places. When it rains, steam is said to spout from the tip of its tail.",
                            "Yellow: The fire on the tip of its tail is a measure of its life. If healthy, its tail burns intensely."],
        'level_up_learnset': {
            1: ["Scratch", "Growl"], 
            9: ["Ember"],
            13: ["Leer"],
            17: ["Rage"],
            21: ["Slash"],
            25: ["Flamethrower"],
            33: ["Swords Dance"],
            37: ["Fire Spin"]
        },
        'tm_hm_learnset': {
            "TM06": "Toxic",
            "TM08": "Body Slam",
            "TM09": "Take Down",
            "TM10": "Double-Edge",
            "TM20": "Rage",
            "TM28": "Dig",
            "TM31": "Mimic",
            "TM32": "Double Team",
            "TM34": "Bide",
            "TM38": "Fire Blast",
            "TM39": "Swift",
            "TM44": "Rest",
            "HM01": "Cut",
            "HM03": "Fissure"
            }
    },
    

    "Charmeleon": {
        'types': ["fire"], 
        'category': "Flame",
        'height': "3' 7\"",
        'weight': "41.9 lbs",
        'catch_rate': "45 (6.9%)", 
        'base_exp': 142,
        'exp_group': "Medium Slow",
        'evolves': {'level': 36, 'into': 'Charizard'},
        'base_stats': {"HP": 58, "Attack": 64, "Defense": 58, "Speed": 80, "Special": 80},
        'critical_hit_chance': "8.6%", 
        'pokedex_entries': ["Red/Blue: When it swings its burning tail, it elevates the surrounding temperature to unbearably high levels.",
                            "Yellow: A brutal Pokemon rendered merciless by its dashing speed. Befriending it puts your life at stake."],
        'level_up_learnset': {
            1: ["Scratch", "Growl"],
            9: ["Ember"],
            13: ["Leer"], 
            17: ["Rage"],
            23: ["Slash"],
            29: ["Flamethrower"],
            39: ["Swords Dance"],
            45: ["Fire Spin"]  
        },
        'tm_hm_learnset': {
            "TM06": "Toxic",
            "TM08": "Body Slam",
            "TM09": "Take Down", 
            "TM10": "Double-Edge",
            "TM20": "Rage",
            "TM28": "Dig", 
            "TM31": "Mimic",
            "TM32": "Double Team",
            "TM34": "Bide",
            "TM38": "Fire Blast",
            "TM39": "Swift",
            "TM44": "Rest",
            "HM01": "Cut",
            "HM03": "Fissure"
        }
    },

    "Charizard": {
        'types': ["fire", "flying"],
        'category': "Flame", 
        'height': "5' 7\"",
        'weight': "199.5 lbs",
        'catch_rate': "45 (6.9%)",
        'base_exp': 240,
        'exp_group': "Medium Slow",
        'base_stats': {"HP": 78, "Attack": 84, "Defense": 78, "Speed": 100, "Special": 109},
        'critical_hit_chance': "4.8%",
        'pokedex_entries': ["Red/Blue: It spits fire that is hot enough to melt boulders. It may cause forest fires by blowing flames.", 
                            "Yellow: A Charizard flies about in search of strong opponents. It breathes intense flames that can melt any material."],
        'level_up_learnset': {
            1: ["Scratch", "Growl"],
            9: ["Ember"],
            13: ["Leer"],
            17: ["Rage"], 
            23: ["Slash"],
            33: ["Flamethrower"],
            43: ["Swords Dance"],
            55: ["Fire Spin"]
        },
        'tm_hm_learnset': {
            "TM02": "Razor Wind",
            "TM06": "Toxic", 
            "TM08": "Body Slam",
            "TM09": "Take Down",
            "TM10": "Double-Edge",
            "TM15": "Hyper Beam",
            "TM20": "Rage",
            "TM28": "Dig",
            "TM31": "Mimic", 
            "TM32": "Double Team",
            "TM34": "Bide",
            "TM38": "Fire Blast", 
            "TM39": "Swift",
            "TM44": "Rest",
            "HM01": "Cut"
        }
    },

    "Squirtle": {
        'types': ["water"],
        'category': "Tiny Turtle",
        'height': "1' 8\"",
        'weight': "19.8 lbs",
        'catch_rate': "45 (6.9%)",
        'base_exp': 63,
        'exp_group': "Medium Slow",
        'evolves': {'level': 16, 'into': 'Wartortle'},
        'base_stats': {"HP": 44, "Attack": 48, "Defense": 65, "Speed": 43, "Special": 50},
        'critical_hit_chance': "8.6%",
        'pokedex_entries': ["Red/Blue: After birth, its back swells and hardens into a shell. Powerfully sprays foam from its mouth.",
                            "Yellow: Its shell is not just for protection. Its rounded shape helps it bounce along at a jaunty gait."],
        'level_up_learnset': {
            1: ["Tackle", "Tail Whip"],
            8: ["Bubble"],
            15: ["Water Gun"],
            22: ["Bite"],
            28: ["Withdraw"],
            34: ["Skull Bash"],
            40: ["Hydro Pump"]
        },
        'tm_hm_learnset': {
            "TM06": "Toxic",
            "TM07": "Hail",
            "TM08": "Body Slam",
            "TM09": "Take Down",
            "TM10": "Double-Edge",
            "TM20": "Rage",
            "TM31": "Mimic",
            "TM32": "Double Team",
            "TM34": "Bide",
            "TM35": "Waterfall",
            "TM44": "Rest",
            "HM03": "Surf",
            "HM04": "Strength"
        }
    },

    "Wartortle": {
        'types': ["water"],
        'category': "Turtle",
        'height': "3' 3\"",
        'weight': "49.6 lbs",
        'catch_rate': "45 (6.9%)",
        'base_exp': 142,
        'exp_group': "Medium Slow",
        'evolves': {'level': 36, 'into': 'Blastoise'},
        'base_stats': {"HP": 59, "Attack": 63, "Defense": 80, "Speed": 58, "Special": 65},
        'critical_hit_chance': "8.6%",
        'pokedex_entries': ["Red/Blue: Often hides in water to stalk unwary prey. For swimming fast, it moves its ears to maintain balance.",
                            "Yellow: It is adept at attacking from the water. It swims with its ears spread to maintain balance."],
        'level_up_learnset': {
            1: ["Tackle", "Tail Whip"],
            8: ["Bubble"],
            15: ["Water Gun"],
            24: ["Bite"],
            31: ["Withdraw"],
            38: ["Skull Bash"],
            45: ["Hydro Pump"]
        },
        'tm_hm_learnset': {
            "TM06": "Toxic",
            "TM07": "Hail",
            "TM08": "Body Slam",
            "TM09": "Take Down",
            "TM10": "Double-Edge",
            "TM20": "Rage",
            "TM31": "Mimic",
            "TM32": "Double Team",
            "TM34": "Bide",
            "TM35": "Waterfall",
            "TM44": "Rest",
            "HM03": "Surf",
            "HM04": "Strength"
        }
    },

    "Blastoise": {
        'types': ["water"],
        'category': "Shellfish",
        'height': "5' 3\"",
        'weight': "189.6 lbs",
        'catch_rate': "45 (6.9%)",
        'base_exp': 239,
        'exp_group': "Medium Slow",
        'base_stats': {"HP": 79, "Attack": 83, "Defense": 100, "Speed": 78, "Special": 85},
        'critical_hit_chance': "4.8%",
        'pokedex_entries': ["Red/Blue: A brutal Pokemon with blistering offensive powers. The jets of water it spouts from the jet chambers on its shell can punch through thick steel.",
                            "Yellow: Once it bathes in extremely hot gases from volcanic areas, its body makes the water in its shell into a powerful stream."],
        'level_up_learnset': {
            1: ["Tackle", "Tail Whip"],
            8: ["Bubble"],
            15: ["Water Gun"],
            24: ["Bite"],
            31: ["Withdraw"],
            42: ["Skull Bash"],
            53: ["Hydro Pump"]
        },
        'tm_hm_learnset': {
            "TM06": "Toxic",
            "TM07": "Hail",
            "TM08": "Body Slam",
            "TM09": "Take Down",
            "TM10": "Double-Edge",
            "TM15": "Hyper Beam",
            "TM20": "Rage",
            "TM31": "Mimic",
            "TM32": "Double Team",
            "TM34": "Bide",
            "TM35": "Waterfall",
            "TM44": "Rest",
            "HM03": "Surf",
            "HM04": "Strength"
        }
    },

    # ... and so on for the remaining Pokemon
}

