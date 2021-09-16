from dataclasses import dataclass


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


@dataclass
class Position:
    x: int
    y: int
