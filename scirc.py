print("""
░█▀▀░█░█░█▀▀░█▀█░█▀▄░█▀▀░█▀█░█▀█░█▀▀░░░▀█▀░█▀▄░█▀▀
░▀▀█░█░█░█░█░█▀█░█▀▄░█░░░█▀█░█░█░█▀▀░░░░█░░█▀▄░█░░
░▀▀▀░▀▀▀░▀▀▀░▀░▀░▀░▀░▀▀▀░▀░▀░▀░▀░▀▀▀░░░▀▀▀░▀░▀░▀▀▀
""")
from time import sleep
sleep(1)
print("Importing sys...")
import sys
print("Importing curses...")
import curses
print("Importing threading...")
import threading
print("Importing SugarCaneParse IRC...")
import scparseirc
print("Modules imported!")
print("Initializing curses...")
stdscr = curses.initscr()
curses.noecho()
if not curses.has_colors():
    print("Your terminal doesn't support color.")
    sys.exit(1)
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
print("Ending curses session...")
curses.endwin()
print("Exited successfully")