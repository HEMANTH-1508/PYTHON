# FIBBONACI SERIES USING FUNCTIONS

def fib(n):
    if n<=1:
        return n
    else:
        return fib(n-1)+fib(n-2)
    
num=int(input("ENTER NUMBER : "))
for i in range(num):
    print(fib(i),end=" ")
              