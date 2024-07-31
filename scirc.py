print("""

  ____                                                                   ___   ____     ____ 
 / ___|   _   _    __ _    __ _   _ __    ___    __ _   _ __     ___    |_ _| |  _ \\   / ___|
 \\___ \\  | | | |  / _` |  / _` | | '__|  / __|  / _` | | '_ \\   / _ \\    | |  | |_) | | |    
  ___) | | |_| | | (_| | | (_| | | |    | (__  | (_| | | | | | |  __/    | |  |  _ <  | |___ 
 |____/   \\__,_|  \\__, |  \\__,_| |_|     \\___|  \\__,_| |_| |_|  \\___|   |___| |_| \\_\\  \\____|
                  |___/                                                                      

""")
from time import sleep
import sys
import curses
import threading
sleep(5)
stdscr = curses.initscr()
curses.noecho()
if not curses.has_colors():
    raise SystemError("Your terminal doesn't support color!")
rows, cols = stdscr.getmaxyx()
curses.start_color()
curses.init_pair(1, curses.COLOR_WHITE, curses.COLOR_BLUE)
stdscr.bkgd(' ', curses.color_pair(1))
stdscr.attron(curses.color_pair(1) | curses.A_BOLD | curses.A_REVERSE)
stdscr.addstr("[File] [Edit] [Connect]" + " "*(int(cols)-29) + "[Help]\n")
stdscr.attroff(curses.color_pair(1) | curses.A_BOLD | curses.A_REVERSE)
stdscr.attron(curses.color_pair(1))
stdscr.addstr("Test")
stdscr.attroff(curses.color_pair(1))
curses.init_pair(2, curses.COLOR_WHITE, curses.COLOR_GREEN)
stdscr.attron(curses.color_pair(2))
stdscr.addstr("ing")
stdscr.attroff(curses.color_pair(2))
stdscr.refresh()
sleep(3)
curses.endwin()
print("Exited successfully")