import random

from game_obj.bases import Dot
from .config import GAME_WIN_SIZE


class Snake:
    def __init__(self):
        head_x = random.randint(1, GAME_WIN_SIZE['width'] - 2)
        head_y = random.randint(1, GAME_WIN_SIZE['height'] - 2)
        direct = self.calc_direct(head_x, head_y)
        self.head = Dot(head_x, head_y, '■')
        self.head.set_direct(*direct)
        self.body = [self.head]
        self.turning_points = {}

    @staticmethod
    def calc_direct(x, y):
        """
        计算初始行进方向
        防止出生点离边缘较近同时又朝边缘移动导致游戏过快结束
        :return:
        """
        # (0,1) 向下    (0,-1) 向上    (1,0) 向右    (-1,0) 向左
        # 右和下的边缘距离
        u_dst, l_dst, r_dst, d_dst = y, x, GAME_WIN_SIZE['width']-x, GAME_WIN_SIZE['height']-y
        m = max(x, y, r_dst, d_dst)
        if m == u_dst:
            return 0, -1
        elif m == l_dst:
            return -1, 0
        elif m == r_dst:
            return 1, 0
        else:
            return 0, 1

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
        return self.head.x <= 0 or self.head.x >= GAME_WIN_SIZE['width'] - 1 or \
               self.head.y <= 0 or self.head.y >= GAME_WIN_SIZE['height'] - 1

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
        head_x = random.randint(1, GAME_WIN_SIZE['width'] - 2)
        head_y = random.randint(1, GAME_WIN_SIZE['height'] - 2)
        super().__init__(head_x, head_y, 'o')
