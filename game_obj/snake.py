import random
from . import TITLE_START_X, TITLE_START_Y


class Food:
    def __init__(self):
        self.x = random.randint(1, TITLE_START_X - 1)
        self.y = random.randint(1, TITLE_START_Y - 1)
        self.cur_style = ["o", self.y, self.x]


class Snake:
    def __init__(self):
        self.x = 22
        self.y = 10
        self.paint = "*-"
        self.ini_style = [self.paint, self.y, self.x]
        self.cur_style = self.ini_style

    def mov(self):
        pass

    def left(self):
        self.x -= 1
        self.cur_style = [self.paint, self.y, self.x]

    def right(self):
        self.x += 1
        self.cur_style = [self.paint, self.y, self.x]

    def up(self):
        self.y -= 1
        self.cur_style = [self.paint, self.y, self.x]

    def down(self):
        self.y += 1
        self.cur_style = [self.paint, self.y, self.x]

    def eat(self, f: Food):
        if self.x == f.x and self.y == f.y:
            self.grow()
            return True
        else:
            return False

    def grow(self):
        """
        吃了会长大
        :return:
        """
        self.paint += "-"
        self.cur_style = [self.paint, self.y, self.x]
