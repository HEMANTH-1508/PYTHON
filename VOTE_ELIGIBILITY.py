# VOTE ELIGIBILITY

a=int(input("ENTER YOUR AGE: "))

if a<1:
    print("ENTER VALID AGE")
elif a>18 :
    print("THE PERSON IS ELIGIBLE TO VOTE")
else:
    b=18-a
    print("YOU STILL NEED",b,"YEARS TO VOTE")
