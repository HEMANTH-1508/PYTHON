# 

import math

def Square(num):
    root = int(math.sqrt(num))
    return root**2 == num

def sum(num):
    sum = 0
    while num > 0:
        sum += num % 10
        num //= 10
    return sum

lower_range = int(input("Enter lower range: "))
upper_range = int(input("Enter upper range: "))

perfect_squares = []

for num in range(lower_range, upper_range+1):
    if Square(num) and sum(num) < 10:
        perfect_squares.append(num)


print(perfect_squares)
