#!/usr/bin/env python3

import subprocess

def uname_func():
    uname = "uname"
    uname_arg = "-a"
    print("\nGathering system info with %s command:\n" % uname)
    subprocess.call([uname, uname_arg])

def disk_func():
    diskspace = "df"
    diskspace_arg = "-h"
    print("\nGathering diskpace information %s command:\n" % diskspace)
    subprocess.call([diskspace, diskspace_arg])

def dir_func():
    directory = "ls"
    directory_arg = "-l"
    directory_arg_2 = "-t"
    print("\nListing files in directory %s command:\n" % directory)
    subprocess.call([directory, directory_arg, directory_arg_2])

def main():
    uname_func()
    disk_func()
    dir_func()

main()
