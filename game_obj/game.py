import curses
import time

from utils import log
from . import stdscr, win
from .dot import Food, Snake


class Game:
    def __init__(self):
        self.delay_flag = True
        self.win = win
        self.food = Food()
        self.snake = Snake()
        self.flag = True  # 游戏继续进行的标志，撞墙或撞到自己则游戏结束
        self.white_keys = [ord('p'), ord('P'), ord('q'), ord('Q')]  # 暂停时接受的按键
        self.key_events = {
            curses.KEY_LEFT: self.snake.left,
            curses.KEY_RIGHT: self.snake.right,
            curses.KEY_UP: self.snake.up,
            curses.KEY_DOWN: self.snake.down,
            ord('q'): self.quit,
            ord('Q'): self.quit,
            ord('p'): self.pause,
            ord('P'): self.pause,
        }
        self.init_win()

    def init_win(self):
        self.win.nodelay(self.delay_flag)
        self.win.keypad(True)
        self.win.refresh()

    def pause(self):
        self.delay_flag = not self.delay_flag
        self.win.nodelay(self.delay_flag)

    def draw(self):
        # 加载游戏界面
        self.win.clear()
        self.win.border('#', '#', '#', '#')
        # 渲染食物和蛇的图像
        self.win.addstr(self.food.y, self.food.x, self.food.sign)
        for b in self.snake.body:
            self.win.addstr(b.y, b.x, b.sign)
        self.win.refresh()

    def listen_key_events(self):
        c = self.win.getch()
        # 游戏进入暂停，不接受除暂停和退出以外的操作
        if not self.delay_flag:
            while c not in self.white_keys:
                c = self.win.getch()
        m = self.key_events.get(c)
        return m() if m else None

    def start(self):
        # 初始化游戏对象
        while self.flag:
            self.draw()
            self.listen_key_events()
            self.check_ele_status()
            self.snake.move()
            time.sleep(0.33)
        self.__quit()

    @staticmethod
    def __quit():
        curses.nocbreak()
        stdscr.keypad(False)
        curses.echo()
        curses.endwin()

    def quit(self):
        self.flag = False

    def check_ele_status(self):
        """
        对游戏中各种状态进行判断
        :return:
        """
        if self.snake.hit_wall() or self.snake.hit_self():
            self.flag = False

        if self.snake.eat(self.food):
            self.snake.grows()
            self.food = Food()

        self.snake.update_direction()
