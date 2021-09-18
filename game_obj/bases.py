from dataclasses import dataclass

@dataclass
class Position:
    x: int
    y: int

class Dot:
    def __init__(self, pos: Position, sign):
        """
        游戏元素的基类，每个游戏元素都是由一个或多个在命令行中的坐标点所组成的
        :param x:
        :param y:
        :param sign:
        """
        # 坐标
        self.pos = pos

        # 文字显示
        self.sign = sign

        # 运动方向
        self.direct_x = 0
        self.direct_y = 0

    def set_direct(self, pos: Position):
        self.direct_x = pos.x
        self.direct_y = pos.y

    def __eq__(self, other):
        return self.pos.x == other.pos.x and self.pos.y == other.pos.y
