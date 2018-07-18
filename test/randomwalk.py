from random import choice


class RandomWalk():
    """docstring for RandomWalk"""
    def __init__(self, num_points=1000):
        self.num_points = num_points
        self.x_val = [0]
        self.y_val = [0]


    def fill_walk(self):
        while len(self.x_val) < self.num_points:
            x_direction = choice([1, -1])
            x_distance = choice(list(range(5)))
            x_step = x_direction * x_distance

            y_direction = choice([1, -1])
            y_distance = choice(list(range(5)))
            y_step = y_direction * y_distance

            # 拒绝原地踏步
            if x_step == 0 and y_step == 0:
                continue

            next_x = self.x_val[-1] + x_step
            next_y = self.y_val[-1] + y_step

            self.x_val.append(next_x)
            self.y_val.append(next_y)




