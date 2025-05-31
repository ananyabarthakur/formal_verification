
from z3 import *

def verify_sudoku(grid):
    """
    Verifies that the given Sudoku grid satisfies all rules.
    grid: 9x9 list of lists with integers (1..9)
    """
    s = Solver()

    # 9x9 matrix of integer variables (we'll use the given grid values)
    cells = [[Int(f'cell_{r}_{c}') for c in range(9)] for r in range(9)]

    # Add constraints: use given values from the grid
    for r in range(9):
        for c in range(9):
            if grid[r][c] != 0:
                s.add(cells[r][c] == grid[r][c])
            else:
                s.add(And(cells[r][c] >= 1, cells[r][c] <= 9))

    # Rows contain 1..9
    for r in range(9):
        s.add(Distinct(cells[r]))

    # Columns contain 1..9
    for c in range(9):
        s.add(Distinct([cells[r][c] for r in range(9)]))

    # 3x3 subgrids contain 1..9
    for box_row in range(3):
        for box_col in range(3):
            subgrid = []
            for r in range(3):
                for c in range(3):
                    subgrid.append(cells[3*box_row + r][3*box_col + c])
            s.add(Distinct(subgrid))

    if s.check() == sat:
        print("Sudoku solution is valid!")
    else:
        print("Sudoku solution is invalid!")

if __name__ == "__main__":
    # Sample valid Sudoku solution
    grid = [
        [5,3,4,6,7,8,9,1,2],
        [6,7,2,1,9,5,3,4,8],
        [1,9,8,3,4,2,5,6,7],
        [8,5,9,7,6,1,4,2,3],
        [4,2,6,8,5,3,7,9,1],
        [7,1,3,9,2,4,8,5,6],
        [9,6,1,5,3,7,2,8,4],
        [2,8,7,4,1,9,6,3,5],
        [3,4,5,2,8,6,1,7,9]
    ]

    verify_sudoku(grid)
