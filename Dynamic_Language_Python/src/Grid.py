"""
Grid module for Sudoku Solver.
"""
class Grid:
    """
    Grid class for representing a Sudoku grid.

    Attributes:
        GRID_SIZE (int): The size of the grid (9x9).
        BOX_SIZE (int): The size of each box (3x3).
        grid (list): A 2D list representing the Sudoku grid.

    Methods:
        __init__():
            Initialize the Grid object with default values for grid size, box size, and the grid itself.

        init(grid_str):
            Initialize the Grid object with a string representing the Sudoku grid.

        check_input(grid_str):
            Validate the input string for the Sudoku grid.

        parse_input(input_string):
            Parse the input string into a 2D grid (list of lists).

        get_row(row):
            Get the values in a specific row of the grid.

        get_column(col):
            Get the values in a specific column of the grid.

        get_box(row, col):
            Get the values in a specific 3x3 box of the grid.

        get_grid():
            Get the deep copy of current state of the grid.

        __iter__():
            Make the grid iterable.
    """
    def __init__(self):
        """
        Initialize the Grid object with default values for grid size, box size, and the grid itself.
        """
        self.GRID_SIZE = 9
        self.BOX_SIZE = 3
        self.grid = None

    def init(self, grid_str):
        """
        Initialize the Grid object with a string representing the Sudoku grid.

        Args:
            grid_str (str): A string representing the Sudoku grid, where each character is a digit.
        """
        self.parse_input(grid_str)

    def check_input(self, grid_str):
        """
        Validate the input string for the Sudoku grid.

        Args:
            grid_str (str): A string representing the Sudoku grid, where each character is a digit.

        Raises:
            ValueError: If the input string does not have the correct length.
            ValueError: If the input string contains non-digit characters.
            ValueError: If the input string contains out-of-range digits.
        """
        if len(grid_str) != self.GRID_SIZE ** 2:
            raise ValueError("Input string does not have the correct length.")
        if not all(char.isdigit() for char in grid_str):
            raise ValueError("Input string contains non-digit characters.")
        if not all(0 <= int(char) <= 9 for char in grid_str):
            raise ValueError("Input string contains out-of-range digits.")

    def parse_input(self, input_string):
        """
        Parse the input string into a 2D grid (list of lists).

        Args:
            input_string (str): A string representing the Sudoku grid, where each character is a digit.

        Raises:
            ValueError: If the input string does not have the correct length.
            ValueError: If the input string contains non-digit characters.
            ValueError: If the input string contains out-of-range digits.
        """
        self.check_input(input_string)
        self.grid = [[int(input_string[i * self.GRID_SIZE + j]) for j in range(self.GRID_SIZE)]
                     for i in range(self.GRID_SIZE)]

    def get_row(self, row):
        """
        Get the values in a specific row of the grid.

        Args:
            row (int): The index of the row to retrieve.

        Returns:
            list: A list of integers representing the values in the specified row.
        """
        return self.grid[row]

    def get_column(self, col):
        """
        Get the values in a specific column of the grid.

        Args:
            col (int): The index of the column to retrieve.

        Returns:
            list: A list of integers representing the values in the specified column.
        """
        return [self.grid[row][col] for row in range(self.GRID_SIZE)]

    def get_box(self, row, col):
        """
        Get the values in a specific 3x3 box of the grid.

        Args:
            row (int): The row index of a cell within the desired 3x3 box.
            col (int): The column index of a cell within the desired 3x3 box.

        Returns:
            list: A list of integers representing the values in the specified 3x3 box.
        """
        start_row = (row // self.BOX_SIZE) * self.BOX_SIZE
        start_col = (col // self.BOX_SIZE) * self.BOX_SIZE
        return [self.grid[r][c] for r in range(start_row, start_row + self.BOX_SIZE)
                for c in range(start_col, start_col + self.BOX_SIZE)]
    def get_grid(self):
        """
        Get the deep copy of current state of the grid.

        Returns:
            list: A list of lists representing the current state of the grid.
        """
        return [row[:] for row in self.grid]

    def __iter__(self):
        """
        Make the grid iterable.

        Returns:
            iterator: An iterator over the rows of the grid.
        """
        return iter(self.grid)