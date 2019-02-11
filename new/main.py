from new.game import launch, game_loop
from new.player import Player
from new.build import Build
import game_utilities


if __name__ == '__main__':
    game_data = game_utilities.load_data()
    status = True
    while status:
        print("Welcome to the TextRPG created by ChresSSB")
        print("1. New Game")
        print("2. Load Game")
        print("3. Edit Game")
        print("4. Credits")
        print("5. Quit")
        command = input("Select an option: ").lower()
        if command == "1" or command.startswith("new"):
            player = launch("new", game_data)
            game_loop(player, game_data)
        elif command == "2" or command.startswith("loa"):
            player = launch("load", game_data)
            game_loop(player, game_data)
        elif command == "3" or command.startswith("edi"):
            pass
        elif command == "4" or command.startswith("cre"):
            print("Thank you for ShoShin for very minor help on edit methods and Khajeet for being a tester")
        elif command == "5" or command.startswith("qu"):
            status = False
        else:
            print("Select a valid option!")

