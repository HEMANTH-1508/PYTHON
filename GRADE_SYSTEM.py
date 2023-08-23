# GRADE SYSTEM

a=int(input("ENTER THE MARKS OBTAINED IN SLOT A: "))
b=int(input("ENTER THE MARKS OBTAINED IN SLOT B: "))
c=int(input("ENTER THE MARKS OBTAINED IN SLOT C: "))
d=int(input("ENTER THE MARKS OBTAINED IN SLOT D: "))

avg=(a+b+c+d)/4

#if a>0 or a<100 and b>0 or b<100 and c>0 or c<100 and d>0 or d<100 :

if avg>90:
    print("YOU OBTAINED S GRADE")
elif avg<90 and avg>80:
    print("YOU OBTAINED A GRADE")
elif avg<80 and avg>70:
    print("YOU OBTAINED B GRADE")
elif avg<70 and avg>60:
    print("YOU OBTAINED C GRADE")
elif avg<60 and avg>50:
    print("YOU OBTAINED D GRADE")
else :
    print("YOU OBTAINED E GRADE")
#else:
#    print("ENTER VALID MARKS")



