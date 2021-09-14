import curses

HEIGHT = 20
WIDTH = 60
Y_START = 0
X_START = 0

stdscr = curses.initscr()
h, w = stdscr.getmaxyx()
try:
    win = stdscr.subwin(HEIGHT, WIDTH, (h - HEIGHT) // 2, (w - WIDTH) // 2)
except Exception as e:
    raise Exception("窗口过小，无法加载游戏界面")
win.nodelay(True)
win.keypad(True)
win.refresh()
stdscr.keypad(True)
