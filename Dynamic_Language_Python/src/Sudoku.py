import logging
import random

from src.Grid import Grid

class Sudoku(Grid):
    """
    Sudoku class that extends the Grid class to provide additional functionality
    for parsing and solving Sudoku puzzles.

    Methods:
        __init__():
            Initialize the Sudoku object.

        parse(grid_str):
            Parse the input string and initialize the grid.

        get_inference():
            Generate and return the possible candidates for each cell in the grid.

        is_valid(row, col, num):
            Check if it's valid to place the number in the given cell.

        solve():
            Solve the Sudoku puzzle using backtracking.

        get_one_random_answer():
            Get one valid solution for the Sudoku puzzle.
    """
    def __init__(self):
        super().__init__()

    def parse(self, grid_str):
        """
        Parse the input string and initialize the grid.

        Args:
            grid_str (str): A string representing the Sudoku grid, where each character is a digit.
        """
        logging.info("Parsing Sudoku grid...")
        super().init(grid_str)
        logging.info("Parsed Sudoku grid successfully.")

    def get_inference(self):
        """
        Generate and return the possible candidates for each cell in the grid.

        Returns:
            list: A 2D list of sets, where each set contains the possible candidates for a cell.

        Raises:
            ValueError: If the grid is not initialized.
        """
        if self.grid is None:
            raise ValueError("Grid is not initialized. Please call parse() method first.")

        candidates = [[set(range(1, 10)) if self.grid[r][c] == 0 else {self.grid[r][c]}
                       for c in range(self.GRID_SIZE)] for r in range(self.GRID_SIZE)]

        for row in range(self.GRID_SIZE):
            for col in range(self.GRID_SIZE):
                if self.grid[row][col] == 0:
                    candidates[row][col] -= set(self.get_row(row))
                    candidates[row][col] -= set(self.get_column(col))
                    candidates[row][col] -= set(self.get_box(row, col))

        return candidates

    def is_valid(self, row, col, num):
        """
        Check if it's valid to place the number in the given cell.

        Args:
            row (int): Row index.
            col (int): Column index.
            num (int): Number to place.

        Returns:
            bool: True if valid, False otherwise.
        """
        # Check the row
        if num in self.get_row(row):
            return False
        # Check the column
        if num in self.get_column(col):
            return False
        # Check the 3x3 box
        if num in self.get_box(row, col):
            return False
        return True

    def solve(self):
        """
        Solve the Sudoku puzzle using backtracking.

        Returns:
            bool: True if solved, False otherwise.
        """
        for row in range(self.GRID_SIZE):
            for col in range(self.GRID_SIZE):
                if self.grid[row][col] == 0:
                    random_nums = list(range(1, 10))
                    random.shuffle(random_nums)
                    for num in random_nums:
                        if self.is_valid(row, col, num):
                            self.grid[row][col] = num
                            if self.solve():
                                return True
                            self.grid[row][col] = 0
                    return False
        return True

    def get_one_random_answer(self):
        """
        Get one valid solution for the Sudoku puzzle.

        Returns:
            list: A 2D list representing the solved Sudoku grid.
        """
        if self.solve():
            return self.grid
        else:
            raise ValueError("No solution exists for the given Sudoku puzzle.")