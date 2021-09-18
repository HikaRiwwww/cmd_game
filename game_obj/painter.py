import curses

from game_obj.bases import Position
from snake.config import SCORE_BOARD, GUIDANCE, GAME_OVER_SIZE


class Painter:
    """
    用于处理图形绘制
    """

    def __init__(self):
        self.scr = curses.initscr()
        curses.curs_set(0)

    def draw_score_board(self, score):
        prompt = SCORE_BOARD['text']
        pp = Position(SCORE_BOARD['text_pos_x'], SCORE_BOARD['text_pos_y'])
        self.draw_text(pp, prompt)
        sp = Position(SCORE_BOARD['score_pos_x'], SCORE_BOARD['score_pos_y'])
        self.draw_text(sp, score)

    def draw_guidance(self):
        p = Position(GUIDANCE['text_pos_x'], GUIDANCE['text_pos_y'])
        for t in GUIDANCE['text']:
            self.draw_text(p, t)
            p.y += 1

    def draw_dots(self, win, *dots):
        for dot in dots:
            win.addstr(dot.y, dot.x, dot.sign)

    def draw_text(self, pos, text, win=None):
        if win:
            win.addstr(pos.y, pos.x, text)
        else:
            self.scr.addstr(pos.y, pos.x, text)
            self.scr.refresh()

    def draw_win_in_middle(self, height, width, nodelay=True, keypad=True):
        h, w = self.scr.getmaxyx()
        win = self.scr.subwin(height, width, (h - height) // 2, (w - width) // 2)
        win.nodelay(nodelay)
        win.keypad(keypad)
        return win

    def create_game_win(self, height, width):
        try:
            return self.draw_win_in_middle(height, width)
        except Exception as e:
            print(e)
            raise Exception("窗口过小，无法加载游戏界面")

    def repaint_game_win(self, win, border):
        win.clear()
        win.border(*border)

    def draw_game_over(self):
        """
        渲染游戏结束的画面
        :param win:
        :param border:
        :return:
        """
        height, width = GAME_OVER_SIZE['height'], GAME_OVER_SIZE['width']
        border = GAME_OVER_SIZE['border']
        pos = Position(GAME_OVER_SIZE['text_pos_x'], GAME_OVER_SIZE['text_pos_y'])
        text = GAME_OVER_SIZE['text']
        win = self.draw_win_in_middle(height, width, nodelay=False)
        win.border(*border)
        for t in text:
            self.draw_text(pos, t, win=win)
            pos.y += 2
        curses.curs_set(0)
        return win
