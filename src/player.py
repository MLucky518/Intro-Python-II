# Write a class to hold player information, e.g. what room they are in
# currently.
from random import randint


class Player:
    def __init__(self, name, current_room, weapon, inventory):
        self.name = name
        self.current_room = current_room
        self.health = 20
        self.current_weapon = weapon
        self.inventory = inventory

    def __str__(self):
        return f" \n Greetings {self.name} !!, you are currently in the {self.current_room} \n currently you have {self.health} health and wield {self.current_weapon} as a weapon"

    def attack(self, enemy):
        print(
            f"{self.name} attacks with {self.current_weapon} and deals {self.weapon.damage} damage ")
        enemy.health - self.weapon.damage

    def getInventory(self):
        return [item.name for item in self.inventory]

    def move(self, direction):
        try:
            if direction == 'w':
                self.current_room = self.current_room.n_to
            elif direction == 'd':
                self.current_room = self.current_room.e_to
            elif direction == 's':
                self.current_room = self.current_room.s_to
            elif direction == 'a':
                self.current_room = self.current_room.w_to
            print(f'\n{self.current_room}')
        except AttributeError:
            print(f'\nThere is no room in that direction')

    def search(self):
        
        num = randint(0, len(self.current_room.inventory) - 1)
        current_item = self.current_room.inventory[num]
        selection = input(
            f" \n you found  {current_item} would you like to pick it up? y for yes \n n for no")
        if selection.lower() == "y":
            if len(self.inventory.items) < self.inventory.capacity:
                self.inventory.items.append(current_item)
                self.current_room.inventory.remove(current_item)
                print(f"You picked up {current_item} ")
            else:
                print("no inventory space")
