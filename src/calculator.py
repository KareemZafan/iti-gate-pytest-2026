import math

def add(a, b): 
    return a + b

def subtract(a, b):
    return a - b

def multiply(a,b):
    return a * b

def divide(a, b):
    if b == 0:
        # try:
        #     return a / b
        # except: 
        #     return None
        raise ZeroDivisionError("Cannot divide by zero")
    return a / b    

def get_square_root(a):
    if a < 0:
       # raise ValueError("Negative numbers are not allowed") 
       return None
    return math.sqrt(a)

