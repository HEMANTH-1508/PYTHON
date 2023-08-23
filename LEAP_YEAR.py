#LEAP YEAR OR NOT

a=int(input("ENTER THE YEAR : "))

if a%4==0:
    if a%100==0:
        if a%400==0:
            print("GIVEN YEAR IS A LEAP YEAR")        
        else:
            print("GIVEN YEAR IS NOT A LEAP YEAR")    
    else:
        print("GIVEN YEAR  A LEAP YEAR")
else:
    print("GIVEN YEAR IS NOT A LEAP YEAR")
        