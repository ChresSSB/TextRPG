import game_utilities
from new import character_init
from new.build import Build
from new.equipable import Equipable
from new.inventory import inventory
from new.player import Player
import os


def launch(mode, game_data):

    saves = game_utilities.process_json("players.json")
    if mode == "new":
        name = input("What is your character's name?: ")
        return character_init.character_creation(saves, game_data["build_data"], name)
    else:
        while True:
            xref = saves["xref"]
            print(', '.join(xref))
            name = input("Pick a save: ")
            if name in xref:
                return character_init.load_character(saves, name)
            else:
                print("That save doesn't exist")


def game_loop(player, game_data):
    """
    game loop
    :param character:
    :return:
    """
    game_status = True
    print("Welcome to the game!")
    save_file = game_utilities.process_json("players.json")
    while game_status:
        if player.hp == 0:
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
            inventory(player, game_data)
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
        save_file["players"][player.name] = player.todict()
        game_utilities.write_json("players.json", save_file)





