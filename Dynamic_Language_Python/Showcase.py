# Import necessary classes
from src.Sudoku import Sudoku
from src.utils import paint_problem, paint_ans
'''
This is a showcase of how to use the Sudoku class to solve a Sudoku problem.
'''
if __name__ == "__main__":
    # Create a Sudoku instance and parse a grid string
    sudoku_instance = Sudoku()
    grid_str = "020000300900075002000900500008000003010000060705060900007003000600720001002000040"
    sudoku_instance.parse(grid_str)

    # Use the painter to print the Sudoku grid
    print("Sudoku Problem:")
    paint_problem(sudoku_instance)

    # Assuming you have a method to solve the Sudoku and get the solution
    solution = sudoku_instance.get_one_random_answer()

    # Use the painter to print the Sudoku solution
    print("\nSudoku Solution:")
    paint_ans(solution)