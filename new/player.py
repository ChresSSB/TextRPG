from new.item import Item

class Player:

    def __init__(self, name, build):
        self.name = name
        self.max_hp = build.hp
        self.max_mp = build.mp
        self.hp = build.hp
        self.mp = build.mp
        self.level = 0
        self.exp = 0
        self.gold = 0
        self.equipment = []
        self.locked_skills = build.prog
        self.skills = []
        self.inventory = []
        self.alive = True

    def take_damage(self, damage):
        self.hp = self.hp - damage
        if self.hp <= 0:
            self.alive = False

    def heal_damage(self, amount):
        self.hp = self.hp + amount
        if self.hp > self.max_hp:
            self.hp = self.max_hp

    def equip(self, item):
        pass

    def dequip(self, item):
        pass

    def display_stats(self):
        pass

    def __str__(self):
        return ', '.join("%s: %s" % item for item in vars(self).items())
