import time

def show_inventory(player, game_data):

    add_item(player, game_data["item_data"]["equipable"]["Leek of higher crit chance"])
    sorted_list = sort_alphabetically(player.inventory)
    # ways to sort: Alpha, Numer, Type, Recent

    # Adjust strings for name, amount, type
    # create list of strings to print
    print(sorted_list)

    # format
    print("║Item                 ║Type     ║Amount   ║")


    print("╔═══════════════════════════════════════════╗")
    print("║  Inventory                                ║")
    print("╠═════════════════════════╦═════════╦═══════╣")
    print("║Item                     ║Type     ║Amount ║")
    for k in sorted_list:
        print("╠═════════════════════════╬═════════╬═══════╣")
        name = k[0]
        if len(name) > 21:
            name = name[0:22]
            name = name + "..."
        name = name[0:25].ljust(25)

        amount = str(k[1][0])
        amount = amount.ljust(7)

        tipe = k[1][1]
        tipe = tipe.ljust(9)

        time = k[1][2]

        print("║" + name + "║" + tipe + "║" + amount + "║")


    print("╚═════════════════════════╩═════════╩═══════╝")


def sort_alphabetically(inventory):
    unsorted = []
    for key in inventory.items():
        unsorted.append(key)

    sorted(unsorted)

    print(unsorted)
    return unsorted


def sort_by_type(inventory):
    inventory = sort_alphabetically(inventory)
    equipables = []
    miscs = []
    consumables = []
    for key in inventory:
        if inventory[1][1] == "Equipable":
            equipables.append(key)
        elif inventory[1][1] == "Misc":
            miscs.append(key)
        else:
            consumables.append(key)

    unsorted = equipables.extend(consumables)
    unsorted = unsorted.extend(miscs)

    print(unsorted)
    return unsorted


def sort_recent(inventory):
    pass


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
