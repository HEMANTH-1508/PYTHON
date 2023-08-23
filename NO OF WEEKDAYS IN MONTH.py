# no of weekdays in a month-1

import calendar

def weekdays(year, month):
    weekdays = 0
    for day in range(1, calendar.monthrange(year, month)[1] + 1):
        if calendar.weekday(year, month, day) < 5:
            weekdays += 1
    return weekdays

# Example usage
year = 2023
month = 4
weekdays_in_month = weekdays(year, month)
print(f"There are {weekdays_in_month} weekdays in {calendar.month_name[month]} {year}.")
