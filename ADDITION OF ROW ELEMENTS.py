#  ADDITION OF ELEMENTS OF THE ROW

a=[[1,2,3],[4,5,7],[3,2,2]]
rows=len(a)
col=len(a[0])

for i in range(0,rows):
    sumrow=0
    for j in range(0,col):
        sumrow += a[i][j]
    print("ROW",i+1,"is :",sumrow )
            