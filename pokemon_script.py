from type_advantages import *
from pokemon_creator import *
import sys,time,random



# Thanks to Bill Gross on Stack overflow at
# https://stackoverflow.com/questions/4099422/printing-slowly-simulate-typing
# for the bones of this function.
def slow_type(text, end='\n'):
    # This function prints text letter by letter based on the typing speed below.
    # There are issues, one being that it accepts input while printing.
    # I also want to add the ability to skip the slow printing.
    typing_speed = 200 #wpm
    for letter in text:
        sys.stdout.write(letter)
        sys.stdout.flush()
        # This makes '...'s take significantly longer than other text.
        if letter == '.':
            time.sleep(random.random()/typing_speed*200)
        elif letter not in ['\n', '\\', ' ']:
            time.sleep(5.0/typing_speed)
    print(end)



def starter_descriptions():
        slow_type("\n\nThe green one is Bulbasaur, a sturdy toad with a huge bulb on its back.\
           \nAs Bulbasaur grows, his bulb will blossom into a giant flower, capable of healing, poison, \
           \nand powerful energy blasts. Bulbasaur grows a little slower than the others, but he is \
           \ncurrently the strongest by far. He's also the cuddliest!\
           \n\nThe blue one is Squirtle, and if you couldn't tell by the name, this little squirt\
           \n(get it?) can store and pressurize water in his belly. Someday his shell will grow an \
           \nappendage that looks and acts as a cannon! Nature is truly incredible. For now, this \
           \nlittle turtle is playful and clever, using his shell both as a weapon and a shield.\
           \n\nLastly, we have Charmander. This feisty fella has got an eternal flame in his heart, \
           \nand one on his tail too. I suspect that he will one day become an incredibly powerful \
           \ndragon that can best his old buddies, but he's still got a long way to go until then.\
           \nIf you've got the passion and energy to match Charmander, he will be a good friend.")
        

def choose_pokemon(your_name, pid, caught_pokemon_dict):
    starter_descriptions()
    slow_type(f"So what'll it be, {your_name}? Bulbasaur, Squirtle, or Charmander? ", end='')
    while True:
        try:
            your_choice = input('')
            caught_pokemon_dict = create_pokemon(your_choice, 5, pid, caught_pokemon_dict)
            assert caught_pokemon_dict[1].species in ['Bulbasaur','Squirtle','Charmander']
            pokemon_caught()
        except (AssertionError,KeyError):
            slow_type("I'm sorry, I'm not sure I heard you correctly.\
                  \nWill you pick Bulbasaur, Squirtle, or Charmander?\
                  \nDo you want me to retell my descriptions again?", end='')
            retell = input("")
            if retell.lower().strip() in ['yes','y','yes please', 'pretty please', 'sure', 'why not']:
                starter_descriptions()
            continue
        except:
            print("Some other error occurred.")
            raise
        break

# This officially adjusts the pid and sets caught to True so that you can't select a pokemon 
# you never caught. See create_pokemon() for more info on pid.
def pokemon_caught():
    global pid
    pid += 1
    global caught
    caught = True

# Draws from functions in pokemon_creator.py.
def pokedex_menu():
    while True:
        menu_selection = input(F"WHICH ENTRY FOR {caught_pokemon_dict[pid].name.upper()} DO YOU WANT TO ACCESS?\
            \n\t1: SPECIES\n\t2: PERSONAL\n\t3: MOVES")
        if menu_selection.lower() in ['1', 'species']:
            caught_pokemon_dict[pid].species_entry()
        elif menu_selection.lower() in ['2', 'personal']:
            caught_pokemon_dict[pid].personal_entry()
        elif menu_selection.lower() in ['3', 'moves']:
            caught_pokemon_dict[pid].moves_entry()
        else: 
            return

# Main game
def main():
    print ("\n\n\n\n\n\nWARNING FROM DEVELOPER: DON'T TYPE WHILE TEXT IS PRINTING.\
       \nI AM WORKING ON FIXING THE PROBLEM.\n")
    global caught_pokemon_dict
    caught_pokemon_dict = {}

    # See the create_pokemon function for an explanation of pid.
    global pid
    pid = 0

    global caught
    caught = False

    print("\nProfessor Oak: ", end='')
    slow_type("Hey, neighbor! I can't tell you how excited I am that you are \
          \nstarting off on your journey. As you probably know, Pokemon trainers have to \
          \nstart training at a very young age in order to become a competitive battler \
          \nor an effective researcher. Well, I've known you since you were born, and I have\
          \na strong feeling that you're going to be both! I'm really proud that you've come\
          \nthis far. Anyway, here's what you've been waiting for. Your Pokedex!")
    input("How do you like it? ") 
    slow_type("\nI thought so. There's not many of these floating around, since I'm the inventor, \
          \nand they don't come cheap. So that makes you a very special kid. Go on, set it up.")
    your_name = input("WELCOME, TRAINER!\nWHAT IS YOUR NAME? ").title()
    print(f"\nWELCOME {your_name.upper()}!")
    print("\nProfessor Oak: ", end='')
    slow_type("Great! Now, allow me to remind you what your responsibilities\
              \nare. Your mission is to train a pokemon by traveling and battling until you\
              \nare strong enough to hold your own against the best trainers in the world.\
              \nIn addition, you are to collect as many Pokemon as you can so that I can \
              \ncontinue my research. There are some Pokemon that are so rare and powerful \
              \nthat most people think they are just myths, but I believe that they exist...")
    slow_type("Do you agree?", end='')
    input('')
    slow_type("\nWell, the point is that if you do encounter such a Pokemon, you'll want to be \
              \nstrong enough to try and catch it. Don't go facing something dangerous before\
              \nyou're ready, although I'm sure you'll be plenty careful. Do you accept your \
              \nmission?", end='')
    input("")
    slow_type("\nIn that case, I have three special, powerful Pokemon that would be perfect for the task. \
        \nBecause the closer you get to your Pokemon, the stronger you both become, I am offering you\
        \nonly one of these Pokemon. Pick whichever one you feel the strongest connection to.")
    choose_pokemon(your_name, pid, caught_pokemon_dict)
    slow_type(f"\nGreat choice! Now, go home and rest, play with {caught_pokemon_dict[1].name} and I'll see you\
              \nback here in the morning!")
    if input(f"\nDING!\
          \nNEW POKEMON: {caught_pokemon_dict[1].name.upper()}\
          \nLOOK AT {caught_pokemon_dict[1].name.upper()}'S STATS? \n").lower() in ['yes','y','yes please', 'pretty please', 'sure', 'why not']:
        pokedex_menu()

    slow_type("The next morning...")
    
    

if __name__ == '__main__':
    main()
