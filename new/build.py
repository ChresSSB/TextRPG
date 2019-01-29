class Build:
    def __init__(self, build):
        self.name = build["name"]
        self.hp = build["hp"]
        self.mp = build["mp"]
        self.stats = build["stats"]
        self.prog = build["prog"]

    def __str__(self):
        return self.name

