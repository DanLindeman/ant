

class Actor(object):
    """Base class for all actor objects
    """

    def __init__(self, x, y, speed, angle):
        self.x = x
        self.y = y
        self.angle = angle
        self.speed = speed
 

    def move(self):
        self.x += math.sin(self.angle) * self.speed
        self.y -= math.cos(self.angle) * self.speed