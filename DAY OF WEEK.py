# Day of the week

from datetime import datetime
def daysofweek(y,m,d):
    days=["MONDAY","TUESDAY","WEDNESDAY","THURSDAY","FRIDAY","SATURDAY","SUNDAY"]
    return days[datetime(y,m,d).weekday()]

dd=int(input("enter the DATE : "))
mm=int(input("enter the MONTH : "))
yy=int(input("enter the YEAR : "))
print(daysofweek(yy,mm,dd))


