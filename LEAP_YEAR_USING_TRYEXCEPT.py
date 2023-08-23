# leap yeasar or not using try except code

try:
    input_year=int(input("ENTER THE YEAR : "))
    if input_year>0:
        if(input_year%400==0 or input_year%100!=0 and input_year%4==0):
            print("%d IS A LEAP YEAR"%input_year)
        else:
            print("%d IS A NOT LEAP YEAR"%input_year)

        x=input_year%4
        if x!=0:
            prev=input_year-x
            print("PREVIOUS LEAP YEAR IS : ",prev)
            print("UPCOMING LEAP YEAR IS : ",prev+4)
        else:
            print("NEXT LEAP YEAR : ",input_year+4 )
            print("PREVIOUS LEAP YEAR IS : ",input_year-4)

except:
    print("ENTER VALID YEAR")
      