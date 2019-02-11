

def inventory(player, game_data):
    print("Item                 |Amount")
    for k, v in player.inventory.items():
        print("____________________________")
        num = 24 - len(k) + len(str(v)) - 2
        string = '{:>' + str(num) + '}'
        amount = string.format("|" + str(v))
        print(k + str(amount))


