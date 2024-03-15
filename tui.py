

from pynput import keyboard
from IPython.display import clear_output

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
while True:
    p1_direction = movement(p1_direction)

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