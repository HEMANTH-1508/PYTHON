# perfect number

n=int(input("ENTER A NUMBER : "))
sum=0
l=[]
for i in range(1,n):
    if n%i==0:
        l.append(i)
        sum+=i
if sum==n:
    print("PERFECT NUMBER")
else:
    print("NOT A PERFECT NUMBER")
    
    