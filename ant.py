import math
from random import randint

class Ant(object):
    """Class to represent a single Ant
    """

    def __init__(self, x, y, speed, angle, awareness_radius):
        """
        """
        self.x = x
        self.y = y
        self.angle = angle
        self.speed = speed
        self.awareness_radius = awareness_radius

        self.color = (100, 0, 0)
        self.size = 10
        self.thickness = 0 # indicated ants are filled in

    def move(self):
        """Update position based on speed and angle
        """
        self.x += math.sin(self.angle) * self.speed
        self.y -= math.cos(self.angle) * self.speed
        random_selector = randint(0, 40)
        if random_selector == randint(0, 40):
            self.angle += 5
        if random_selector == randint(0, 40):
            self.angle -= 5
