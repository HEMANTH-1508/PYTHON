# frequency of the element 

l=[1,3,5,6,1,3,6,2,4,3,1]
s={}

for i in l:
    if i not in s:
        s[i]=l.count(i)
print(s)


