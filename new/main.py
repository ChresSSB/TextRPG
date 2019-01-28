from new.player import Player
from new.build import Build
import game_utilities


if __name__ == '__main__':
    name = "Chres"
    builds_json = game_utilities.process_json("build.json")
    players_json = game_utilities.process_json("players.json")

    build1 = builds_json["builds"]["build1"]
    build = Build(build1)
    player = Player(name, build)
    print(player)
    player_dictionary = player.__dict__

    players_json["players"][player.name] = player_dictionary

    game_utilities.write_json("players.json", players_json)
