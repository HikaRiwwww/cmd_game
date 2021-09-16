import curses

from game_obj.bases import Position
from snake.config import SCORE_BOARD, GUIDANCE


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

    @staticmethod
    def draw_dots(win, *dots):
        for dot in dots:
            win.addstr(dot.y, dot.x, dot.sign)

    def draw_text(self, pos, text):
        self.scr.addstr(pos.y, pos.x, text)
        self.scr.refresh()

    def create_game_win(self, height, width):
        h, w = self.scr.getmaxyx()
        try:
            win = self.scr.subwin(height, width, (h - height) // 2, (w - width) // 2)
            return win
        except Exception as e:
            print(e)
            raise Exception("窗口过小，无法加载游戏界面")

    @staticmethod
    def draw_game_win(win, border):
        win.clear()
        win.border(*border)
