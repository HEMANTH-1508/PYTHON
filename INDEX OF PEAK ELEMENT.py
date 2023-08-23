# return index of peak element 

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

nums=[1,5,6,8,2,3,5]
target=max(nums)

print(findindex(nums,target))