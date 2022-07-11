import curses
from curses import A_BOLD, A_UNDERLINE, wrapper

def main(stdscr):
    stdscr.clear()
    stdscr.addstr(1, 1, "AAAA")
    stdscr.addstr("BBBB", A_BOLD)
    stdscr.addstr(5, 1, "HELLO", curses.A_BLINK)
    stdscr.addstr(6,1, "REVERSED", curses.A_REVERSE)
    stdscr.addstr(7,1, "STANDOUT", curses.A_STANDOUT)
    stdscr.addstr(8, 6, "KTHXBYE", A_UNDERLINE)
    stdscr.refresh()
    stdscr.getch()

wrapper(main)