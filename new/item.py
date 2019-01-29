class Item:
    def __init__(self, name):
        self._name = name
        self._buy = 0
        self._sell = 0
        self._desc = ""
        self._rarity = "common"

    def __str__(self):
        return self.name


