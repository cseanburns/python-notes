#!/usr/bin/env python3

import curses
import subprocess
import os

screen = curses.initscr()
screen.addstr("hello! dropping you in to a command prompt...\n")
print("program initialized...")
screen.refresh()
curses.napms(2000)

curses.endwin()

screen.addstr("I'll be waiting when you get back.\n")

print("about to open a command prompt...")
curses.napms(2000)

if os.name == 'nt':
    shell = 'cmd.exe'
else:
    shell = 'sh'
subprocess.call(shell)

screen.refresh()
curses.napms(2000)

curses.endwin()
