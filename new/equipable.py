from new.item import Item


class Equipable(Item):
    def __init__(self, item):
        Item.__init__(self, item)
        self._build_requirement = item["classes"]
        self._slot = item["slot"]

    def __str__(self):
        return self._name

