# MATRIX ADDITION


a = [[1,2],[4,3]]
b = [[2,5],[3,1]]
c = [[0,0],[0,0]]

for i in range(len(a)):
    for j in range(len(b)):
        c[i][j] = a[i][j] + b[i][j]

for k in c:
   print(k)  #FOR PRINTING THE ANSWER IN MATRIX FORMAT
   
