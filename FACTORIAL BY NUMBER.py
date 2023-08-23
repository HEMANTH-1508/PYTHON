# 1!/1+2!/1+3!/3.......N!/N

def fact(a):
    if a==0 or a==1:
        return 1
    else:
        return a*fact(a-1)
    
    
a=int(input("ENTER A NUMBER : "))
sum=0
for i in range(1,a+1):
    sum += fact(i)/i
print(sum)      