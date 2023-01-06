#!/usr/bin/env python3

import curses

screen = curses.initscr()

pad = curses.newpad(100, 100)
pad.addstr("this text is thirty characters")

pad.refresh(0, 2, 5, 5, 15, 20)

curses.napms(3000)
curses.endwin()
