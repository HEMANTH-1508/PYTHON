# sum of digits = product of digits

n=int(input("ENTER A NUMBER : "))
k=n
sum=0
x=0

while n>0:
    x=n%10
    sum=sum+x
    n=n//10
    
print("The sum of digits is ",sum)

product=1
y=0
while k>0:
    y=k%10
    product=product*y
    k=k//10
    
print("The products of digits is ",product)

if sum==product:
    print("LUCKY NUMBER")
else:
    print("NOT LUCKY NUMBER")

    
    