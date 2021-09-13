import curses
import random
import time

from utils import log
from . import stdscr, HEIGHT, WIDTH, Y_START, X_START, win
from .dot import Dot, Food, Snake


class Game:
    def __init__(self):
        self.win = win
        self.food = Food()
        self.snake = Snake()
        self.flag = True  # 游戏继续进行的标志，撞墙或撞到自己则游戏结束
        self.key_events = {
            curses.KEY_LEFT: self.snake.left,
            curses.KEY_RIGHT: self.snake.right,
            curses.KEY_UP: self.snake.up,
            curses.KEY_DOWN: self.snake.down,
            ord('q'): self.quit,
            ord('Q'): self.quit,

        }

    def load_game_window(self):
        self.win.clear()
        self.win.border('#', '#', '#', '#')

    def draw(self):
        # 加载游戏界面
        self.load_game_window()

        # 渲染食物和蛇的图像
        self.win.addstr(self.food.y, self.food.x, self.food.sign)
        for b in self.snake.body:
            self.win.addstr(b.y, b.x, b.sign)
        self.win.refresh()

    def listen_key_events(self, c):
        m = self.key_events.get(c)
        return m() if m else None

    def start(self):
        # 初始化游戏对象
        while self.flag:
            self.draw()
            self.snake.move()
            c = self.win.getch()
            self.listen_key_events(c)
            self.check_game_status()
            time.sleep(0.1)

        self.__quit()

    @staticmethod
    def __quit():
        curses.nocbreak()
        stdscr.keypad(False)
        curses.echo()
        curses.endwin()

    def quit(self):
        self.flag = False

    def check_game_status(self):
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
