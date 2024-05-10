from type_advantages import *
from pokemon_creator import *
from pokemon_script import *

def player_turn(player, opponent, moves):
    print(f"\n{player.name.capitalize()}, it's your turn!")
    print("Choose a move:")
    for move in moves:
        print(f"{move} - Attack Power: {moves[move]['Power']}")

    move_name = -1
    while True:
        move_name = input("Enter the name of the move you want to use: ").title()
        if move_name in moves:
            break
        else:
            print("That doesn't sound right.")

    move_category_based_player_stats =  get_category(player, opponent, move_name)
    attack_stat = move_category_based_player_stats[0]
    defense_stat = move_category_based_player_stats[1]
    move_type = moves[move_name]['Type']

    # This formula thanks to https://gamefaqs.gamespot.com/gameboy/367023-pokemon-red-version/faqs/64175/damage-calculation
    turndamage = floor((floor(player.level * 2 /5) + 2) * moves[move_name]['Power'] * attack_stat / defense_stat / 50)
    if turndamage > 997:
        turndamage = 997
    turndamage += 2
    if move_type in player.types:
        turndamage += floor(turndamage / 2)
    advantage_multiplier = type_advantage(move_type, opponent.types)
    turndamage *= advantage_multiplier*10
    turndamage = floor(turndamage/10)
    if turndamage not in [0, 1]:
        turndamage = floor(turndamage * random.randrange(217, 255) / 255) 
        if turndamage > opponent.current_health:
            turndamage = opponent.current_health


    opponent.current_health -= turndamage
    print(f"{player.name.capitalize()} attacked {opponent.name.capitalize()} with {move_name} for {turndamage:,.0f} damage!")
    if opponent.current_health <= 0 and player.current_health <= 0:
        print("The game ends in a draw!")
        return True
    elif opponent.current_health <= 0:
        print(f"\n{player.name.capitalize()} has won!")
        return True
    elif player.current_health <= 0:
        print(f"\n{opponent.name.capitalize()} has won!")
        return True
    else:
        print(f"{opponent.name.capitalize()} has {opponent.current_health:,.0f} HP remaining.")
        return False

def battle(player1, player2):
    print("\nLet the battle begin!")
    while player1.current_health > 0 and player2.current_health > 0:
        if player_turn(player1, player2, player1.moves):
            break  # Player 1 won
        if player_turn(player2, player1, player2.moves):
            break  # Player 2 won

def creative_mode_creator(p):
    global pid
    global caught_pokemon_dict
    while True:
        choice = input (f"{p}, choose your Pokemon! ").title()
        if choice in pokemon_dict:
            break
        print("That Pokemon hasn't been added yet.")
    while True:
        try: level = int (input (f"Pick your Pokemon's level. ")) -1
        except:''
        if level in range(100):
            break
        print("Pick a number between 1 and 100.")
    caught_pokemon_dict = create_pokemon(choice, level, pid, caught_pokemon_dict)
    pid += 1

if __name__ == "__main__":    
    pid = 0
    caught_pokemon_dict = {}
    creative_mode_creator('Player 1')
    creative_mode_creator('Player 2')
    battle(caught_pokemon_dict[1], caught_pokemon_dict[2])