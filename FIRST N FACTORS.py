# first N factors

n=int(input("\nENTER A NUMBER : "))
num=int(input("\nENTER VALUE OF N : "))
l=[]
for i in range(1,n):
    if n%i==0:
        l.append(i)
print("\nFACTORS OF THE NUMBER ARE : ",l)

factors = []
for j in range(1, num+1):
    if num % j == 0:
        factors.append(j)
        if len(factors) == n:
            break

print("\nThe first", n, "factors of", num, "are:", factors)

         