

class Zukemon():
    def __init__(self, life_points):
        self.life_points = life_points

    def hit(self):
        pass

    def reduce_life_points_by(self, life_points_to_reduce):
        self.life_points = max(0, self.life_points - life_points_to_reduce)

    def increase_life_points_by(self, life_points_to_increase):
        self.life_points += life_points_to_increase

    def get_life_points(self):
        return self.life_points

    def is_dead(self):
        return self.life_points == 0
