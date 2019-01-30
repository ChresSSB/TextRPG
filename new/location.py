
class Location:
    def __init__(self, name, location):
        self._name = name
        self._adjacent = location["adjacent"]
        self._enemies = {}
        self._shops = []
        self._npcs = []
        self._rest = False

    def __str__(self):
        return self.name

    def get_name(self):
        return self._name

    def get_adjacent(self):
        return self._adjacent

    def set_adjacent(self, locations):
        self._adjacent = locations

    def add_adjacent(self, location):
        self._adjacent.append(location)

    def clear_adjacent(self):
        self._adjacent = []

    def get_shops(self):
        return self._shops

    def set_shops(self, shops):
        self._shops = shops

    def add_shops(self, shop):
        self._shops.append(shop)

    def clear_shops(self):
        self._shops = []

    def get_npcs(self):
        return self._npcs

    def set_npcs(self, npcs):
        self._npcs = npcs

    def add_npcs(self, npc):
        self._npcs.append(npc)

    def clear_npcs(self):
        self._npcs = []

    def get_enemies(self):
        return self._enemies

    def set_enemies(self, enemies):
        self._enemies = enemies

    def add_enemies(self, enemy, ratio):
        self._enemies[enemy] = ratio

    def clear_enemies(self):
        self._enemies = {}


