# add two binary numbers

a = str(input("ENTER THE FIRST BINARY VALUE : "))
b = str(input("ENTER THE SECOND BINARY VALUE : "))

sum = bin(int(a,2) + int(b,2))

print(sum[2:])

