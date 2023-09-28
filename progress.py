from dataclasses import dataclass

@dataclass
class BarStyle:
    full: str = '#'
    empty: str = ' '
    first: str = '['
    last: str = ']'
    border_left: str = None
    border_right: str = None

    def __post_init__(self):
        if self.border_left is None:
            self.border_left = self.full
        if self.border_right is None:
            self.border_right = self.empty

    @classmethod
    def preset(cls, name: str):
        return cls(
            **{
            'rocket': {'full': '  ', 'empty': '  ', 'first': '🌎', 'last': '🌕', 'border_left': '🔥🚀', 'border_right': ''},
            'blocky': {'full': '█', 'empty': ' ', 'first': '█', 'last': '█'},
            'arrow': {'full': '-', 'border_right': '>'},
            }[name])

class ProgressBar:
    __HIDE_CURSOR = "\x1b[?25l"
    __SHOW_CURSOR = "\x1b[?25h"

    def __init__(self, size: int=10, bar_style: BarStyle=None):
        self.__size = size
        if bar_style is None:
            bar_style = BarStyle('#', ' ', '[', ']')
        self.__bar_style = bar_style

    def __get_bar(self, n_full_chars) -> str:
        n_empty_chars = self.__size - n_full_chars
        bar = ''
        bar += self.__bar_style.first
        if n_full_chars > 0:
            if n_full_chars > len(self.__bar_style.border_left):
                bar += self.__bar_style.full * (n_full_chars-len(self.__bar_style.border_left))
            bar += self.__bar_style.border_left[-min(n_full_chars, len(self.__bar_style.border_left)):]
        if n_empty_chars > 0:
            bar += self.__bar_style.border_right[:min(n_empty_chars, len(self.__bar_style.border_right))]
            if n_empty_chars > len(self.__bar_style.border_right):
                bar += self.__bar_style.empty * (n_empty_chars-len(self.__bar_style.border_right))
        bar += self.__bar_style.last
        return bar

    def display(self, progress:float) -> None:
        print(self.__get_bar(round(progress * self.__size)), end='\r')


    def __enter__(self):
        print(self.__HIDE_CURSOR, end='')
        return self
    
    def __exit__(self, *exc):
        print(self.__SHOW_CURSOR)