# finding number
matrix=[[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]]
n=int(input("Enter the number: "))

x=[]
y=[]
for row in matrix:
    if n in row:
        x.append(n)
        
    else:
        y.append(n)
if len(x)>0:
    print("True")
else:
    print("False")
