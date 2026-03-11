#!/usr/bin/env python3

from platform import system, release
from printy import printy
import os
from time import sleep
import pyfiglet

def main():
    f = pyfiglet.Figlet(font='slant')

    os.system('clear')

    # change color by replacing first letter of second argument in printy
    # k - black, g - gray, w - white
    # <r - dark red, r - red, r> - light red
    # <n - dark green, n - green, n> light green
    # <y - dark yellow, y - yellow (default), y> - light yellow
    # <b - dark blue, b - blue, b> - light blue
    # <m - dark magenta, m - magenta, m> light magenta
    printy(f.renderText(system() + '\n'), 'yB')
    print(release(), '\n\n')
    sleep(2)

if __name__ == '__main__':
    main():
