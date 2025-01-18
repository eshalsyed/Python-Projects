# Time converter

import pytz # Work with timezones
from datetime import datetime # Work with dates and time

#Intro
print("\nTime Zone Converter!")
print("\nHere are the available timezones: ")
for timez in pytz.all_timezones:
    print(timez)
print("\nIn this program you will be able to convert your currect timezone to another!\n")

# User inputs
ask_time = input("Enter your currect date and time(YYYY-MM-DD & HH:MM:SS): ")
ask_timezone = input("Enter your currect timezone: ")
ask_convert = input("Enter the timezone to convert to: ")

# Format in which datetimes go
format = "%Y-%m-%d %H:%M:%S"


try:
    # Converting string into datetime object
    str_change = datetime.strptime(ask_time,format)
    
    # Putting the converted datetime with the correct timezone
    tz = pytz.timezone(ask_timezone)
    actual_tz = tz.localize(str_change)
    
    # Converting that timezone
    change = pytz.timezone(ask_convert)
    converted = actual_tz.astimezone(change)
    print(f"The time in {change} is {converted.strftime('%Y-%m-%d %H:%M:%S')}")

except ValueError:
    print("The date time format is incorrect. Please ensure it follows the YYYY-MM-DD HH:MM:SS format.")
except pytz.UnknownTimeZoneError:
    print("One or both of the timezones you entered are invalid. Please check and try again.")
