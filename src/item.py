class Item:
    def __init__(self,name,description):
        self.name = name
        self.description = description


class Weapon(Item):
    def __init__(self,name,description,damage):
        super().__init__(name,description)
        self.damage = damage
    
    def __str__(self):
        return(f"{self.name}")
