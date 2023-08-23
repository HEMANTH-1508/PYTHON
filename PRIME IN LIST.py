# to print prime numbers in the list

l=[1,5,6,8,2,3,5]

p=[]
c=[]

for num in l:
    if num>1:
        for i in range(2,num):
            if num%i==0:
                c.append(num)
                break
        else:
            p.append(num)
            
print(p)