# to completly delete repeated numbers

l=[1,2,3,1,1,4,5,2,3,4]
l1=[]

for i in range(len(l)):
    if l.count(l[i])>1:
        continue
    else:
        l1.append(l[i])
print(l1) 