# getting list from user 2nd method

lst = []
n = int(input("Enter number of elements : "))

for i in range(0, n):
    ele = int(input("ENTER THE ELEMENT : "))
    lst.append(ele)  
print(sorted(lst))

        