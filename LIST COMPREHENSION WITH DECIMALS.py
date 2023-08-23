#list comprehension with decimals

import numpy as np
l_range=eval(input("Enter lower range: "))
u_range=eval(input("Enter upper range: "))

while True:
    res=None
    if(l_range<0 or u_range<0 or l_range>u_range):
        print("Enter a valid input")
        res=False
    break
a=[(round(x,2),round(x**2,2)) for x in np.arange(l_range,u_range+0.1,0.1)]
print(a)
