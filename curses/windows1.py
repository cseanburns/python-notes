#!/usr/bin/env python3

import curses

screen = curses.initscr()

my_window = curses.newwin(15, 20, 0, 0)

my_window.addstr(4, 4, "Hello from 4,4")
my_window.addstr(5, 15, "Hello from 5,15 with a long string")

my_window.refresh()
curses.napms(2000)

screen.clear()
screen.refresh()

my_window.mvwin(10, 10)
my_window.refresh()
curses.napms(1000)

my_window.clear()
my_window.refresh()
curses.napms(1000)

curses.endwin()
