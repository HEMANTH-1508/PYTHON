# pip install python-dateutil

from datetime import datetime
from dateutil import relativedelta
 
d1=input("ENTER DATE IN THE FORM OF DD/MM/YYYY : ") 
d2=input("ENTER DATE IN THE FORM OF DD/MM/YYYY : ") 

start_date=datetime.strptime(d1, "%d/%m/%Y")
end_date=datetime.strptime(d2, "%d/%m/%Y")

delta=relativedelta.relativedelta(end_date,start_date)

print(delta.years,"YEARS",delta.months,"MONTHS",delta.days,"DAYS")

delta.years
d3=d1.split('/')
by=d3[2]
d4=d2.split('/')
dj=d3[2]

if(delta.years>=19 and by%4==0):
    print("I m a lucky adult")
elif delta.years<19:
    print("I m aspiring to become adult")
    
if by%400==0 or by%100!=0 and by%4==0:
    print("Birth year is leap Year")
else:
    print("Birth year is not a leap Year")

if dj%400==0 or dj%100!=0 and dj%4==0:
    print("Joining year is leap Year")
else:
    print("Joining year is not a leap Year")
    
    
    
    
    
    
    
