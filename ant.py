

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
        print self.x, self.y


