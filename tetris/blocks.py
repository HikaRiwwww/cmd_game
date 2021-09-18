import random

from game_obj.bases import Position, Dot


class Blocks:
    """
    单个方块的类
    每次实例化随机出一个不同的形状和随机的摆放角度
    L Z —— 田 T
    """

    def __init__(self, body: []):
        self.body = body

    @classmethod
    def new(cls):
        m = {
            1: cls._create_l,
            2: cls._create_z,
            3: cls._create_square,
            4: cls._create_t,
            5: cls._create_line,
        }
        body = m.get(random.randint(1, 6))()
        return cls(body)

    @classmethod
    def _create_l(cls, pos: Position):
        """
        L型
        :return:
        """
        dots = []
        for i in range(3):
            dot = Dot(pos, "o")
            pos.x += 1
            dots.append(dot)
        for i in range(2):
            pos.y += 1
            dot = Dot(pos, "o")
            dots.append(dot)
        return dots

    @classmethod
    def _create_z(cls, pos: Position):
        """
        z型
        :param pos:
        :return:
        """
        dots = []
        for i in range(2):
            pos.x += 1
            dots.append(Dot(pos, "o"))
        pos.y += 1
        for i in range(2):
            pos.x += 1
            dots.append(Dot(pos, "o"))
        return dots

    @classmethod
    def _create_square(cls, pos: Position):
        """
        方形
        :return:
        """
        dots = []
        for i in range(2):
            for j in range(2):
                dots.append(Dot(pos, "o"))
                pos.x += 1
            pos.y += 1
        return dots

    @classmethod
    def _create_t(cls, pos: Position):
        """
        T型
        :return:
        """
        dots = []
        for i in range(3):
            dots.append(Dot(pos, 'o'))
            pos.x += 1
        pos.x -= 1
        pos.y += 1
        dots.append(Dot(pos, 'o'))
        return dots

    @classmethod
    def _create_line(cls, pos: Position):
        """
        线型
        :return:
        """
        dots = []
        for i in range(4):
            dots.append(Dot(pos, 'o'))
            pos.x += 1
        return dots

    def rotate(self):
        pass

    def left(self):
        pass

    def right(self):
        pass

    def down(self):
        pass
