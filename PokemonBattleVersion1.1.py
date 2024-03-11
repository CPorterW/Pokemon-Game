# Define a function to get stats of a chosen pokemon
lvl = 5  # All Pokemon start at level 5
hpmod = 10

def get_stats(starter_choice):
    # Return stats based on the chosen pokemon
    # [1. The Pokemon's name, 2. Their level, 3. Their HP, 4. Their attack, 5. Their type]
    if starter_choice == 'bulbasaur':
        return [starter_choice, lvl, 5 * lvl * hpmod, 0.25 * lvl, "Grass"]
    elif starter_choice == 'charmander':
        return [starter_choice, lvl, 4.5 * lvl * hpmod, 0.27 * lvl, "Fire"]
    else:  # squirtle
        return [starter_choice, lvl, 4.7 * lvl * hpmod, 0.26 * lvl, "Water"]

def get_moves(pokemon):
    if pokemon == 'bulbasaur':
        return [('Tackle', 50, 'Normal'), ('Vine Whip', 40, 'Grass'), ('Growl', 0, 'Normal')]
    elif pokemon == 'charmander':
        return [('Tackle', 50, 'Normal'), ('Ember', 40, 'Fire'), ('Growl', 0, 'Normal')]
    elif pokemon == 'squirtle':
        return [('Tackle', 50, 'Normal'), ('Water Gun', 40, 'Water'), ('Growl', 0, 'Normal')]

def choose_pokemon(player, p1, p2, p3, p4, p5, p6):
    pokemoptions = [p1, p2, p3, p4, p5, p6]
    starter_choice = "missingno"
    while starter_choice not in pokemoptions:
        print(f"\n{player}, will you choose:")
        for i in range(len(pokemoptions)):
            if not pokemoptions[i + 1].isdigit():
                print(f"{pokemoptions[i].capitalize()}")
            else:
                print(f"or {pokemoptions[i].capitalize()}?")
                break
        starter_choice = input().lower().strip()
        if starter_choice not in pokemoptions:
            print(f"I'm sorry, I'm not sure I heard you correctly. Please choose {p1.capitalize()}, {p2.capitalize()}, or {p3.capitalize()}.")

    return get_stats(starter_choice)

# Function to calculate type advantages
def type_advantage(attacker_type, defender_type):
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

    if attacker_type in advantages and defender_type in advantages[attacker_type]['double']:
        return 2  # Double damage
    elif attacker_type in advantages and defender_type in advantages[attacker_type]['half']:
        return 0.5  # Half damage
    elif attacker_type in advantages and defender_type in advantages[attacker_type]['zero']:
        return 0  # Zero damage
    else:
        return 1  # No advantage

def player_turn(player, opponent, moves):
    print(f"\n{player[0].capitalize()}, it's your turn!")
    print("Choose a move:")
    for i, (move, move_power, move_type) in enumerate(moves, start=1):
        print(f"{i}. {move} - Attack Power: {move_power}")

    move_index = -1
    while move_index not in range(len(moves)):
        try:
            move_index = int(input("Enter the number of the move you want to use: ")) - 1
            if move_index not in range(len(moves)):
                print("Invalid input. Please enter a valid number.")
        except ValueError:
            print("Invalid input. Please enter a number.")

    turndamage = player[3] * moves[move_index][1]
    move_type = moves[move_index][2]
    advantage_multiplier = type_advantage(move_type, opponent[4])
    turndamage *= advantage_multiplier
    if player [4] == move_type:
        turndamage *= 1.5

    opponent[2] -= turndamage
    print(f"{player[0].capitalize()} attacked {opponent[0].capitalize()} with {moves[move_index][0]} for {turndamage:,.0f} damage!")

    if opponent[2] <= 0:
        print(f"\n{player[0].capitalize()} has won!")
        return True
    else:
        print(f"{opponent[0].capitalize()} has {opponent[2]:,.0f} HP remaining.")
        return False

def battle(player1, player2, player1_moves, player2_moves):
    print("\nLet the battle begin!")
    while player1[2] > 0 and player2[2] > 0:
        if player_turn(player1, player2, player1_moves):
            break  # Player 1 won
        if player_turn(player2, player1, player2_moves):
            break  # Player 2 won

# Main game
print("\n\nWelcome to the Pokémon Battle Game!")
pokemon1_stats = choose_pokemon("Player 1", "bulbasaur", "charmander", "squirtle", "0", "0", "0")
pokemon1_moves = get_moves(pokemon1_stats[0])
pokemon2_stats = choose_pokemon("Player 2", "bulbasaur", "charmander", "squirtle", "0", "0", "0")
pokemon2_moves = get_moves(pokemon2_stats[0])

print(f"\nPlayer 1 chose {pokemon1_stats[0].capitalize()}.")
print(f"Player 2 chose {pokemon2_stats[0].capitalize()}.")

battle(pokemon1_stats, pokemon2_stats, pokemon1_moves, pokemon2_moves)
