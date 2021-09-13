import curses
import random
import time

from utils import log
from . import stdscr, TITLE_START_X, TITLE_START_Y
from . import new_win
from .snake import Dot


class Game:
    def __init__(self):
        head_x = random.randint(1, TITLE_START_X - 1)
        head_y = random.randint(1, TITLE_START_Y - 1)
        self.food = self.new_food()
        self.snake = [Dot(head_x, head_y, '■')]
        self.head = self.snake[0]
        self.turning_points = {
            (head_x, head_y): (1, 0),
        }
        self.update_direction()

    def update_direction(self):
        for i, dot in enumerate(self.snake):
            direct = self.turning_points.get((dot.x, dot.y))
            if direct:
                dot.set_direct(*direct)
                if i == len(self.snake) - 1:
                    self.turning_points.pop(dot.x, dot.y)

    @staticmethod
    def new_food():
        return Dot(random.randint(1, TITLE_START_X - 1), random.randint(1, TITLE_START_Y - 1), 'o')

    def load_game_window(self):
        new_win.clear()
        new_win.border('#', '#', '#', '#')

    def draw(self):
        self.load_game_window()
        new_win.addstr(self.food.y, self.food.x, self.food.sign)
        for b in self.snake:
            new_win.addstr(b.y, b.x, b.sign)
        new_win.refresh()

    def update_turing_points(self, direct_x, direct_y):
        x = self.head.x
        y = self.head.y
        self.turning_points[(x, y)] = (direct_x, direct_y)

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

    def snake_eat(self):
        return self.snake[0].x == self.food.x and self.snake[0].y == self.food.y

    def start(self):
        # 初始化游戏对象
        while True:
            # 渲染图形
            self.snake_move()
            self.draw()
            c = new_win.getch()
            if c == curses.KEY_LEFT:
                self.left()
            elif c == curses.KEY_RIGHT:
                self.right()
            elif c == curses.KEY_UP:
                self.up()
            elif c == curses.KEY_DOWN:
                self.down()
            elif c in [ord('q'), ord('Q')]:
                self.quit()
                return
            if self.turning_points:
                self.update_direction()
            if self.snake_eat():
                self.food = self.new_food()
                self.snake_grows()
            time.sleep(0.2)

    @staticmethod
    def quit():
        curses.nocbreak()
        stdscr.keypad(False)
        curses.echo()
        curses.endwin()

    def snake_grows(self):
        tail = self.snake[-1]
        x = tail.x - tail.direct_x
        y = tail.y - tail.direct_y
        new_tail = Dot(x, y, '□')
        new_tail.set_direct(tail.direct_x, tail.direct_y)
        self.snake.append(new_tail)

    def snake_move(self):
        for b in self.snake:
            b.x += b.direct_x
            b.y += b.direct_y
