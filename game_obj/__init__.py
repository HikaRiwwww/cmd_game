import curses

HEIGHT = 20
WIDTH = 60
Y_START = 10
X_START = 10

TITLE_START_Y = 10
TITLE_START_X = 22

stdscr = curses.initscr()
stdscr.keypad(True)


new_win = curses.newwin(HEIGHT, WIDTH, Y_START, X_START)
new_win.keypad(True)
