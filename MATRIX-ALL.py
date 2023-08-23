# MATRIX  VALUES FROM USER

print("\n3X3 MATRIX")
a=int(input("\nENTER NUMBER OF ROWS : "))
b=int(input("\nENTER NUMBER OF COLUMNS : "))
print()


matrix=[]
for i in range(0,a):
    row=[]   
    for j in range(0,b):
        ele=int(input("enter the element : "))
        row.append(ele)
    matrix.append(row) 
    
print("\nThe matrix is:")
for row in matrix:
    for ele in row:
        print(ele, end=" ")
    print()

# GIVING OPTION TO THE USER
print("\n       OPTIONS ")
print("\nSUM OF ELEMENTS OF ROWS : 1")
print("SUM OF ELEMENTS OF COLUMNS : 2")
print("SUM OF ELEMENTS OF DIAGNOL : 3")

p=int(input("\nENTER THE OPTION : "))

if p==1:
    # ADDITION OF ELEMENTS IN ROW
    for row in matrix:
        row_sum = 0
        for ele in row:
            row_sum += ele
        print("Sum of elements in row", matrix.index(row) + 1, "is:", row_sum)            
elif p==2:
    # ADDITION OF ELEMENTS IN A COLUMN
    for j in range(0, b):
        col_sum = 0
        for i in range(0, a):
            col_sum += matrix[i][j]
        print("Sum of elements in column", j + 1, "is:", col_sum)
elif p==3:
    # ADDITION OF ELEMENTS IN DIAGNOL
    diag_sum = 0
    for i in range(0, 3):
        diag_sum += matrix[i][i]
    print("Sum of elements along the diagonal is:", diag_sum)         
else:
    print("ENTER VALID OPTION")
    