#!/usr/bin/env python3

import curses

screen = curses.initscr()

screen.addstr("Hello, I will be cleared in 2 seconds.")
screen.refresh()
curses.napms(2000)

screen.clear()

screen.refresh()
curses.napms(2000)

curses.endwin()
