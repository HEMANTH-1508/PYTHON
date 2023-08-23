# HAPPY NUMBER 

def isHappy(n):    
    r = 0
    s = 0    
    while(n > 0):    
        r = n%10    
        s += r**2  
        n //= 10    
    return s  
        
n = int(input("ENTER A NUMBER : "))    
value = n   
     
while(value != 1 and value != 4):
    value = isHappy(value)    
     
if(value == 1):    
    print("GIVEN NUMBER IS A HAPPY NUMBER")
elif(value == 4):    
    print("GIVEN NUMBER IS NOT A HAPPY NUMBER")  
    
