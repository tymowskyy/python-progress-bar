import time


class ProgressBar:

    def __init__(self, size=10, full_char='#', empty_char=' '):
        self.__size = size
        self.__full_char = full_char
        self.__empty_char = empty_char

    def display(self, progress):
        n_full_chars = round(progress * self.__size)
        n_empty_chars = self.__size - n_full_chars
        print('[' + self.__full_char * n_full_chars + self.__empty_char * n_empty_chars + ']')

if __name__ == '__main__':
    progress_bar = ProgressBar()
    for i in range(100):
       progress_bar.display(i/99)
       time.sleep(.1)