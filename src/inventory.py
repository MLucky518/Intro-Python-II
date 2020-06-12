class Inventory:
    def __init__(self,items,capacity):
        self.items = items
        self.capacity = capacity

    def __str__(self):
        return f"Currently in inventory: {self.items}"