class ArenaDisplay:
    def __init__(self):
        self.damage = 0

    def update(self, zukemon, damage):
        self.damage = damage
        print(f'{type(zukemon).__name__} made {damage} damage')
