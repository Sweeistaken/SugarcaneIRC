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
import irc.client
sleep(1)
stdscr = curses.initscr()
curses.noecho()
if not curses.has_colors():
    raise SystemError("Your terminal doesn't support color!")
rows, cols = stdscr.getmaxyx()
curses.start_color()
curses.init_pair(1, curses.COLOR_WHITE, curses.COLOR_BLUE)
curses.init_pair(3, curses.COLOR_WHITE, curses.COLOR_BLACK)
stdscr.bkgd(' ', curses.color_pair(3))
stdscr.attron(curses.color_pair(1))
stdscr.addstr("[File] [Edit] [Connect]" + " "*(int(cols)-29) + "[Help]")
stdscr.attroff(curses.color_pair(1))
stdscr.addstr("Test")
curses.init_pair(2, curses.COLOR_BLACK, curses.COLOR_GREEN)
stdscr.attron(curses.color_pair(2))
stdscr.addstr("ing")
stdscr.attroff(curses.color_pair(2))
stdscr.refresh()
sleep(3)
curses.endwin()
print("Exited successfully")