# arrange in ascending and add element

lst=[1,2,3,4,5,6,7,8,9,10]

n=int(input("ENTER THE NEW ELEMENT : "))
p=int(input(" ENTER THE POSITION : "))

lst.insert(p,n)

print(sorted(lst))

