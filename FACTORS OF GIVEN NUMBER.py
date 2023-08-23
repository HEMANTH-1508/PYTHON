# factors of given number

n=int(input("ENTER A NUMBER : "))
l=[]
for i in range(1,n):
    if n%i==0:
        l.append(i)
print("FACTORS OF THE NUMBER ARE : ",l)        