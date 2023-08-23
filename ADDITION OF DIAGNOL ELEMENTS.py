#  ADDITION OF ELEMENTS OF THE DIAGNOL

a=[[1,2,3],[4,5,7],[3,2,2]]
rows=len(a)
col=len(a[0])
diagnol=0

for k in range(0,rows):
    diagnol += a[k][k]
print("SUM OF DIAGNOL IS : ",diagnol)   
