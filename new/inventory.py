

def show_inventory(player, game_data):
    print("╔════════════════════════════╗")
    print("║  Inventory                 ║")
    print("╠═════════════════════╦══════╣")
    print("║Item                 ║Amount║")
    line_size = 25
    for k, v in player.inventory.items():
        print("╠═════════════════════╬══════╣")
        num = 24 - len(k) + len(str(v)) - 2
        string = '{:>' + str(num) + '}'
        amount = string.format("║" + str(v))
        if len(str(v)) == 1:
            print("║" + k + str(amount) + "     ║")
        elif len(str(v)) == 2:
            print("║" + k + str(amount) + "    ║")
        else:
            print("║" + k + str(amount) + "   ║")
    print("╚═════════════════════╩══════╝")

