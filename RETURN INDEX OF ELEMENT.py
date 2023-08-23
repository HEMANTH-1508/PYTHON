# to return index of target element else return -1 or -2

def findindex(n,t):
    l=[]
    l1=[-1,-1]
    for i in range(len(n)):
        if t not in n:
            return l1
        elif n[i] == t:
            l.append(i)
            continue
    return l

nums=[1, 2, 3, 1, 1, 4, 5, 2, 3, 4, 5]
target=int(input("ENTER THE TARGET NUMBER : "))

print(findindex(nums,target))
