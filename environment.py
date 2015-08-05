from ant import Ant

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
        """  Moves particles and tests for collisions with walls others """
        for i, ant in enumerate(self.ants):
            ant.move()