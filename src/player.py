# Write a class to hold player information, e.g. what room they are in
# currently.
from random import randint


class Player:
    def __init__(self, name, current_room, weapon):
        self.name = name
        self.current_room = current_room
        self.health = 20
        self.current_weapon = weapon
        self.inventory = []

    def __str__(self):
        return f" \n Greetings {self.name} !!, you are currently in the {self.current_room} \n currently you have {self.health} health and wield {self.current_weapon} as a weapon"

    def attack(self, enemy):
        print(
            f"\n{self.name} attacks with {self.current_weapon} and deals {self.weapon.damage} damage \n")
        enemy.health - self.weapon.damage

    def getInventory(self):
        return [item.name for item in self.inventory]

    def move(self, direction):
        try:
            if direction == 'w':
                if self.current_room.n_to.is_locked:
                    print(f"LOCKED!!!")
                    return
                self.current_room = self.current_room.n_to
            elif direction == 'd':
                self.current_room = self.current_room.e_to
            elif direction == 's':
                self.current_room = self.current_room.s_to
            elif direction == 'a':
                self.current_room = self.current_room.w_to
            print(f'\n{self.current_room}\n')
        except AttributeError:
            print(f'\nThere is no room in that direction')

    def search(self):
        if len(self.current_room.inventory) <= 0:
            print(f"\nThe area contains nothing of interest\n")
            return
        num = randint(0, len(self.current_room.inventory) - 1)
        current_item = self.current_room.inventory[num]
        selection = input(
            f" \n you found  {current_item.name} would you like to pick it up?\n y for yes \n n for no\n")
        if selection.lower() == "y":
            if len(self.inventory) < 5:
                self.inventory.append(current_item)
                self.current_room.inventory.remove(current_item)
                current_item.on_take()
                print(f"\nYou picked up {current_item} \n")
            else:
                print("\n no inventory space\n")

    def print_inventory(self):
        print(f"Current Items i Inventory -")
        for item in self.inventory:
            print(f"\n {item.name}\n")


class Enemy(Player):
    def __init__(self, name, current_room, weapon, damage, health):
        super().__init__(name, current_room, weapon)
        self.damage = damage
        self.health = health
