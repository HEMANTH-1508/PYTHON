# HARSHAD NUMBER

sum=0
z=0
n=int(input("Enter the number : "))
temp=n
while temp>0:
    z=temp%10
    sum=sum+z
    temp=temp//10
    
    
if n%sum==0:
    print("HARSHAD NUMBER")
else:
    print("NOT HARSHAD NUMBER")
    