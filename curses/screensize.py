#!/usr/bin/env python3

import curses

screen = curses.initscr()
num_rows, num_cols = screen.getmaxyx()
curses.endwin()

print("Rows:    %d" % num_rows)
print("Columns: %d" % num_cols)

