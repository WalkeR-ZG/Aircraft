class Coordinate(object):
    def __init__(self, x, y, z, orientation):
        self.x = x
        self.y = y
        self.z = z
        self.orientation = orientation

    def up(self):
        self.z += 1

    def down(self):
        if self.z > 0:
            self.z -= 1
        else:
            self.z = 0

    def forward(self):
        self.orientation.move(self)

    def add_step(self, x_step, y_step):
        self.x += x_step
        self.y += y_step

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y and self.z == other.z
