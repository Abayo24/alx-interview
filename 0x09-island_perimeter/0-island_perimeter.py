#!/usr/bin/python3
"""island_perimeter"""
def island_perimeter(grid):
    """Function to calculate the perimeter of the island in the grid"""
    perimeter = 0
    rows = len(grid)
    cols = len(grid[0])

    # Iterate through the grid
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:  # Land found
                # Check all four directions: up, down, left, right
                # Top boundary or water above
                if i == 0 or grid[i-1][j] == 0:
                    perimeter += 1
                # Bottom boundary or water below
                if i == rows-1 or grid[i+1][j] == 0:
                    perimeter += 1
                # Left boundary or water on the left
                if j == 0 or grid[i][j-1] == 0:
                    perimeter += 1
                # Right boundary or water on the right
                if j == cols-1 or grid[i][j+1] == 0:
                    perimeter += 1
    return perimeter
