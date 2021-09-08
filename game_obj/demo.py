import curses
import time

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
new_win.border('#', '#', '#', '#')
new_win.addstr(TITLE_START_Y, TITLE_START_X, "Created by throne2")
new_win.refresh()
while True:
    c = new_win.getch()
    if c == ord('s'):
        new_win.erase()
        new_win.border('#', '#', '#', '#')
        new_win.addstr(TITLE_START_Y, TITLE_START_X, "#-")
        break

while True:
    c = new_win.getch()
    if c == curses.KEY_LEFT:
        TITLE_START_X -= 1
        new_win.erase()
        new_win.border('#', '#', '#', '#')
        new_win.addstr(TITLE_START_Y, TITLE_START_X, "#-")
    elif c == curses.KEY_RIGHT:
        TITLE_START_X += 1
        new_win.erase()
        new_win.border('#', '#', '#', '#')
        new_win.addstr(TITLE_START_Y, TITLE_START_X, "#-")
    if c == curses.KEY_UP:
        TITLE_START_Y -= 1
        new_win.erase()
        new_win.border('#', '#', '#', '#')
        new_win.addstr(TITLE_START_Y, TITLE_START_X, "#-")
    if c == curses.KEY_DOWN:
        TITLE_START_Y += 1
        new_win.erase()
        new_win.border('#', '#', '#', '#')
        new_win.addstr(TITLE_START_Y, TITLE_START_X, "#-")
