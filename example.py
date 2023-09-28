from progress import ProgressBar, BarStyle
import time

if __name__ == '__main__':
    with ProgressBar() as progress_bar:
        for i in range(101):
            progress_bar.display(i/100)
            time.sleep(.05)
    with ProgressBar(size=15, bar_style=BarStyle(full='-', border_right='>')) as progress_bar:
        for i in range(101):
            progress_bar.display(i/100)
            time.sleep(.02)