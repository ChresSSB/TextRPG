import time
import game_utilities

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
    inventory = player.inventory
    entry = input("equip [item],dequip [slot], look [item], q to quit: ")
    if entry.startswith("equip"):
        item = game_utilities.remove_prefix(entry, "equip ")
        if item in inventory.keys():
            if inventory[item][1] == "Equipable":
                item = game_data['item_data']['equipable'][item]
                if player["build"] or "any" in item.get_build_requirement:
                    slot = item.get_slot
                    player.equipment[slot] = item
                    player.inventory.remove(item)
                    # update_stats(character, item)
                    print("Equipped " + item)
                else:
                    print("Your class can't equip this " + item)
            else:
                print("This item can not be equipped.")
        else:
            print("This item does not exist.")
    elif entry.startswith("dequip"):
        pass
    elif entry.startswith("look"):
        look = game_utilities.remove_prefix(entry, "look ")
        if look in player.inventory:
            if player.inventory[look][1] == "equipable":
                item = game_data["item_data"]["equipable"][look]
                print("Name: " + look)
                print("Description: " + item.get_desc())
                print("Rarity: " + item.get_rarity())
                print("Buy Price: " + str(item.get_buy_price()))
                print("Sell Price: " + str(item.get_sell_price()))
                print("Type: " + str(type(item)))
                print("Slot: " + item.get_slot)
                print("Required Classes: " + ', '.join(item.get_build_requirement))
                print("Properties: ")
                print("     HP: +" + str(item.get_buffs["hp"]))
                print("     MP: +" + str(item.get_buffs["mp"]))
                print("     Attack: +" + str(item.get_buffs["att"]))
                print("     Defense: +" + str(item.get_buffs["def"]))
                print("     Evasion: +" + str(item.get_buffs["evd"]))
                print("     Critical: +" + str(item.get_buffs["crt"]))
                input("press anything to go back to inventory: ")
            if player.inventory[look][1] == "misc":
                print("Name: " + look)
                print("Description: " + item.get_desc())
                print("Rarity: " + item.get_rarity())
                print("Buy Price: " + str(item.get_buy_price()))
                print("Sell Price: " + str(item.get_sell_price()))
                print("Type: " + str(type(item)))
                input("press anything to go back to inventory: ")
        else:
            print("Invalid Item")
    elif entry.startswith("sort"):
        pass
    elif entry == "q":
        pass
    else:
        pass

