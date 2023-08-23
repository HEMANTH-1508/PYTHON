# first monday of given month and year

import datetime

def first_monday(year, month):
    first_day = datetime.date(year, month, 1)
    days_to_monday = (7 - first_day.weekday()) % 7
    first_monday_date = first_day + datetime.timedelta(days=days_to_monday)
    return first_monday_date

y=int(input("ENTER YEAR : "))
m=int(input("ENTER MONTH : "))

print(first_monday(y,m))