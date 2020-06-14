from room import Room
from item import Weapon
from item import Item
from item import inventories
from player import Player


#


# Declare all the rooms

room = {
    'outside':  Room("Outside Mansion Gate Entrance",
                     """In front of you there is an unlocked gate with a winding cobblestone path leading up to the Wyndham Mansion """, inventories[0], False),
    "entrance": Room("Outside Mansion Main Entrance", """Before you are two heavy wooden doors that appear to be unlocked """, [], False),

    'foyer':    Room("Foyer", """You are in a huge open area. In front of you there is a large door with a snake crest above the entrance. To your left you can see a regular looking wooden door, but to your right you can see a door with a lions head crest above the entrance.""", [], False),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""", [], False),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""", [], False),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""", [], False),
}


# Link rooms together

room['outside'].n_to = room['entrance']
room["entrance"].n_to = room["foyer"]
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
# Main
#

# Delare Player and Greeting

new_name = input("\nEnter your name adventurer\n")
initial_weapon = Weapon("Bare Fists", "Big balled fists", "Fists of steel", 5)

new_player = Player(new_name, room['outside'],
                    initial_weapon)

print(new_player)


# Make a new player object that is currently in the 'outside' room.

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.

def check_input():
    print_instructions()

    selection = input(
        f" \n What would you like to do next? \n")

    if selection == "m":
        check_movement(new_player)

    elif selection == "i":
        handle_inventory()

    elif selection == "s":
        new_player.search()

    elif selection == "location":
        print(new_player.current_room)


def handle_inventory():
    new_player.print_inventory()
    selection = input(
        f"\nTo Examine an item type examine followed by item name\n ")
    s = selection.split()
    print(s[1])
    for item in new_player.inventory:
        if item.name == s[1] and s[0] == "examine":
            item.examine()
        else:
            print(f"\n invalid input\n")


def print_instructions():
    print(f"\n Press m to move \n Press i to inspect inventory \n Press s to search the area for items\n Type location for current location\n")


def check_movement(player):
    selection = input(
        f" \n{player.name} Where would you like to  move?\n Press w to move forward \n Press a to move left \n Press s to move backwards \n Press d to  move right \n")

    player.move(selection)


while True:

    try:
        check_input()

    except Exception:
        print("Enter a valid value")
