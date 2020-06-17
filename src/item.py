class Item:
    def __init__(self, name, description, inspection):
        self.name = name
        self.description = description
        self.inspection = inspection

    def on_take(self):
        """
        make a function  that gives items added options on pickup
        """
        print(f"Take method works!!")

    def examine(self):
        print(f"\n{self.inspection}\n")

    def __str__(self):
        return f"\n{self.name} \n description- {self.description}"


class Weapon(Item):
    def __init__(self, name, description, inspection, damage):
        super().__init__(name, description, inspection)
        self.damage = damage

    def __str__(self):
        return(f"{self.name}")


game_items = {
    "GH-Key":Item("GH-Key", "A key of some kind", "This appears to be a key to a guard house"),
    "GUN": Weapon("gun","pistol","",9)
}

inventories = {

    "outside": [ game_items["GH-Key"],game_items["GUN"] ],

}


unlocks = {
    "GH": game_items["GH-Key"]
}
