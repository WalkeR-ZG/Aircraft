from Coordinate import Coordinate
from Orientation import Orientation


class Position(Coordinate, Orientation):
    def __init__(self, x, y, z, orientation):
        Orientation.__init__(self, orientation)
        Coordinate.__init__(self, x, y, z, self)

    def __eq__(self, other):
        return Coordinate.__eq__(self, other) and Orientation.__eq__(self, other)
