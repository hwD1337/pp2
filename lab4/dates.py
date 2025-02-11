#Import the datetime module and display the current date:
import datetime

x = datetime.datetime.now()
print(x)

#Return the year and name of weekday:
import datetime

x = datetime.datetime.now()

print(x.year)
print(x.strftime("%A"))

#Subtract Five Days from Current Date
from datetime import datetime, timedelta

def subtract_five_days():
    current_date = datetime.now()
    new_date = current_date - timedelta(days=5)
    return new_date
print(subtract_five_days())

#Print Yesterday, Today, Tomorrow
from datetime import datetime, timedelta

def print_yesterday_today_tomorrow():
    today = datetime.now()
    yesterday = today - timedelta(days=1)
    tomorrow = today + timedelta(days=1)
    
    print("Yesterday:", yesterday.strftime('%Y-%m-%d'))
    print("Today:", today.strftime('%Y-%m-%d'))
    print("Tomorrow:", tomorrow.strftime('%Y-%m-%d'))
print_yesterday_today_tomorrow()

#Drop Microseconds from Datetime
from datetime import datetime

def drop_microseconds():
    current_datetime = datetime.now()
    new_datetime = current_datetime.replace(microsecond=0)
    return new_datetime
print(drop_microseconds())

#Calculate Two Date Difference in Seconds
from datetime import datetime

def calculate_date_difference(date1, date2):
    delta = date2 - date1
    return delta.total_seconds()
date1 = datetime(2025, 2, 11, 20, 0, 0)
date2 = datetime(2025, 2, 12, 20, 0, 0)
print(calculate_date_difference(date1, date2))  # Output: 86400.0



