#!/usr/bin/python3
"""
Islander Perimeter
"""


def island_perimeter(grid):
  """
  Calculates the perimeter of the island in the grid.

  Args:
      grid: A list of lists of integers, where 0 represents water and 1 represents land.

  Returns:
      The perimeter of the island in the grid.
  """
  perimeter = 0
  rows, cols = len(grid), len(grid[0])

  for row in range(rows):
    for col in range(cols):
      if grid[row][col] == 1:
        # Check if cell at edge (all sides contribute)
        if row == 0 or row == rows - 1 or col == 0 or col == cols - 1:
          perimeter += 4
        else:
          # Check adjacent cells (subtract for shared edges)
          if grid[row - 1][col] == 0:
            perimeter += 1
          if grid[row + 1][col] == 0:
            perimeter += 1
          if grid[row][col - 1] == 0:
            perimeter += 1
          if grid[row][col + 1] == 0:
            perimeter += 1
  return perimeter
