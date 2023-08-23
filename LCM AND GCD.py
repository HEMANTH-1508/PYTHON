# GCD AND LCM -3

from math import gcd

l=input("ENTER THE NUMBERS GIVING ',' AFTER EVERY NUMBER : ")
s=l.split(",")
nums=list(map(int,s))
gcd_s=gcd(*nums)

print(gcd_s)

x=1
for i in nums:
    x=(x*i)

lcm=x//gcd_s    
print(lcm)    
