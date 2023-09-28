class BarStyle:
    def __init__(self, full='#', empty=' ', first='[', last=']', border_left=None, border_right=None):
        if border_left is None:
            border_left = full
        if border_right is None:
            border_right = empty
        self.full = full
        self.empty = empty
        self.first = first
        self.last = last
        self.border_left = border_left
        self.border_right = border_right


class ProgressBar:
    __HIDE_CURSOR = "\x1b[?25l"
    __SHOW_CURSOR = "\x1b[?25h"

    def __init__(self, size=10, bar_style=None):
        self.__size = size
        if bar_style is None:
            bar_style = BarStyle('#', ' ', '[', ']')
        self.__bar_style = bar_style

    def display(self, progress):
        n_full_chars = round(progress * self.__size)
        n_empty_chars = self.__size - n_full_chars
        bar = ''
        bar += self.__bar_style.first
        if n_full_chars > 0:
            bar += self.__bar_style.full * (n_full_chars-1)
            bar += self.__bar_style.border_left
        if n_empty_chars > 0:
            bar += self.__bar_style.border_right
            bar += self.__bar_style.empty * (n_empty_chars-1)
        bar += self.__bar_style.last
        print(bar, end='\r')


    def __enter__(self):
        print(self.__HIDE_CURSOR, end='')
        return self
    
    def __exit__(self, *exc):
        print(self.__SHOW_CURSOR)