#!/usr/bin/python3
"""pascals Triangle
"""
def pascal_triangle(n):
    """Generate Pascal's Triangle up to n rows using a generator."""
    if n <= 0:
        yield []  # Return an empty row if n is less than or equal to 0
    else:
        previous_row = [1]
        yield previous_row
        
        for idx in range(1, n):
            # Create the current row with 1s
            row = [1] * (idx + 1)
            # Update the middle elements based on the previous row
            row[1:idx] = [previous_row[i - 1] + previous_row[i]
                          for i in range(1, idx)]
            yield row
            previous_row = row

def factorial(num):
    """Calculate factorial"""
    if num == 0:
        return 1
    return num * factorial(num - 1)