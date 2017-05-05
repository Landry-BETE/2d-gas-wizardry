import random

import numpy as np

BLUE = (0, 0, 255)


class Particle:
    def __init__(self, x_boundary, y_boundary, color=BLUE, size_range=(14, 15), max_ini_speed=10):
        L = [2 * i - max_ini_speed for i in range(max_ini_speed + 1) if i != max_ini_speed / 2]
        self.size = random.randrange(*size_range)
        self.pos = np.random.rand(2) * ([x_boundary, y_boundary ] - np.array([self.size]*2)) + [self.size]*2
        self.color = color
        self.x_boundary = x_boundary
        self.y_boundary = y_boundary
        self.speed = np.array([random.choice(L), random.choice(L)]).astype('float64')

    def move(self):
        """Essentially, bouncing from the walls"""
        bounce_x = self.size <= self.pos[0] <= self.x_boundary - self.size
        bounce_y = self.size <= self.pos[1] <= self.y_boundary - self.size
        self.speed = np.array([2 * bounce_x - 1, 2 * bounce_y - 1]) * self.speed
        self.pos += self.speed
