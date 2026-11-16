import math


def square_root(a):
    try:
        if a < 0:
            raise ValueError("cannot take the squre root of a negative number")
        return math.sqrt(a)
    except ValueError as e:
        print(f"Error: {e}")
        return None

def hypotenuse(a, b):
    try:
        return math.hypot(a, b)
    except (TypeError, ValueError) as e:
        print(f"Error: {e}")
        return None

def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    if a == 0:
        raise ZeroDivisionError('division by zero')
    return b / a

def log(a, b):
    if a <= 0 or a == 1 or b <= 0:
        raise ValueError('Invalid arguments')
    return math.log(a, b)

def exp(a, b):
    return a ** b
