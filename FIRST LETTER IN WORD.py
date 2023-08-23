# print first alphabet in a word

a=input("ENTER A WORD : ")

s=sorted(a)
j="".join(s)
print("ALPHABETICAL ORDER : ",j)


l1=[]
l2=[]

for i in j:
    if i not in l1:
        l1.append(i)
    else:
        l2.append(i)
        
print(l1)        
print(l2)