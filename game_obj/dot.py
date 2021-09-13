import random

from game_obj import WIDTH, HEIGHT
from utils import log


class Dot:
    def __init__(self, x, y, sign):
        """
        游戏元素的基类，每个游戏元素都是由一个或多个在命令行中的坐标点所组成的
        :param x:
        :param y:
        :param sign:
        """
        # 坐标
        self.x = x
        self.y = y

        # 文字显示
        self.sign = sign

        # 运动方向
        self.direct_x = 0
        self.direct_y = 0

    def set_direct(self, x, y):
        self.direct_x = x
        self.direct_y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y


class Snake:
    def __init__(self):
        head_x = random.randint(1, WIDTH - 2)
        head_y = random.randint(1, HEIGHT - 2)
        self.head = Dot(head_x, head_y, '■')
        self.head.set_direct(0, 1)
        self.body = [self.head]
        self.turning_points = {
            (head_x, head_y): (1, 0),
        }

    def left(self):
        if self.head.direct_x == 1:
            return
        self.update_turing_points(-1, 0)

    def right(self):
        if self.head.direct_x == -1:
            return
        self.update_turing_points(1, 0)

    def up(self):
        if self.head.direct_y == 1:
            return
        self.update_turing_points(0, -1)

    def down(self):
        if self.head.direct_y == -1:
            return
        self.update_turing_points(0, 1)

    def update_turing_points(self, direct_x, direct_y):
        x = self.head.x
        y = self.head.y
        self.turning_points[(x, y)] = (direct_x, direct_y)

    def eat(self, food: Dot):
        return self.head.x == food.x and self.head.y == food.y

    def grows(self):
        """
        变长！
        :return:
        """
        tail = self.body[-1]
        x = tail.x - tail.direct_x
        y = tail.y - tail.direct_y
        new_tail = Dot(x, y, '□')
        new_tail.set_direct(tail.direct_x, tail.direct_y)
        self.body.append(new_tail)

    def move(self):
        for b in self.body:
            b.x += b.direct_x
            b.y += b.direct_y

    def hit_wall(self):
        return self.head.x <= 0 or self.head.x >= WIDTH - 1 or \
               self.head.y <= 0 or self.head.y >= HEIGHT - 1

    def hit_self(self):
        return self.head in self.body[1:]

    def update_direction(self):
        """
        针对每个拐点，更新body中每个点的运动方向
        当尾部通过一个拐点时，这个拐点需要被弹出
        :return:
        """
        for i, dot in enumerate(self.body):
            x, y = dot.x, dot.y
            direct = self.turning_points.get((x, y))
            if direct:
                dot.set_direct(*direct)
                if i == len(self.body) - 1:
                    self.turning_points.pop((x, y))


class Food(Dot):
    def __init__(self):
        head_x = random.randint(1, WIDTH - 2)
        head_y = random.randint(1, HEIGHT - 2)
        super().__init__(head_x, head_y, 'o')
