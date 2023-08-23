# squares of even and odd elements

lst = []
n = int(input("Enter number of elements: "))

for i in range(0, n):
    ele = int(input("Enter the element: "))
    lst.append(ele)
    
print("Sorted list: ", sorted(lst))

p = []
n = []
for j in lst:
    if j%2== 0:
        n.append(j)
    else:
        p.append(j)
        
print("ODD elements: ", p)
print("EVEN elements: ", n)

even_sum = 0
odd_sum = 0
even_count = 0
odd_count = 0

for k in p:
    even_sum += k
    even_count += 1
if even_count > 0:
    even_sqr = (even_sum**2)
else:
    even_sqr = 0

for h in n:
    odd_sum += h
    odd_count += 1
if odd_count > 0:
    odd_sqr = (odd_sum**2)
else:
    odd_sqr = 0

print("Average of even elements:", even_sqr)
print("Average of odd elements:", odd_sqr)

