import curses
from curses import A_BOLD, A_UNDERLINE, wrapper

def main(stdscr):
    curses.init_pair(1, curses.COLOR_BLUE, curses.COLOR_YELLOW)
    BLUE_YELLOW = curses.color_pair(1)
    stdscr.clear()
    stdscr.addstr(1, 1, "AAAA")
    stdscr.addstr("BBBB", A_BOLD)
    stdscr.addstr(5, 1, "HELLO", curses.A_BLINK)
    stdscr.addstr(6,1, "REVERSED", curses.A_REVERSE)
    stdscr.addstr(7,1, "STANDOUT", curses.A_STANDOUT)
    stdscr.addstr(8, 6, "KTHXBYE", A_UNDERLINE)
    stdscr.addstr(10, 10, "COLOR TEST", BLUE_YELLOW)
    stdscr.refresh()
    stdscr.getch()

wrapper(main)