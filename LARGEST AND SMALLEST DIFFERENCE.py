# list program to determine nth largest and mth smallest and caluculate sum difference and product of them

l=[2,3,5,8,1,6]
l.sort()

x =int(input("enter the Nth smallest number : "))
y =int(input("enter the Nth largest number : "))

a=l[x-1]
b=l[-y]
print("the Nth smallest number is : ",a)
print("the Nth largest number is : ",b)


sum=a+b
sub=a-b
mul=a*b

print("the sum of Nth smallest and Nth largest number is : ",sum)
print("the difference of Nth smallest and Nth largest number is : ",sub)
print("the product of Nth smallest and Nth largest number is : ",mul)

