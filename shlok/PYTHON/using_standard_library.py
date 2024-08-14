import os

# Displaying all the attributes and methods of the module
print(dir(os))

# Using a method from the module
os.system('ls')  # On Windows, use 'dir' instead of 'ls'


import sys

# Displaying version information of Python
print("VERSION INFO", sys.version_info)

# Displaying only the version of Python
print("VERSION", sys.version)


import platform

# Displaying information about the platform
print(platform.platform())



import logging

# Configure the file for logging
logging_file = 'test.log'

# Make configurations for logging
logging.basicConfig(
    format='%(asctime)s : %(levelname)s : %(message)s',
    filename=logging_file,
    filemode='w',
    level=logging.DEBUG
)

# Use different log levels to log different messages
logging.debug("Start of the program")
logging.info("Doing something")
logging.warning("Warning message")
logging.error("Error message")
logging.critical("Critical error message")





import re

# Example patterns and matches
x = re.compile('a*')
print("Match for 'a':", x.match('a'))
print("Match for '':", x.match(''))
print("Match for 'aaa':", x.match('aaa'))
print("Match for 'aab':", x.match('aab'))
print("Match for 'b':", x.match('b'))

x = re.compile('a+')
print("Match for '':", x.match(''))
print("Match for 'b':", x.match('b'))

x = re.compile('[a-z]')
print("Match for 'ax':", x.match('ax'))

x = re.compile('[a-zA-Z0-9]+')
print("Match for 'aA0':", x.match('aA0'))

x = re.compile('[a-zA-Z0-9]{5}')
print("Match for 'a9A78':", x.match('a9A78'))

x = re.compile('[a-zA-Z0-9]{3,7}')
print("Match for 'aA3':", x.match('aA3'))

x = re.compile('[a-zA-Z0-9]+[a-z]$')
print("Match for 'aA0bD7fr4Xz':", x.match('aA0bD7fr4Xz'))

x = re.compile('^[a-z][a-zA-Z0-9]+')
print("Match for 'aA0bD7fr4Xz':", x.match('aA0bD7fr4Xz'))

x = re.compile('^[a-z]{1}\+[a-z]{1}$')
print("Match for 'a+b':", x.match('a+b'))

# Example to match a mobile number of India
x = re.compile(r'^\+91-[0-9]{10}$')
print("Match for '+91-9909453634':", x.match('+91-9909453634'))

# Example to match an email address
x = re.compile(r'^[a-z][a-z0-9._]+@([0-9a-z][0-9a-z-]+\.)+[a-z]{2,4}$')
print("Match for 'anup.chavda@serpentcs.com':", x.match('anup.chavda@serpentcs.com'))





from datetime import datetime as dtime

# Print today's date and time
current_datetime = dtime.now()
print("CURRENT DATETIME", current_datetime)

# Print current date and time
current_datetime = dtime.today()
print("CURRENT DATETIME", current_datetime)

# Extract and print date and time components
current_date = current_datetime.date()
print("Current Date", current_date)
current_time = current_datetime.time()
print("Current Time", current_time)
current_day = current_datetime.day
print("Day in the date", current_day)
current_month = current_datetime.month
print("Month in the date", current_month)
current_year = current_datetime.year
print("Year in the date", current_year)
current_hour = current_datetime.hour
print("Current Hour", current_hour)
current_minute = current_datetime.minute
print("Current Minute", current_minute)
current_second = current_datetime.second
print("Current Second", current_second)
current_microsecond = current_datetime.microsecond
print("Current Microsecond", current_microsecond)
current_weekday = current_datetime.weekday()
print("Current Weekday", current_weekday)

# Working with ISO format and other datetime functions
dt_max = dtime.max
print("dt_max", dt_max)
dt_min = dtime.min
print("dt_min", dt_min)

new_dtime = current_datetime.replace(day=25)
print("NEW DTIME", new_dtime)

curr_timestruct = current_datetime.timetuple()
print("Time Struct", curr_timestruct)

dt_str = current_datetime.strftime('%Y-%m-%d %H:%M:%S')
print("DT STR", dt_str)

new_dt = dtime.strptime(dt_str, '%Y-%m-%d %H:%M:%S')
print("NEW DT", new_dt)





from datetime import date

my_bday = date(1985, 6, 14)
curr_day = date.today()
diff = curr_day - my_bday
age = diff.days // 365
print("My age is:", age)




from datetime import date, timedelta

st_dt = date(2013, 1, 16)
en_dt = date(2013, 1, 31)
interval = (en_dt - st_dt).days

new_start_date = st_dt
while new_start_date <= en_dt:
    if new_start_date.weekday() == 6:  # Sunday
        interval -= 1
    new_start_date += timedelta(days=1)

print("Interval excluding Sundays:", interval)
