class Item:
    def __init__(self, item):
        self._name = item["name"]
        self._buy_price = item["buy_price"]
        self._sell_price = item["sell_price"]
        self._desc = item["description"]
        self._rarity = item["rarity"]

    def __str__(self):
        return self._name

    def get_name(self):
        return self._name

    def get_buy_price(self):
        return self._buy_price

    def get_sell_price(self):
        return self._sell_price

    def get_desc(self):
        return self._desc

    def get_rarity(self):
        return self._rarity
