# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
    def __init__(self, name, description, inventory, is_locked,unlock_item):
        self.name = name
        self.description = description
        self.inventory = inventory
        self.is_locked = is_locked
        self.unlock_item = unlock_item

    def __str__(self):
        return f" {self.name} \n {self.description}"
