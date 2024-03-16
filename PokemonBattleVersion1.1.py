from type_advantages import *
from scratch_paper import *

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
    print ("Professor Oak: I have three special, powerful Pokemon that would be perfect for the task. \
           \nBecause the closer you get to your Pokemon, the stronger you both become, I am offering you\
           \nonly one of these Pokemon. Pick whichever one you feel the strongest connection to.\
           \n\nThe green one is Bulbasaur, a sturdy toad with a huge bulb on its back.\
           \nAs Bulbasaur grows, his bulb will blossom into a giant flower. \
           \nBulbasaur grows a little slower than the others, but he is currently the strongest by far.")

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
