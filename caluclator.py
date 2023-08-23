# caluclator

import time

def sum(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    return a / b

def float_div(a, b):
    return a // b

def mod(a, b):
    return a % b

def pow(a, b):
    return a ** b

while True:
    print("\n1=ADDITION OF NUMBERS")
    print("\n2=SUBTRACTION OF NUMBERS")
    print("\n3=MULTIPLICATION OF NUMBERS")
    print("\n4=DIVISION OF NUMBERS")
    print("\n5=FLOAT DIVISION OF NUMBERS")
    print("\n6=MODULUS OF NUMBERS")
    print("\n7=EXPONENT OF NUMBERS")
    print("\n8=EXIT CALCULATOR")
    
    x = int(input("SELECT THE CORRESPONDING FUNCTION 1-8: "))
    
    if x == 8:
        print("\nExiting calculator...")
        break
    
    a = float(input("\nENTER NUMBER A: "))
    b = float(input("\nENTER NUMBER B: "))
    
    if x == 1:
        print("\nADDITION OF TWO NUMBERS IS:", sum(a, b))
    elif x == 2:
        print("\nSUBTRACTION OF TWO NUMBERS IS:", sub(a, b))
    elif x == 3:
        print("\nMULTIPLICATION OF TWO NUMBERS IS:", mul(a, b))
    elif x == 4:
        print("\nDIVISION OF TWO NUMBERS IS:", div(a, b))
    elif x == 5:
        print("\nFLOAT DIVISION OF TWO NUMBERS IS:", float_div(a, b))
    elif x == 6:
        print("\nMODULUS OF TWO NUMBERS IS:", mod(a, b))
    elif x == 7:
        print("\nPOWER OF TWO NUMBERS IS:", pow(a, b))
    else:
        print("\nENTER VALID INPUT")
    
    time.sleep(1)
