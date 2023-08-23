# SEASONS

month = int(input("Enter the month (1-12): "))
day = int(input("Enter the day (1-31): "))

if month == 3 and day >= 20 or month == 4 or month == 5 or month == 6 and day < 21:
    season = "Spring"
elif month == 6 and day >= 21 or month == 7 or month == 8 or month == 9 and day < 22:
    season = "Summer"
elif month == 9 and day >= 22 or month == 10 or month == 11 or month == 12 and day < 21:
    season = "Fall"
else:
    season = "Winter"

print("The season is", season)