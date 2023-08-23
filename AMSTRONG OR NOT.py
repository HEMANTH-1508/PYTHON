# AMSTRONG  NUMBER OR NOT

sum=0
z=0
n=int(input("Enter the number : "))
temp=n
while temp>0:
    z=temp%10
    sum=sum+(z**3)
    temp=temp//10
    
    
if sum==n:
    print("AMSTRONG NUMBER")
else:
    print("NOT AMSTRONG NUMBER")