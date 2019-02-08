import game_utilities
from new import character_init
from new.build import Build
from new.equipable import Equipable
from new.player import Player
import os


def load_data():
    game_data = {}

    builds = game_utilities.process_json("builds.json")
    build_dict = {}

    items = game_utilities.process_json("items.json")
    items_dict = {}
    items_dict["equipable"] = {}
    items_dict["misc"] = {}
    items_dict["consumable"] = {}

    for item in items["equipable"]["equipable_items"]:
        items_dict["equipable"][item] = Equipable(items["equipable"]["equipable_items"][item])


    progs = game_utilities.process_json("prog.json")
    progs_dict = {}

    for build in builds["builds"]:
        build_dict[build] = Build(builds["builds"][build])

    game_data["build_data"] = build_dict
    game_data["item_data"] = items_dict
    print(game_data)
    return game_data


def launch(mode):

    game_data = load_data()

    saves = game_utilities.process_json("players.json")
    if mode == "new":
        name = input("What is your character's name?: ")
        return character_init.character_creation(saves, game_data["build_data"], name)
    else:
        while True:
            name = input("Pick a save: ")
            xref = saves["xref"]
            print(xref)
            if name in xref:
                return character_init.load_character(saves, name)
            else:
                print("That save doesn't exist")


def game_loop():
    """
    game loop
    :param character:
    :return:
    """
    game_status = True
    print("Welcome to the game!")
    # print(character)
    save_file = game_utilities.process_json("saves.json")
    while game_status:
        if player["hp"] == 0:
            print("You will be healed back up to full health!")
            pass
        print("#######################")
        print("1. Stats")
        print("2. Inventory")
        print("3. Rest")
        print("4. Travel")
        print("5. Shop")
        print("6. Encounter")
        print("7. Quit")
        print("#######################")
        selection = input("Select an option: ").lower()
        if selection.startswith("sta") or selection == "1":
            player.display_stats()
        elif selection.startswith("inv") or selection == "2":
            pass
        elif selection.startswith("res") or selection == "3":
            pass
        elif selection.startswith("tr") or selection.startswith("goto") or selection == "4":
            pass
        elif selection.startswith("sho") or selection == "5":
            pass
        elif selection.startswith("enc") or selection == "6":
            pass
        elif selection.startswith("qui") or selection == "7":
            break
        else:
            print("Unrecognized Action. Please try again!")
        save_file["saves"][player["name"]] = player


if __name__ == '__main__':
    player = launch("new")
    player.display_stats()



