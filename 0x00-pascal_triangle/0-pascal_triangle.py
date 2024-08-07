#!/usr/bin/python3
"""pascals Triangle
"""
def pascal_triangle(n):
    if n <= 0:
        yield []
    else:
        for idx in range(n):
            triangle = [factorial(idx) // (factorial(i) * factorial(idx - i)) for i in range(idx + 1)]
            yield triangle

def factorial(num):
    if num == 0:
        return 1
    return num * factorial(num - 1)