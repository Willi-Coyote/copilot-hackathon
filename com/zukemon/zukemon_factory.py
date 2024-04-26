import random


class ZukemonFactory:
    def create_zukemon(self, type):
        if type == 151:
            return Mew()
        elif type == 8:
            return Wartortle()
        elif type == 9:
            return Blastoise()
        elif type == 258:
            return Mudkip()
        elif type == 25:
            return Pikachu()
        elif type == 54:
            return Psyduck()
        elif type == 553:
            return Krookodile()
        else:
            raise ValueError("No Zukemon for type " + str(type))

    def create_random_zukemon(self):
        zukemon_types = [151, 8, 9, 258, 25, 54, 553]
        zukemon_type = random.choice(zukemon_types)
        return self.create_zukemon(zukemon_type)
