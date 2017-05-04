import random

WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)


class Particle:
    def __init__(self, x_boundary, y_boundary, color=BLUE, size_range=(10, 11), max_ini_speed=10):
        """it's a mess but it'll get more compact"""
        L = [2 * i - max_ini_speed for i in range(max_ini_speed + 1) if i != max_ini_speed / 2]
        self.size = random.randrange(*size_range)
        self.x = random.randrange(self.size, x_boundary - self.size)
        self.y = random.randrange(self.size, y_boundary - self.size)
        self.color = color
        self.x_boundary = x_boundary
        self.y_boundary = y_boundary
        self.move_x = random.choice(L)
        self.move_y = random.choice(L)

    def move(self):
        """Essentially, bouncing from the walls"""
        self.move_x = (2 * (self.size <= self.x <= self.x_boundary - self.size) - 1) * self.move_x
        self.move_y = (2 * (self.size <= self.y <= self.y_boundary - self.size) - 1) * self.move_y

        self.x += self.move_x
        self.y += self.move_y
