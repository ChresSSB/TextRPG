import game_utilities

def reformat(filename):
    data = game_utilities.process_json(filename)
    game_utilities.write_json(filename, data)


reformat("items.json")