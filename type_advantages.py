# Function to calculate type advantages
def type_advantage(attack_type, defender_types):
    advantages = {
        'Normal': {'double': [], 'half': ['Rock', 'Steel'], 'zero': ['Ghost']},
        'Grass': {'double': ['Water', 'Ground', 'Rock'], 'half': ['Fire', 'Ice', 'Poison', 'Flying', 'Bug', 'Dragon', 'Steel'], 'zero': []},
        'Fire': {'double': ['Grass', 'Ice', 'Bug', 'Steel'], 'half': ['Fire', 'Water', 'Rock', 'Dragon'], 'zero': []},
        'Water': {'double': ['Fire', 'Ground', 'Rock'], 'half': ['Water', 'Grass', 'Dragon'], 'zero': []},
        'Electric': {'double': ['Water', 'Flying'], 'half': ['Electric', 'Ground'], 'zero': []},
        'Ice': {'double': ['Grass', 'Ground', 'Flying', 'Dragon'], 'half': ['Fire', 'Water', 'Ice', 'Steel'], 'zero': []},
        'Fighting': {'double': ['Normal', 'Ice', 'Rock', 'Dark', 'Steel'], 'half': ['Poison', 'Flying', 'Psychic', 'Bug', 'Fairy'], 'zero': []},
        'Poison': {'double': ['Grass', 'Fairy'], 'half': ['Poison', 'Ground', 'Rock', 'Ghost'], 'zero': []},
        'Ground': {'double': ['Fire', 'Electric', 'Poison', 'Rock', 'Steel'], 'half': ['Grass', 'Ice', 'Water'], 'zero': ['Flying']},
        'Flying': {'double': ['Grass', 'Fighting', 'Bug'], 'half': ['Electric', 'Rock', 'Steel'], 'zero': []},
        'Psychic': {'double': ['Fighting', 'Poison'], 'half': ['Psychic', 'Steel'], 'zero': []},
        'Bug': {'double': ['Grass', 'Psychic', 'Dark'], 'half': ['Fire', 'Fighting', 'Poison', 'Flying', 'Ghost', 'Steel', 'Fairy'], 'zero': []},
        'Rock': {'double': ['Fire', 'Ice', 'Flying', 'Bug'], 'half': ['Fighting', 'Ground', 'Steel'], 'zero': []},
        'Ghost': {'double': ['Psychic', 'Ghost'], 'half': ['Dark'], 'zero': ['Normal']},
        'Dragon': {'double': ['Dragon'], 'half': [], 'zero': []},
        'Dark': {'double': ['Psychic', 'Ghost'], 'half': ['Fighting', 'Dark', 'Fairy'], 'zero': []},
        'Steel': {'double': ['Ice', 'Rock', 'Fairy'], 'half': ['Fire', 'Water', 'Electric', 'Steel'], 'zero': []},
        'Fairy': {'double': ['Fighting', 'Dragon', 'Dark'], 'half': ['Fire', 'Poison', 'Steel'], 'zero': []}
    }
    multiplier = 1
    for type in defender_types:
        if type in advantages[attack_type]['double']:
            multiplier *= 2  # Double damage
        elif type in advantages[attack_type]['half']:
            multiplier *= 0.5  # Half damage
        elif type in advantages[attack_type]['zero']:
            multiplier *= 0  # Zero damage
    return multiplier