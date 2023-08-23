#pattern printing-1

n=int(input("ENTER A NUMBER : "))

for i in range(1,n):
    for j in range(1,i+1):
        print("*",end=" ")
    print()
 