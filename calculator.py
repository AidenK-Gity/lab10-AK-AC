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

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if a == 0:
        raise ZeroDivisionError("a cannot be 0")
    return b / a

def logarithm(a, b):
    if a <= 0 or a == 1:
        raise ValueError("base must be positive and not equal to 1")
    if b <= 0:
        raise ValueError("b must be positive")
    return math.log(b, a)

def exponent(a, b):
    return a ** b


