#!/usr/bin/python3

import time
import datetime

start_year, start_month, start_day = input("Enter start year, month, day: ").split()
end_year, end_month, end_day = input("Enter end year, month, day: ").split()

start_date = datetime.date(int(start_year),
        int(start_month),
        int(start_day))
end_date = datetime.date(int(end_year),
        int(end_month),
        int(end_day))

print(start_date)
print(end_date)

if start_date > end_date:
    days = start_date - end_date
else:
    days = end_date - start_date

print(days)
