# TRANSPOSE OF A MATRIX

a = [[4,6,7,8],[3,7,2,7],[7,3,7,5]]

rows = len(a)
cols = len(a[0])

transpose = [[0 for j in range(rows)] for i in range(cols)]

for i in range(cols):
    for j in range(rows):
        transpose[i][j] = a[j][i]

print("Original Matrix:")
print(*a, sep="\n")
print("Transposed Matrix:")
print(*transpose, sep="\n")
