#  date 

from datetime import datetime,timedelta

now=datetime.now()
x=now-timedelta(days=3)

print(now)
print(x)

