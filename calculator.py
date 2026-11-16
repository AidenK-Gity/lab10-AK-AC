# https://github.com/AidenK-Gity/lab10-AK-AC
# Partner 1: Aiden Kennedy
# Partner 2: Andrew Citra
import math


def square_root(a):
    try:
        return math.sqrt(a)
    except ValueError as e:
        raise

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

def mul(a, b):
    return a * b

def div(a, b):
    if a == 0:
        raise ZeroDivisionError('division by zero')
    return b / a

def logarithm(a, b):
    if a <= 0 or a == 1 or b <= 0:
        raise ValueError('Invalid arguments')
    return math.log(a, b)

def exp(a, b):
    return a ** b
