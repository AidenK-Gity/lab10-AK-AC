# https://github.com/AidenK-Gity/lab10-AK-AC
# Partner 1: Aiden Kennedy
# Partner 2: Andrew Citra
import math

# First example
def add(a, b): 
    return a + b

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def logarithm(a, b):
    if a <= 0 or a == 1:
        raise ValueError("base must be positive and not equal to 1")
    if b <= 0:
        raise ValueError("b must be positive")
    return math.log(b, a)

def exponent(a, b):
    return a ** b

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
