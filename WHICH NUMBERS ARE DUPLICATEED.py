#  TO SHOW WHICH NUMBERS ARE DUPLICATED

lst = []
n = int(input("Enter number of elements : "))

for i in range(0, n):
    ele = int(input("ENTER THE ELEMENT : "))
    lst.append(ele) 
     
print(sorted(lst))
l1=[]
l2=[]

for i in lst:
    if i not in l1:
        l1.append(i)
    else:
        l2.append(i)
        
print(l2)
        