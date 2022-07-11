import curses, time


def main(stdscr: 'curses._CursesWindow'):
    curses.init_pair(1, curses.COLOR_WHITE, curses.COLOR_BLUE)
    curses.init_pair(2, curses.COLOR_WHITE, curses.COLOR_CYAN)
    curses.init_pair(3, curses.COLOR_WHITE, curses.COLOR_RED)
    AZUL = curses.color_pair(1)
    CYAN = curses.color_pair(2)
    RED = curses.color_pair(3)
    
    #Cuidado con el tamaño de la ventana o puede dar error si se desborda
    win_counter = curses.newwin(1, 10, 10, 10)
    
    for i in range(100):
        win_counter.clear()
        color = AZUL
        if i > 50:
            color = CYAN
        if i > 75:
            color = RED
        win_counter.addstr(f"Count: {i}", color)
        win_counter.refresh()
        time.sleep(0.1)
    stdscr.getch()

curses.wrapper(main)