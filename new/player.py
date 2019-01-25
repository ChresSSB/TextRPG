

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
        self. equipment =[]
        self.locked_skills = build.skills
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

