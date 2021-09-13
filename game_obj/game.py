import curses
import random
import time

from . import stdscr, HEIGHT, WIDTH, Y_START, X_START
from .dot import Dot


class Game:
    def __init__(self):
        self.win = stdscr.subwin(HEIGHT, WIDTH, Y_START, X_START)
        self.win.nodelay(True)
        self.win.keypad(True)
        self.win.refresh()

        head_x = random.randint(1, WIDTH - 2)
        head_y = random.randint(1, HEIGHT - 2)
        self.food = self.new_food()
        self.snake = [Dot(head_x, head_y, '■')]
        self.head = self.snake[0]
        self.turning_points = {
            (head_x, head_y): (1, 0),
        }
        self.update_direction()
        self.flag = True  # 游戏继续进行的标志，撞墙或撞到自己则游戏结束

    def update_direction(self):
        for i, dot in enumerate(self.snake):
            x, y = dot.x, dot.y
            direct = self.turning_points.get((x, y))
            if direct:
                dot.set_direct(*direct)
                if i == len(self.snake) - 1:
                    self.turning_points.pop((x, y))

    @staticmethod
    def new_food():
        x = random.randint(1, WIDTH - 2)
        y = random.randint(1, HEIGHT - 2)
        return Dot(x, y, 'o')

    def load_game_window(self):
        self.win.clear()
        self.win.border('#', '#', '#', '#')

    def draw(self):
        self.load_game_window()
        self.win.addstr(self.food.y, self.food.x, self.food.sign)
        for b in self.snake:
            self.win.addstr(b.y, b.x, b.sign)
        self.win.refresh()

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
        while self.flag:
            # 渲染图形
            self.draw()
            self.snake_move()
            c = self.win.getch()
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
            elif c in [ord('p'), ord('P')]:
                time.sleep(100000)
            if self.snake_eat():
                self.food = self.new_food()
                self.snake_grows()
            self.update_direction()
            self.check_status()
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

    def check_status(self):
        # log(self.hit_wall(), self.hit_self())
        if self.hit_wall() or self.hit_self():
            print('game over')
            self.flag = False

    def hit_wall(self):
        return self.head.x <= 0 or self.head.x >= WIDTH - 1 or \
               self.head.y <= 0 or self.head.y >= HEIGHT - 1

    def hit_self(self):
        for dot in self.snake[1:]:
            if self.head.x == dot.x and self.head.y == dot.y:
                return True
        return False
