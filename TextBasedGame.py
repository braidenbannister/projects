#Braiden Bannister
#IT-140
import sys,time,random

rooms = { # establishign nested dictionaries with items and directions as keys
        'Great Hall': {'South': 'Library', 'West': 'Armory', 'North': 'Kitchen'},
        'Bedroom': {'North': 'Drawing Room', 'West': 'Sunroom', 'item': 'Helmet'},
        'Library': {'South': 'Sunroom', 'North': 'Great Hall', 'item': 'Archmage Enchantment'},
        'Sunroom': {'North': 'Library', 'East': 'Bedroom', 'item': 'Sunblessed Shield'},
        'Drawing Room': {'South': 'Bedroom'},
        'Armory': {'East': 'Great Hall', 'item': 'Thunderfury, Blessed Blade of the Windseeker'},
        'Kitchen': {'South': 'Great Hall', 'item': 'Armor'},
        'Exit': {'Exit': 'Exit'}
}
# Creating statics
DIRECTIONS = ['North', 'South', 'East', 'West', 'Add item']
EXIT_COMMAND = "Exit"
VALID_INPUTS = DIRECTIONS + [EXIT_COMMAND]
INVALID_DIRECTION = "That is not a valid direction. You need to enter one of: " + \
                    str(VALID_INPUTS) + "."
CANNOT_GO_THAT_WAY = "You bumped into a wall."
GAME_OVER = "Thanks for playing."
EXIT_ROOM_SENTINEL = "exit"

def show_status_norm(): # for a room with no item
        print_slow("You are in the " + str(tuple1[0]) if not tuple1[1] else str(tuple1))
        print('\nInventory = ', inventory)
        print('-' * 10)
def show_status(): #For cleaner code printing in a function for the while loop
        print_slow("You are in the " + str(tuple1[0]) if not tuple1[1] else str(tuple1))
        print('\nInventory = ', inventory)
        print('-' * 10)
        print_slow('You see the ' + rooms[currentRoom]['item'])
def you_lose(): # Function for losing
        print_slow("You are in the " + str(tuple1))
        print('\nInventory = ', inventory)
        print('-' * 10)
        print_slow("You see what seems like a strike of lightning, before a burning pain rises through your "
                   "stomach. You look down and see Sir Wentworths blade driven deep into your stomach.\n")
        print_slow("You lose.\n")
        print(u'\u2620' * 10)
def you_win():
        print_slow("You are in the " + str(tuple1))
        print('\nInventory = ', inventory)
        print('-' * 10)
        print_slow("\nYou clash blades with Sir Wentworth!")
        print_slow("\nThe vicious clashing of blades can be heard ringing through out the halls. Your "
                   "\nThunderfury blessed blade of the Windseeker cracks with electricity and thunderous booms "
                   "\nthrough the Drawing Room. With the Archmages Enchantment speeding your attacks up you plunge "
                   "\nyour blade into Sir Wentworth's chest and slay the villain. The princess rushes to you "
                   "\nand embraces you - 'My Hero!' You hear her shout. And with that you have won the day.")

def print_slow(str): # Creating a function to write out the printed statement slowly for immersion
        for letter in str:
                print(letter, end='', flush=True)
                time.sleep(0.2)

def showinstructions(): #instructions to show at the start of the game
        print_slow("Sir Wentworth Text Adventure Game!\n")
        print_slow("Collect all 5 Items to win the game, or be defeated by Sir Wentworth!\n")
        print_slow("Move Commands: North, South, East, West.\n")
        print_slow("To add an item to your inventory type: 'add item'\n")
        print_slow("You arrive in the Great Hall, and hear the scream of the princess as Sir Wentworth"
                   " dashes away with her!")
def main(current_room: str, user_input: str): # Main Game Function established
        next_room = current_room
        err_msg = ''
        correctInput = ''
        for i in range(len(user_input)):  # running a for loop in order to change string to correct casing.
                if (i == 0):
                        correctInput += user_input[i].upper()
                else:
                        correctInput += user_input[i].lower()
        if correctInput == 'Add item': # If user wants to add item to inventory then we adjust the list to show item and remove from dict
                if 'item' in rooms[current_room].keys():
                        inventory.append(rooms[current_room]['item'])
                        rooms[current_room].pop('item')
        elif (user_input.lower() == EXIT_COMMAND.lower()):  # If user inputs Exit
                next_room = EXIT_ROOM_SENTINEL
                err_msg = GAME_OVER
        elif (user_input.lower() not in [x.lower() for x in VALID_INPUTS]):  # If user inputs invalid command (Not direction or exit)
                err_msg = INVALID_DIRECTION
        elif (user_input.lower() not in [x.lower() for x in rooms[current_room].keys()]):  # If user inputs valid direction, but cant go that way
                err_msg = CANNOT_GO_THAT_WAY
        else:  # User inputs valid direction for room
                correctInput = ''
                for i in range(len(user_input)): #running a for loop in order to change string to correct casing.
                        if (i == 0):
                                correctInput += user_input[i].upper()
                        else:
                                correctInput += user_input[i].lower()
                next_room = rooms[current_room][correctInput]

        return next_room, err_msg


inventory = []
gameActive = True# set bool to true for loop
currentRoom = "Great Hall"# Set starting room
showinstructions()
while (gameActive): # start game loop
        tuple1 = main(currentRoom, input('\nEnter your move: ')) # call the function
        currentRoom = tuple1[0] # set current room to what the function sets it as making sure to index 0
        if (currentRoom == "exit"): # Break loop if user exits
                print_slow('You chose to exit the game.')
                gameActive = False
        elif currentRoom == "Drawing Room" and len(inventory) >= 5: # Break loop if user wins the game
                you_win()
                gameActive = False
        elif currentRoom == "Drawing Room" and len(inventory) < 5: # lose the game
                you_lose()
                gameActive = False
        elif 'item' in rooms[currentRoom].keys(): # line of code if there is an item in the room
                show_status()
        else: # normal line of code if no item in room
                show_status_norm()



