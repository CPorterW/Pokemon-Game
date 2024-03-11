import random

class Move:
    def __init__(self, name, move_type, power, accuracy, speed):
        self.name = name
        self.move_type = move_type
        self.power = power
        self.accuracy = accuracy
        self.speed = speed
        self.usage_limit = 2  # Move can be used up to 2 times
        self.used_times = 0  # Tracks how many times the move has been used

    def is_usable(self):
        return self.used_times < self.usage_limit

    def use(self):
        if self.is_usable():
            self.used_times += 1
            return True
        return False

class SpecialMove(Move):
    def __init__(self, name, move_type, power, accuracy, speed, effect=None):
        super().__init__(name, move_type, power, accuracy, speed)
        self.effect = effect

    def apply_effect(self, target):
        if self.effect and self.use():
            self.effect(target)

class Pokemon:
    def __init__(self, name, pokemon_type, health, moves, status=None):
        self.name = name
        self.pokemon_type = pokemon_type
        self.health = health
        self.moves = moves
        self.status = status
        self.status_duration = 0

    def display_moves(self):
        print(f"{self.name}'s moves:")
        for i, move in enumerate(self.moves, start=1):
            if move.is_usable():
                print(f"{i}. {move.name} (Power: {move.power}, Speed: {move.speed}, Usage: {move.used_times}/{move.usage_limit})")

    def select_move(self):
        usable_moves = [move for move in self.moves if move.is_usable()]
        if not usable_moves:
            print(f"{self.name} has no usable moves left!")
            return None
        self.display_moves()
        choice = int(input("Choose your move: ")) - 1
        return usable_moves[choice]

    def take_damage(self, damage):
        self.health -= damage
        if self.health < 0:
            self.health = 0

    def apply_status_effects(self):
        if self.status == "poison":
            poison_damage = 10
            self.health -= poison_damage
            print(f"{self.name} is poisoned and takes {poison_damage} damage.")
            self.status_duration -= 1
        elif self.status == "sleep":
            print(f"{self.name} is asleep and cannot move.")
            self.status_duration -= 1
        
        if self.status_duration <= 0:
            print(f"{self.name}'s {self.status} status has worn off.")
            self.status = None

    def inflict_status(self, status):
        if not self.status:
            self.status = status
            self.status_duration = random.randint(1, 3)
            print(f"{self.name} is now {status} for {self.status_duration} turns.")

type_effectiveness = {
    ("Fire", "Grass"): 2.0, ("Grass", "Fire"): 0.5,
    ("Water", "Fire"): 2.0, ("Fire", "Water"): 0.5,
    ("Grass", "Water"): 2.0, ("Water", "Grass"): 0.5,
    ("Electric", "Water"): 2.0, ("Electric", "Grass"): 0.5,
    ("Fighting", "Normal"): 2.0, ("Rock", "Flying"): 2.0,
}

def calculate_effectiveness(move, defender):
    return type_effectiveness.get((move.move_type, defender.pokemon_type), 1.0)

def calculate_damage(move, attacker, defender):
    effectiveness = calculate_effectiveness(move, defender)
    damage = move.power * effectiveness
    return damage

def ai_choose_move(pokemon, opponent):
    usable_moves = [move for move in pokemon.moves if move.is_usable()]
    best_move = None
    highest_damage = 0
    for move in usable_moves:
        damage = calculate_damage(move, pokemon, opponent) * calculate_effectiveness(move, opponent)
        if damage > highest_damage:
            best_move = move
            highest_damage = damage
    return random.choice(usable_moves) if usable_moves else None

def battle(pokemon1, pokemon2):
    turn = 1
    while pokemon1.health > 0 and pokemon2.health > 0:
        print(f"\nTurn {turn}:")
        pokemon1.apply_status_effects()
        pokemon2.apply_status_effects()

        if pokemon1.health <= 0 or pokemon2.health <= 0:
            break

        move1 = pokemon1.select_move()
        move2 = ai_choose_move(pokemon2, pokemon1)

        if move1 and move2:
            # Determine move order based on speed
            if move1.speed >= move2.speed:
                execute_move(pokemon1, pokemon2, move1)
                if pokemon2.health > 0:
                    execute_move(pokemon2, pokemon1, move2)
            else:
                execute_move(pokemon2, pokemon1, move2)
                if pokemon1.health > 0:
                    execute_move(pokemon1, pokemon2, move1)
        elif move1:  # Only pokemon1 can move
            execute_move(pokemon1, pokemon2, move1)
        elif move2:  # Only pokemon2 can move
            execute_move(pokemon2, pokemon1, move2)
        
        turn += 1

        if pokemon1.health <= 0:
            print(f"{pokemon1.name} fainted. {pokemon2.name} wins!")
            break
        elif pokemon2.health <= 0:
            print(f"{pokemon2.name} fainted. {pokemon1.name} wins!")
            break

def execute_move(attacker, defender, move):
    if attacker.status == "sleep":
        print(f"{attacker.name} is asleep and cannot move.")
        attacker.status_duration -= 1
        if attacker.status_duration <= 0:
            attacker.status = None
            print(f"{attacker.name} woke up!")
    elif move and move.use():
        print(f"{attacker.name} uses {move.name}.")
        if isinstance(move, SpecialMove) and move.effect:
            move.apply_effect(defender)
        else:
            damage = calculate_damage(move, attacker, defender)
            defender.take_damage(damage)
            print(f"{defender.name} took {damage} damage, remaining health {defender.health}.")

# Define moves here...

# Define Pokémon here...

def main():
    # Initialize Pokémon with their moves...

    # Example:
    tackle = Move("Tackle", "Normal", 50, 100, 20)
    ember = Move("Ember", "Fire", 40, 100, 25, 2)
    vine_whip = Move("Vine Whip", "Grass", 45, 100, 25, 2)
    water_gun = Move("Water Gun", "Water", 40, 100, 25, 2)
    # Add more moves...

    charmander = Pokemon("Charmander", "Fire", 100, [ember, tackle])
    bulbasaur = Pokemon("Bulbasaur", "Grass", 100, [vine_whip, tackle])
    squirtle = Pokemon("Squirtle", "Water", 100, [water_gun, tackle])
    # Add more Pokémon...

    available_pokemon = [charmander, bulbasaur, squirtle]
    player_pokemon = select_pokemon(available_pokemon)
    ai_pokemon = random.choice([p for p in available_pokemon if p != player_pokemon])

    print(f"You selected {player_pokemon.name}.")
    print(f"The AI selected {ai_pokemon.name}.")

    battle(player_pokemon, ai_pokemon)

if __name__ == "__main__":
    main()
