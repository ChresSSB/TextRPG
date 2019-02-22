from new.item import Item


class Equipable(Item):
    def __init__(self, item):
        Item.__init__(self, item)
        self._build_requirement = item["classes"]
        self._slot = item["slot"]
        self._buffs = item["buffs"]

    def __str__(self):
        return self._name

    def get_slot(self):
        return self._slot

    def get_build_requirement(self):
        return self._build_requirement

    def get_buffs(self):
        return self._buffs

