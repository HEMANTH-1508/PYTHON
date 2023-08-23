# list comprehension

lower = int(input("Enter the lower range: "))
upper = int(input("Enter the upper range: "))

result = [(i, i**2) for i in range(lower, upper+1)]

print(result)

