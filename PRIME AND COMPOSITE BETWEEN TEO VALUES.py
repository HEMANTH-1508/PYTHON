# PRIME AND COMPOSITE NUMBERS BETWEEN TWO VALUES

a=int(input("ENTER NUMBER a : "))
b=int(input("ENTER NUMBER b : "))

p=[]
c=[]

for num in range (a,b+1):
    if num>1:
        for i in range(2,num):
            if num%i==0:
                c.append(num)
                break
        else:
            p.append(num)
print("ALL THE PRIME NUMBERS BETWEEN a AND b IS/ARE : ",p,len(p))
print("ALL THE COMPOSITE NUMBERS BETWEEN a AND b IS/ARE : ",c,len(c)) 

               