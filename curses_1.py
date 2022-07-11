import curses
import time
from curses import wrapper

def main(stdscr):
    curses.init_pair(1, curses.COLOR_WHITE, curses.COLOR_BLUE)
    curses.init_pair(2, curses.COLOR_WHITE, curses.COLOR_CYAN)
    curses.init_pair(3, curses.COLOR_WHITE, curses.COLOR_RED)
    AZUL = curses.color_pair(1)
    CYAN = curses.color_pair(2)
    RED = curses.color_pair(3)
    stdscr.clear()
    for i in range(100):
        color = AZUL
        if i > 50:
            color = CYAN
        if i > 75:
            color = RED
        stdscr.clear()
        stdscr.addstr(1, 1, f"Count: {i}", color)
        stdscr.refresh()
        time.sleep(0.1)
    stdscr.getch()

wrapper(main)