import game_utilities
from new import character_init
from new.build import Build
from new.player import Player
import os



def launch(mode):
    saves = game_utilities.process_json("players.json")
    if mode == "new":
        name = input("What is your character's name?: ")
        builds = game_utilities.process_json("builds.json")
        for item in builds[""]:
            pass
        # TODO : build all objects with method
        return character_init.character_creation(saves, builds, name)
    else:
        while True:
            name = input("Pick a save: ")
            xref = saves["xref"]
            print(xref)
            if name in xref:
                return character_init.load_character(saves, name)
            else:
                print("That save doesn't exist")


if __name__ == '__main__':
    player = launch("new")
    player.display_stats()



