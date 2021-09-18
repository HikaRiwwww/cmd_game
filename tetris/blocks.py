from game_obj.bases import Position, Dot


class Blocks:
    """
    单个方块的类
    每次实例化随机出一个不同的形状和随机的摆放角度
    L Z —— 田 T
    """

    def __init__(self, body: []):
        self.body = body

    def new(self):
        pass

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
        pass

    @classmethod
    def _create_square(cls, pos: Position):
        """
        方形
        :return:
        """
        pass

    @classmethod
    def _create_t(cls, pos: Position):
        """
        T型
        :return:
        """
        pass

    @classmethod
    def _create_line(cls, pos: Position):
        """
        线型
        :return:
        """
        pass
