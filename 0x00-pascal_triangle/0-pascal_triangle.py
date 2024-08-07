#!/usr/bin/python3
"""pascals Triangle
"""
def pascal_triangle(n):
    """Generate Pascal's Triangle up to n rows using a generator."""
    if n <= 0:
        yield []  # Return an empty row if n is less than or equal to 0
    else:
        previous_row = []
        for idx in range(n):
            # Create the current row with 1s
            row = [1] * (idx + 1)
            # Update the middle elements based on the previous row
            row = [
                row[i] if i == 0 or i == idx else previous_row[i - 1] + previous_row[i]
                for i in range(idx + 1)
            ]
            yield row
            previous_row = row

def factorial(num):
    if num == 0:
        return 1
    return num * factorial(num - 1)