import time


def inventory_main(player, game_data):
    sorted_list = sort_alphabetically(player.inventory)
    # ways to sort: Alpha, Numer, Type, Recent

    # Adjust strings for name, amount, type
    # create list of strings to print

    show_inventory(sorted_list)

    # Management Loop


def show_inventory(sorted_list):
    print("╔════════════════════════════════════════════╗")
    print("║  Inventory                                 ║")
    print("╠═════════════════════════╦══════════╦═══════╣")
    print("║Item                     ║Type      ║Amount ║")
    for k in sorted_list:
        print("╠═════════════════════════╬══════════╬═══════╣")
        name = k[0]
        if len(name) > 21:
            name = name[0:22]
            name = name + "..."
        name = name[0:25].ljust(25)

        amount = str(k[1][0])
        amount = amount.ljust(7)

        tipe = k[1][1]
        tipe = tipe.ljust(10)

        print("║" + name + "║" + tipe + "║" + amount + "║")

    print("╚═════════════════════════╩══════════╩═══════╝")


def sort_alphabetically(inventory):
    unsorted = []
    for key in inventory.items():
        unsorted.append(key)

    sorted(unsorted)

    print(unsorted)
    return unsorted


def sort_type(inventory):
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
    inventory = unsorted.extend(miscs)

    print(inventory)
    return inventory


def sort_amount(inventory):
    for i in range(len(inventory)):
        min_idx = i
        for j in range(i+1, len(inventory)):
            print(inventory[min_idx][1][0])
            print(inventory[j][1][0])
            if inventory[min_idx][1][0] > inventory[j][1][0]:
                min_idx = j
        inventory[i], inventory[min_idx] = inventory[min_idx], inventory[i]
    print(inventory)
    return inventory


def sort_recent(inventory):
    for i in range(len(inventory)):
        min_idx = i
        for j in range(i+1, len(inventory)):
            print(inventory[min_idx][1][2])
            print(inventory[j][1][2])
            if inventory[min_idx][1][2] > inventory[j][1][2]:
                min_idx = j
        inventory[i], inventory[min_idx] = inventory[min_idx], inventory[i]
    print(inventory)
    return inventory


def add_item(player, item):
    print(item)
    if item.get_name() in player.inventory:
        player.inventory[item.get_name()][0] += 1
        player.inventory[item.get_name()][2] = int(time.time())
    else:
        player.inventory[item.get_name()] = []
        player.inventory[item.get_name()].append(1)
        player.inventory[item.get_name()].append(str(type(item).__name__))
        player.inventory[item.get_name()].append(int(time.time()))

    print(player.inventory[item.get_name()])


def inventory_management(player, game_data):
    pass

