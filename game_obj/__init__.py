import curses

HEIGHT = 20
WIDTH = 60

stdscr = curses.initscr()
curses.curs_set(0)  # 隐藏输入光标
h, w = stdscr.getmaxyx()
try:
    win = stdscr.subwin(HEIGHT, WIDTH, (h - HEIGHT) // 2, (w - WIDTH) // 2)
except Exception as e:
    raise Exception("窗口过小，无法加载游戏界面")
# stdscr.keypad(True)
