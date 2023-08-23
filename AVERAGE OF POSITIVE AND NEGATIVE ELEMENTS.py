# getting list from user  ad finding average of positive and negative elements

lst = []
n = int(input("Enter number of elements: "))

for i in range(0, n):
    ele = int(input("Enter the element: "))
    lst.append(ele)
    
print("Sorted list: ", sorted(lst))

p = []
n = []
for j in lst:
    if j < 0:
        n.append(j)
    elif j > 0:
        p.append(j)
        
print("Positive elements: ", p)
print("Negative elements: ", n)

pos_sum = 0
neg_sum = 0
pos_count = 0
neg_count = 0

for k in p:
    pos_sum += k
    pos_count += 1
if pos_count > 0:
    pos_avg = pos_sum / pos_count
else:
    pos_avg = 0

for h in n:
    neg_sum += h
    neg_count += 1
if neg_count > 0:
    neg_avg = neg_sum / neg_count
else:
    neg_avg = 0

print("Average of positive elements:", pos_avg)
print("Average of negative elements:", neg_avg)

