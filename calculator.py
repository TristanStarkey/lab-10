#https://github.com/TristanStarkey/lab-11/blob/main/test_calculator.py
# Partner 1: Tristan Starkey
# Partner 2: Arthur Nikitin
import unittest
import math


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def mul(a, b):
    return a * b


def div(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b


def modulo(a, b):
    if b == 0:
        raise ValueError("Cannot modulo by zero.")
    return a % b


def power(base, exp):
    return base ** exp


def square_root(a):
    if a < 0:
        raise ValueError("Cannot take square root of a negative number.")
    return math.sqrt(a)


def logarithm(a, base=math.e):
    if a <= 0:
        raise ValueError("Logarithm undefined for non-positive values.")
    if base <= 0 or base == 1:
        raise ValueError("Logarithm base must be positive and not equal to 1.")
    return math.log(a, base)


def exp(a):
    return math.exp(a)


def hypotenuse(a, b):
    return math.hypot(a, b)
