from ant import Ant
import math

class Environment:
    """ Defines the boundary of a simulation and its properties """

    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.ants = []
        self.color = (0, 0, 0)

    def add_ant(self, x, y, speed, angle, awareness_radius):
        """ Add ant to the Environment"""
        ant = Ant(x, y, speed, angle, awareness_radius)
        self.ants.append(ant)


    def update(self):
        """  Moves ants """
        for i, ant in enumerate(self.ants):
            ant.move()
            self.keep_ant_in_bounds(ant)

    def keep_ant_in_bounds(self, ant):
        """ Corrects angle if ant has hit environment boundary"""

        if ant.x > self.width - ant.size:
            ant.x = 2*(self.width - ant.size) - ant.x
            ant.angle = - ant.angle

        elif ant.x < ant.size:
            ant.x = 2*ant.size - ant.x
            ant.angle = - ant.angle

        if ant.y > self.height - ant.size:
            ant.y = 2*(self.height - ant.size) - ant.y
            ant.angle = math.pi - ant.angle

        elif ant.y < ant.size:
            ant.y = 2*ant.size - ant.y
            ant.angle = math.pi - ant.angle