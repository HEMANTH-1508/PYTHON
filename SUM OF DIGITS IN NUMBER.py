# SUM OF THE DIGITS IN GIVEN NUMBER-16

sum=0
z=0
n=int(input("Enter the number : "))
while n>0:
    z=n%10
    sum=sum+z
    n=n//10
    
print("The sum of digits is ",sum)