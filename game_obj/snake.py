import random
from . import TITLE_START_X, TITLE_START_Y


class Dot:
    def __init__(self, x, y, sign):
        self.x = x
        self.y = y
        self.sign = sign
        self.direct_x = 0
        self.direct_y = 0

    def set_direct(self, x, y):
        self.direct_x = x
        self.direct_y = y
