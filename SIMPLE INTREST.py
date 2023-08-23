#SIMPLE INTREST 

p=int(input("Enter the principle amount : "))
t=int(input("Enter the time : "))
gender=input("GENDER M/F")
sc=input("ENTER 'Y' OR 'N' :" )

if sc=='Y' and gender=='M':
    si=(p*12*t)/100
    print("The simple intrest is:",si)
elif sc=='Y' and gender=='F':
    si=(p*15*t)/100
    print("The simple intrest is:",si)
else:
    si=(p*10*t)/100
    print("The simple intrest is:",si) 





