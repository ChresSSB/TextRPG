import time

def show_inventory(player, game_data):

    add_item(player, game_data["item_data"]["equipable"]["Leek of higher crit chance"])
    sorted_list = sort_alphabetically(player.inventory)
    # ways to sort: Alpha, Numer, Type, Recent

    print("╔════════════════════════════╗")
    print("║  Inventory                 ║")
    print("╠═════════════════════╦══════╣")
    print("║Item                 ║Amount║")
    line_size = 25
    for k in sorted_list:
        print("╠═════════════════════╬══════╣")
        num = 24 - len(k[0][0:18]) + len(str(k[1])) - 29
        string = '{:>' + str(num) + '}'
        amount = string.format(" ║" + str(k[1][0]))
        if len(k[0]) > 17:
            string = "║" + k[0][0:15] + "..." + str(amount)
        else:
            string = "║" + k[0][0:16] + str(amount)
        if len(str(k[1][0])) == 1:
            print(string + "     ║")
        elif len(str(k[1][0])) == 2:
            print(string + "    ║")
        else:
            print(string + "   ║")
    print("╚═════════════════════╩══════╝")


def sort_alphabetically(inventory):
    unsorted = []
    for key in inventory.items():
        unsorted.append(key)

    sorted(unsorted)

    print(unsorted)
    return unsorted


def add_item(player, item):
    print(item)
    if item._name in player.inventory:
        player.inventory[item._name][0] += 1
        player.inventory[item._name][2] = int(time.time())
    else:
        player.inventory[item._name] = []
        player.inventory[item._name].append(1)
        player.inventory[item._name].append(str(type(item).__name__))
        player.inventory[item._name].append(int(time.time()))

    print(player.inventory[item._name])
