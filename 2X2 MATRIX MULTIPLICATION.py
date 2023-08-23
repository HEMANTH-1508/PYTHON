# 2X2 MATRIX MULTIPLICATION

a = [[1,2],[3,4]]
b = [[2,1],[3,2]]
c = [[0,0],[0,0]]

for i in range(len(a)):
    for j in range(len(b)):
        for k in range(len(b)):
            c[i][j] += a[i][k] * b[k][j]

for k in c:
    print(k)  
