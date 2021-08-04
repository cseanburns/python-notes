#!/usr/bin/python3

# Read in CSV file and create lists from column data in file
import csv

with open('data/example.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    dates = []
    colors = []
    for row in readCSV:
        color = row[3]
        date = row[0]

        dates.append(date)
        colors.append(color)

    print(dates)
    print(type(dates))
    print(colors)
    print(type(colors))
