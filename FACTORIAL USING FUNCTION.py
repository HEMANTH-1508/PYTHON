# FACTORIAL USING FUNCTION
def fact(a):
    if a==0 or a==1:
        return 1
    else:
        return a*fact(a-1)
    
    
a=int(input("ENTER A NUMBER : "))
print("FACTORIAL OF",a,"IS",fact(a))    