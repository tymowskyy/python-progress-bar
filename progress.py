import time


class ProgressBar:
    __HIDE_CURSOR = "\x1b[?25l"
    __SHOW_CURSOR = "\x1b[?25h"

    def __init__(self, size=10, full_char='#', empty_char=' '):
        self.__size = size
        self.__full_char = full_char
        self.__empty_char = empty_char

    def display(self, progress):
        n_full_chars = round(progress * self.__size)
        n_empty_chars = self.__size - n_full_chars
        print('[' + self.__full_char * n_full_chars + self.__empty_char * n_empty_chars + ']', end='\r')

    def __enter__(self):
        print(self.__HIDE_CURSOR, end='')
        return self
    
    def __exit__(self, *exc):
        print(self.__SHOW_CURSOR)

if __name__ == '__main__':
    with ProgressBar() as progress_bar:
        for i in range(100):
            progress_bar.display(i/99)
            time.sleep(.05)
    with ProgressBar(size=15, full_char='+', empty_char='-') as progress_bar:
        for i in range(100):
            progress_bar.display(i/99)
            time.sleep(.02)