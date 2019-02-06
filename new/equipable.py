from new.item import Item


class Equipable(Item):
    def __init__(self, item, equipable):
        Item.__init__(self, item)
        self._level_requirement = equipable
        self._build_requirement = []
        self._boosts = {}
        self._slot = ""
