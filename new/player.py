from new.item import Item


class Player:
    def __init__(self):
        self.name = ""
        self.max_hp = 0
        self.max_mp = 0
        self.hp = 0
        self.mp = 0
        self.build = ""
        self.level = 0
        self.exp = 0
        self.next_level = 0
        self.gold = 0
        self.equipment = {
                "helmet": "empty",
                "chestplate": "empty",
                "leggings": "empty",
                "boots": "empty",
                "ring": "empty",
                "amulet": "empty",
                "weapon": "empty"
            }
        self.stats = {}
        self.locked_skills = {}
        self.skills = []
        self.inventory = []
        self.alive = True
        self.death_count = 0
        self.location = ""
        self.access = []

    def new_player(self, name, build):
        self.name = name
        self.max_hp = build.hp
        self.max_mp = build.mp
        self.hp = build.hp
        self.mp = build.mp
        self.build = build.name
        self.level = 0
        self.exp = 0
        self.next_level = 0
        self.gold = 0
        self.equipment = {
            "helmet": "empty",
            "chestplate": "empty",
            "leggings": "empty",
            "boots": "empty",
            "ring": "empty",
            "amulet": "empty",
            "weapon": "empty"
        }
        self.stats = build.stats
        self.locked_skills = build.prog
        self.skills = []
        self.inventory = []
        self.alive = True
        self.death_count = 0
        self.location = ""
        self.access = []

    def load_player(self, save):
        self.name = save["name"]
        self.max_hp = save["max_hp"]
        self.max_mp = save["max_mp"]
        self.hp = save["hp"]
        self.mp = save["mp"]
        self.build = save["class"]
        self.level = save["level"]
        self.exp = save["exp"]
        self.next_level = save["next_level"]
        self.gold = save["gold"]
        self.equipment = save["equipment"]
        self.stats = save["stats"]
        self.locked_skills = save["locked_skills"]
        self.skills = save["skills"]
        self.inventory = save["inventory"]
        self.alive = save["alive"]
        self.death_count = save["death_count"]
        self.location = save["location"]
        self.access = save["access"]

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
        print("***" + self.name + "'s Stats***")
        print("#######################")
        print("Name: " + self.name)
        print("Level: " + str(self.level))
        print("Class: " + self.build)
        print("Deaths: " + str(self.death_count))
        print("Exp: " + str(self.exp))
        print("Next Level: " + str(self.next_level))
        print("Skills: " + ', '.join(self.skills))
        print("Gold: " + str(self.gold))
        print("Location: " + self.location)
        print("Stats:")
        print("     HP: " + str(self.hp) + "/" + str(self.max_hp))
        print("     MP: " + str(self.mp) + "/" + str(self.max_mp))
        print("     Attack: " + str(self.stats["att"]))
        print("     Defense: " + str(self.stats["def"]))
        print("     Evasion: " + str(self.stats["evd"]))
        print("     Speed: " + str(self.stats["spd"]))
        print("     Critical: " + str(self.stats["crt"]))
        print("#######################")

    def __str__(self):
        return ', '.join("%s: %s" % item for item in vars(self).items())
