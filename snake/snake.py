import random

from game_obj.bases import Dot, Position
from .config import GAME_WIN_SIZE, SNAKE_STYLE


class Snake:
    def __init__(self):
        pos = Position(random.randint(1, GAME_WIN_SIZE['width'] - 2), random.randint(1, GAME_WIN_SIZE['height'] - 2))
        direct_pos = self.calc_direct(pos)
        self.head = Dot(pos, SNAKE_STYLE['head'])
        self.head.set_direct(direct_pos)
        self.body = [self.head]
        self.turning_points = {}

    @staticmethod
    def calc_direct(pos: Position):
        """
        计算初始行进方向
        防止出生点离边缘较近同时又朝边缘移动导致游戏过快结束
        :return:
        """
        # (0,1) 向下    (0,-1) 向上    (1,0) 向右    (-1,0) 向左
        # 右和下的边缘距离
        x, y = pos.x, pos.y
        u_dst, l_dst, r_dst, d_dst = y, x, GAME_WIN_SIZE['width']-x, GAME_WIN_SIZE['height']-y
        m = max(x, y, r_dst, d_dst)
        if m == u_dst:
            return Position(0, -1)
        elif m == l_dst:
            return Position(-1, 0)
        elif m == r_dst:
            return Position(1, 0)
        else:
            return Position(0, 1)

    def left(self):
        if self.head.direct_x in [1, -1]:
            return
        self.update_turing_points(-1, 0)

    def right(self):
        if self.head.direct_x in [1, -1]:
            return
        self.update_turing_points(1, 0)

    def up(self):
        if self.head.direct_y in [1, -1]:
            return
        self.update_turing_points(0, -1)

    def down(self):
        if self.head.direct_y in [1, -1]:
            return
        self.update_turing_points(0, 1)

    def update_turing_points(self, direct_x, direct_y):
        x = self.head.pos.x
        y = self.head.pos.y
        self.turning_points[(x, y)] = (direct_x, direct_y)

    def eat(self, food: Dot):
        return self.head == food

    def grows(self):
        """
        变长！
        :return:
        """
        tail = self.body[-1]
        pos = Position(tail.pos.x - tail.direct_x, tail.pos.y - tail.direct_y)
        new_tail = Dot(pos, SNAKE_STYLE['body'])
        new_tail.set_direct(Position(tail.direct_x, tail.direct_y))
        self.body.append(new_tail)

    def move(self):
        for b in self.body:
            b.pos.x += b.direct_x
            b.pos.y += b.direct_y

    def hit_wall(self):
        return self.head.pos.x <= 0 or self.head.pos.x >= GAME_WIN_SIZE['width'] - 1 or \
               self.head.pos.y <= 0 or self.head.pos.y >= GAME_WIN_SIZE['height'] - 1

    def hit_self(self):
        return self.head in self.body[1:]

    def update_direction(self):
        """
        针对每个拐点，更新body中每个点的运动方向
        当尾部通过一个拐点时，这个拐点需要被弹出
        :return:
        """
        for i, dot in enumerate(self.body):
            x, y = dot.pos.x, dot.pos.y
            direct = self.turning_points.get((x, y))
            if direct:
                dot.set_direct(Position(*direct))
                if i == len(self.body) - 1:
                    self.turning_points.pop((x, y))


class Food(Dot):
    def __init__(self):
        pos = Position(random.randint(1, GAME_WIN_SIZE['width'] - 2), random.randint(1, GAME_WIN_SIZE['height'] - 2))
        super().__init__(pos, 'o')
