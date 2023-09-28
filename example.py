from progress import ProgressBar, BarStyle
import time

if __name__ == '__main__':
    with ProgressBar(size=20, bar_style=BarStyle('+', '-', '|', '|')) as progress_bar:
        for i in range(101):
            progress_bar.display(i/100)
            time.sleep(.05)
    with ProgressBar(size=15, bar_style=BarStyle.preset('rocket')) as progress_bar:
        for i in range(101):
            progress_bar.display(i/100)
            time.sleep(.02)