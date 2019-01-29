from new.item import Item

class Equipable(Item):
    def __init__(self, name, buy, sell, desc, rarity, type):
        Item.__init__(self, name, buy, sell, desc, rarity, type)
        self._level_requirement = 0
        self._build_requirement = []
        self._boosts = {}
