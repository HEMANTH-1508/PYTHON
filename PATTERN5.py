# PATTERN PRINTING-5

n = int(input("Enter the number of rows: "))

for i in range(1, n+1):
    
    for j in range(1, i+1):
        
        value = 2 ** (2 * (j-1))
        
        print(value, end=" ")
        
    print()


