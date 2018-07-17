# coding: UTF-8
class Orientation(object):
    ORIENTATION_COLLECTION = ('N', 'E', 'S', 'W')
    ORIENTATION_STEP = {
        'N': [0, 1],
        'E': [1, 0],
        'S': [0, -1],
        'W': [-1, 0]
    }

    def __init__(self, orientation):
        self.ori = orientation
        self.__updateStep__()

    def __updateStep__(self):
        self.x_step, self.y_step = self.ORIENTATION_STEP.get(self.ori)

    def move(self, coord):
        coord.add_step(self.x_step, self.y_step)

    def __eq__(self, other):
        return self.x_step == other.x_step and self.y_step == other.y_step

    def turn_to(self, left):
        for index, value in enumerate(self.ORIENTATION_COLLECTION):
            if self.ori == value:
                if left:
                    turn_flag = 3
                else:
                    turn_flag = 1
                self.ori = self.ORIENTATION_COLLECTION[(index + turn_flag) % len(self.ORIENTATION_COLLECTION)]
                self.__updateStep__()
                return
