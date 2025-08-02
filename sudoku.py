import random

# Size of the grid
N = 9

# Function to check if it's valid to place num in grid[row][col]
def is_safe(grid, row, col, num):
    for x in range(9):
        if grid[row][x] == num or grid[x][col] == num:
            return False

    # Check 3x3 subgrid
    startRow, startCol = 3 * (row // 3), 3 * (col // 3)
    for i in range(3):
        for j in range(3):
            if grid[startRow + i][startCol + j] == num:
                return False
    return True

# Backtracking solver to fill the Sudoku board
def solve(grid):
    for row in range(N):
        for col in range(N):
            if grid[row][col] == 0:
                nums = list(range(1, 10))
                random.shuffle(nums)
                for num in nums:
                    if is_safe(grid, row, col, num):
                        grid[row][col] = num
                        if solve(grid):
                            return True
                        grid[row][col] = 0
                return False
    return True

# Function to print the board
def print_board(grid):
    for row in grid:
        print(" ".join(str(num) for num in row))

# Main
sudoku_board = [[0 for _ in range(N)] for _ in range(N)]
solve(sudoku_board)
print("Generated Sudoku:")
print_board(sudoku_board)

        