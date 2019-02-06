import game_utilities


def reformat(filename):
    data = game_utilities.process_json(filename)
    game_utilities.write_json(filename, data)


def reformat_all():
    pass


reformat("items.json")