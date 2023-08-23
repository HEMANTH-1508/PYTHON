# TO CALUCLATE THE TAXI BILL

a=int(input("ENTER THE DISTANCE TRAVELLED : "))
b=int(input("ENTER THE TAXI NUMBER : "))
c=str(input("ENTER THE NAME : "))

print("TAXI NUMBER : ",b)
print("NAME : ",c)
print("DISTANCE TRAVELLED : ",a)

if a<1:
    c=a*25
    print("AMOUNT :",c,"Rs")
elif a>1 and a<=6:
    c=a*10
    print("AMOUNT :",c,"Rs")
elif a>6 and a<=12:
    c=a*15
    print("AMOUNT :",c,"Rs")
elif 12>1 and a<=18:
    c=a*20
    print("AMOUNT :",c,"Rs")
else:
    c=a*25
    print("AMOUNT :",c,"Rs")

