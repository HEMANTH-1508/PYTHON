#SUM OF FIRST N NATURAL NUMBERS


n=int(input("Enter the value of n:"))
sum=0
for i in range(1,n+1):
    sum=sum+i
print("The sum of first",n,"natural numbers is",sum)
