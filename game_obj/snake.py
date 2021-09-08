import curses

HEIGHT = 20
WIDTH = 60
Y_START = 10
X_START = 10
SNAKE_STYLE = "*-"
TITLE_START_Y = 10
TITLE_START_X = 22
curses.initscr()
new_win = curses.newwin(HEIGHT, WIDTH, Y_START, X_START)
new_win.keypad(True)


def reset_window():
    new_win.clear()
    new_win.border('#', '#', '#', '#')


class Snake:
    def __init__(self):
        self.x = 22
        self.y = 10
        self.ini_style = ["*-", self.y, self.x]
        self.cur_style = self.ini_style

    def draw(self, style):
        reset_window()
        new_win.addstr(self.y, self.x, style)

    def left(self):
        self.x -= 1
        self.cur_style = ["*-", self.y, self.x]

    def right(self):
        self.x += 1
        self.cur_style = ["*-", self.y, self.x]

    def up(self):
        self.y -= 1
        self.cur_style = ["*-", self.y, self.x]

    def down(self):
        self.y += 1
        self.cur_style = ["*-", self.y, self.x]

    def grow(self):
        """
        吃了会长大
        :return:
        """
        pass


class Food:
    def __init__(self):
        self.x = 4
        self.y = 10
        self.ini_style = ["o", self.y, self.x]
        self.cur_style = self.ini_style


def load_game_window():
    new_win.clear()
    new_win.border('#', '#', '#', '#')
    new_win.addstr(TITLE_START_Y, TITLE_START_X, "PRESS S TO START")


def draw_snake():
    new_win.clear()
    new_win.border('#', '#', '#', '#')
    new_win.addstr(TITLE_START_Y, TITLE_START_X, "#-")


if __name__ == '__main__':
    load_game_window()
    s = Snake()
    while True:
        c = new_win.getch()
        if c in [ord('s'), ord('S')]:
            s.draw(s.ini_style)
            break
    while True:
        c = new_win.getch()
        if c == curses.KEY_LEFT:
            s.left()
        elif c == curses.KEY_RIGHT:
            s.right()
        if c == curses.KEY_UP:
            s.up()
        if c == curses.KEY_DOWN:
            s.down()
