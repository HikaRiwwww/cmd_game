import curses
from . import stdscr
from . import new_win
from .snake import Snake, Food


class Game:
    def __init__(self):
        pass

    def load_game_window(self):
        new_win.clear()
        new_win.border('#', '#', '#', '#')

    def draw(self, *obj):
        self.load_game_window()
        for o in obj:
            s, y, x = o.cur_style
            stdscr.addstr("s:{}, y{}, x{}\n".format(s, y, x))
            stdscr.refresh()
            new_win.addstr(y, x, s)
            new_win.refresh()

    def start(self):
        # 初始化游戏对象
        s = Snake()
        f = Food()
        # 渲染图形
        self.draw(s, f)
        while True:
            # 监听事件
            c = new_win.getch()
            if c == curses.KEY_LEFT:
                s.left()
            elif c == curses.KEY_RIGHT:
                s.right()
            elif c == curses.KEY_UP:
                s.up()
            elif c == curses.KEY_DOWN:
                s.down()
            self.draw(s, f)
    def listen_event(self):
        """
        监听键盘事件
        :return:
        """
        pass
