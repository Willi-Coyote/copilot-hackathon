import random


class CriticalHit:
    def is_critical_hit(self, percentage):
        random_number = random.random()
        return random_number < (percentage / 100)
