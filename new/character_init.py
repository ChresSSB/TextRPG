import game_utilities
from new.build import Build
from new.player import Player


def character_creation(players, builds, name):
    build = input("What class is your character?: ")
    save = players

    for item in builds:
        if build in item.name:
            build = item
            break

    if type(build) is str:
        print("Error")
        return "Error"

    save["xref"].append(name)

    save["players"][name] = {"access": [],
        "alive": True,
        "class": build.name,
        "death_count": 0,
        "equipment": {
            "amulet": "empty",
            "boots": "empty",
            "chestplate": "empty",
            "helmet": "empty",
            "leggings": "empty",
            "ring": "empty",
            "weapon": "empty"
        },
        "exp": 0,
        "gold": 0,
        "hp": build.hp,
        "inventory": {},
        "level": 0,
        "location": "Starterville",
        "locked_skills": build.prog,
        "max_hp": build.hp,
        "max_mp": build.mp,
        "mp": build.mp,
        "name": name,
        "next_level": 0,
        "skills": [],
        "stats": {
            "att": build.stats["att"],
            "crt": build.stats["crt"],
            "def": build.stats["def"],
            "evd": build.stats["evd"],
            "spd": build.stats["spd"]
        }}

    game_utilities.write_json("players.json", save)
    print("Character Created!")
    return load_character(players, name)


def load_character(players, name):
    save = players["players"][name]
    player = Player()
    player.load_player(save)
    player.display_stats()
    return player

