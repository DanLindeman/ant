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
            ant.change_direction_randomly()
            self.keep_in_bounds(ant)

    def keep_in_bounds(self, obj):
        """ Corrects angle if ant has hit environment boundary"""

        if obj.x > self.width - obj.size:
            obj.x = 2*(self.width - obj.size) - obj.x
            obj.angle = - obj.angle

        elif obj.x < obj.size:
            obj.x = 2*obj.size - obj.x
            obj.angle = - obj.angle

        if obj.y > self.height - obj.size:
            obj.y = 2*(self.height - obj.size) - obj.y
            obj.angle = math.pi - obj.angle

        elif obj.y < obj.size:
            obj.y = 2*obj.size - obj.y
            obj.angle = math.pi - obj.angle