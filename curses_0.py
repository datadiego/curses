import curses
from curses import A_BOLD, A_UNDERLINE, wrapper

def main(stdscr):
    stdscr.clear()
    stdscr.addstr("AAAA")
    stdscr.addstr("BBBB", A_BOLD)
    stdscr.addstr(20, 0, "HELLO")
    stdscr.addstr(20, 20, "KTHXBYE", A_UNDERLINE)
    stdscr.refresh()
    stdscr.getch()

wrapper(main)