from Grid import Grid

def paint_ans(ans):
    """
    Print the Sudoku solution to the console with colorful box.

    Args:
        ans (list): A 2D list representing the solved Sudoku grid.
    """
    for r in range(len(ans)):
        if r % 3 == 0:
            print("-" * 25)
        for c in range(len(ans[r])):
            if c % 3 == 0:
                print("|", end=" ")
            print(ans[r][c] if ans[r][c] != 0 else " ", end=" ")
        print("|")
    print("-" * 25)


def paint_problem(grid_instance: Grid):
    """
    Print the Sudoku problem grid to the console with a formatted layout.

    Args:
        grid_instance (Grid): An instance of the Grid class containing the Sudoku problem.
    """
    grid = grid_instance.get_grid()
    for r in range(len(grid)):
        if r % 3 == 0:
            print("-" * 25)
        for c in range(len(grid[r])):
            if c % 3 == 0:
                print("|", end=" ")
            print(grid[r][c] if grid[r][c] != 0 else " ", end=" ")
        print("|")
    print("-" * 25)

