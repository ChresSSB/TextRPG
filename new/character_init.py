import game_utilities
from new.build import Build


def character_creation(players, builds):
    name = input("What is the name of your character?: ")
    build = input("What class is your character?: ")

    for item in builds:
        print(str(type(item)) + ": " +  item.name)

    return ""

    players["xref"] = name

    save = players["players"]

    save[name] = {"access": [],
        "alive": True,
        "build": build.name,
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
        "inventory": [],
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
            "att": build.stats.attack,
            "crt": build.stats.critical,
            "def": build.stats.defense,
            "evd": build.stats.evasion,
            "spd": build.stats.speed
        }}

    game_utilities.write_json("players.json", save)





if __name__ == '__main__':
    players = game_utilities.process_json("players.json")

    builds = game_utilities.process_json("builds.json")["builds"]

    buildlist = []

    for key in builds:
        buildlist.append(Build(builds[key]))

    print(buildlist)

    character_creation(players, buildlist)