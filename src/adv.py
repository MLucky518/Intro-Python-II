from room import Room
from item import Weapon
from item import Item
from item import inventories
from player import Player
from item import unlocks

#


# Declare all the rooms

room = {
    'outside':  Room("Outside Mansion Gate Entrance",
                     """In front of you there is an unlocked gate with a winding cobblestone path leading up to the Wyndham Mansion\n On your left past the gate is a large greenhouse, \n and on your right is what seems to be a guard house for gate security """, inventories["outside"], False, []),


    "entrance": Room("Outside Mansion Main Entrance", """Before you are two heavy wooden doors that appear to be unlocked \n On your right you see a large greenhouse, \n and on your left there is a guard house """, [], False, []),

    "Guard House": Room("Guard House", """ Locked guard house""", [], True, unlocks["GH"]),

    'foyer':    Room("Foyer", """You are in a huge open area.\n In front of you there is a large door with a snake crest above the entrance.\n To your left you can see a regular looking wooden door,\n but to your right you can see a door with a lions head crest above the entrance.""", [], False, []),

    "lion": Room("lion", """""", [], True, []),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""", [], False, []),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""", [], False, []),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""", [], False, []),
}


# Link rooms together

room['outside'].n_to = room['entrance']
room["entrance"].n_to = room["foyer"]
room["entrance"].e_to = room["Guard House"]
room["foyer"].e_to = room["lion"]
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
# room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
# Main
#

# Delare Player and Greeting

new_name = input("\nEnter your name adventurer\n")
initial_weapon = Weapon("Bare Fists", "your fists",
                        "They really are YOUR fists", 5)

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

    if selection.lower() == "m":
        check_movement(new_player)

    elif selection.lower() == "i":
        handle_inventory()

    elif selection.lower() == "s":
        new_player.search()

    elif selection.lower() == "location":
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
    if selection == "d":
        if player.current_room.e_to.is_locked:
            for item in player.inventory:
                if item == player.current_room.e_to.unlock_item:
                    player.current_room.e_to.is_locked = False   
                    print("You unlocked the door!")
    player.move(selection)


while True:

    try:
        check_input()

    except Exception:
        print("Enter a valid value")
