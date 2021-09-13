from game_obj import stdscr


def log(*args, **kwargs):
    s = ""
    for arg in args:
        s += "{}, ".format(arg)
    for k, v in kwargs:
        s += "{}={},".format(k, v)
    stdscr.addstr(s[:-1] + "\n")
    stdscr.refresh()