from turtle import*

import time

bgcolor('black')
speed(0)
hideturtle()
for i in range(120):
    color('red')
    circle(i)
    color('green')
    circle(i*0.5)
    right(5)
    forward(5)
for i in range(120,240):
    color('red')
    circle(i)
    color('green')
    circle(i*0.5)
    right(0.5)
    forward(0.5)
    
    
done()

time.sleep(10)
