import curses

HEIGHT = 20
WIDTH = 60
Y_START = 0
X_START = 0

stdscr = curses.initscr()
win = stdscr.subwin(HEIGHT, WIDTH, Y_START, X_START)
win.nodelay(True)
win.keypad(True)
win.refresh()

stdscr.keypad(True)
