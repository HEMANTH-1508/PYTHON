# to remove duplicates from array

l=[1,2,3,1,1,4,5,2,3,4]
l1=[]

for i in l:
    if i not in l1:
        l1.append(i)
print(l1)       
