# Task 1:
# Write a Python script to display the various Date Time formats.

# Current date and time
import datetime as dt
current_datetime = dt.datetime.now()
print("Current date and time:", current_datetime)

## Current year
import datetime as dt
current_datetime = dt.datetime.now()
year = current_datetime.year
print("Current year:", year)

## Month of year
import datetime as dt
current_datetime = dt.datetime.now()
month = current_datetime.strftime("%B")
print("Month of year:", month)

## Week number of the year
import datetime as dt
current_datetime = dt.datetime.now()
week = current_datetime.strftime("%W")
print("Week number of the year:", week)

## Weekday of the week
import datetime as dt
current_datetime = dt.datetime.now()
weekday = current_datetime.strftime("%w")
print("Weekday of the week:", weekday)

## Day of year
import datetime as dt
current_datetime = dt.datetime.now()
day_year = current_datetime.strftime("%j")
print("Day of the year:", day_year)

## Day of the month
import datetime as dt
current_datetime = dt.datetime.now()
day_month = current_datetime.strftime("%d")
print("Day of the month:", day_month)

## Day of week
import datetime as dt
current_datetime = dt.datetime.now()
day_week = current_datetime.strftime("%A")
print("Day of week:", day_week)

# Task 2:
# Write a Python program to print the dates of yesterday, today, tomorrow.

## Yesterday
import datetime as dt
from datetime import timedelta
today = dt.date.today()
yesterday = today - dt.timedelta(days = 1)
print("Yesterday:", yesterday)

## Today
import datetime as dt
from datetime import timedelta
today = dt.date.today()
print("Today:", today)

## Tomorrow
import datetime as dt
from datetime import timedelta
today = dt.date.today()
# print("Today: ", today)
tomorrow = today + dt.timedelta(days = 1)
print("Tomorrow:", tomorrow)

# Task 3:
# Write a Python program to add 5 seconds to the current time.

import datetime as dt
from datetime import timedelta
current_time = dt.datetime.now()
print("Current time:", current_time)
required_time = current_time + dt.timedelta(seconds = 5)
print("After adding 5 seconds:", required_time)

# Task 4
# Write a Python program to print the next 5 days starting today.

import datetime as dt
from datetime import timedelta
today = dt.datetime.today()
print("Today:", today)
for x in range(0, 5):
    next_5_days = today + dt.timedelta(days = 5)
    print(next_5_days)

# Task 5
# Write a Python program to convert Year/Month/Day to Day of Year using datetime module.

## Option 1
import datetime as dt
my_date_string = "2023/09/12"
my_date_time = dt.datetime.strptime(my_date_string, "%Y/%m/%d")
print("Today:", my_date_time)
print("Day of the year:", my_date_time.strftime("%j"))

## Option 2
current_datetime = dt.datetime.now()
print("Today:", current_datetime)
day_year = current_datetime.strftime("%j")
print("Day of the year:", day_year)

# Task 6
# Write a Python program to find the date of the first Monday of a given week.

## Option 1
import datetime as dt
from datetime import timedelta
current_date = dt.date.today()
print(current_date)
day_week = current_date.strftime("%A")
print("Day of week:", day_week)
weekday = current_date.strftime("%w")
print("Number of the weekday:", weekday)
for days in range(0,1):
    date_monday = current_date - dt.timedelta(days = 1)
    print("The first Monday of this week was:", date_monday)

## Option 2
import datetime as dt
week = "37"
year = "2023"
first_monday = "1"
date = dt.datetime.strptime(year + week + first_monday, "%Y%W%w")
print("First Monday of this week was:", date)

# Task 7
# Write a Python program to select all the Sundays in a specified year.

## Option 1
import datetime as dt
year = "2023"
for week in range(52):
    print(dt.datetime.strptime(year+str(week)+ "0", "%Y%W%w")) ## First Sunday: January 1st 2023, Last Sunday: December 24, 2023.

## Option 2
import datetime as dt
from datetime import timedelta
def all_sundays(year):
   d = dt.date(year, 1, 1)                  
   d += timedelta(days = 6 - d.weekday())  # First Sunday is January 1st 2023
   while d.year == year:
      yield d
      d += timedelta(days = 7)
for d in all_sundays(2023):
   print(d)
