from new.item import Item


class Consumable(Item):
    def __init__(self, item):
        Item.__init__(self, item)
        self.one_time = True

    def __str__(self):
        return self._name

