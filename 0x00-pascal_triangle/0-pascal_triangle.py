#!/usr/bin/python3
"""pascals Triangle
"""
def pascal_triangle(n):
    triangle = []
    if (n <= 0):
        return triangle
    
    for idx in range(n):
        row = []
        for i in range(n+1):
            binom_coeff = factorial(idx) // (factorial(i) * factorial(idx - i))
            row.append(binom_coeff)
        triangle.append(row)
        
    return triangle

def factorial(num):
    if num == 0:
        return 1
    result = 1
    for k in range(1, num+1):
        result *= k
    return result