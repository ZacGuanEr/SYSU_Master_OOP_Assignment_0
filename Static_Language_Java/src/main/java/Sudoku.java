/**
*  Sudoku.java
* This class is used to solve Sudoku puzzles.
*/
import java.util.*;
import java.util.logging.Logger;

/**
 * Sudoku class for solving Sudoku puzzles.
 * Extends the Grid class to provide additional functionality specific to Sudoku.
 */
public class Sudoku extends Grid {

    private static final Logger logger = Logger.getLogger(Sudoku.class.getName());

    /**
     * Constructor for the Sudoku class.
     * Initializes the Sudoku grid.
     */
    public Sudoku() {
        super();
    }

    /**
     * Parses the Sudoku grid from a string input.
     *
     * @param gridStr the string representation of the Sudoku grid
     * @throws IllegalArgumentException if the input string is invalid
     */
    public void parse(String gridStr) {
        logger.info("Parsing Sudoku grid...");
        super.init(gridStr);
        logger.info("Parsed Sudoku grid successfully.");
    }

    /**
     * Gets the possible candidates for each cell in the Sudoku grid.
     *
     * @return a 2D array of sets, where each set contains the possible candidates for a cell
     * @throws IllegalStateException if the grid is not initialized
     */
    public Set<Integer>[][] getInference() {
        if (this.grid == null) {
            throw new IllegalStateException("Grid is not initialized. Please call parse() method first.");
        }

        Set<Integer>[][] candidates = new HashSet[GRID_SIZE][GRID_SIZE];
        for (int row = 0; row < GRID_SIZE; row++) {
            for (int col = 0; col < GRID_SIZE; col++) {
                if (this.grid[row][col] == 0) {
                    candidates[row][col] = new HashSet<>(Arrays.asList(1, 2, 3, 4, 5, 6, 7, 8, 9));
                } else {
                    candidates[row][col] = new HashSet<>(Collections.singleton(this.grid[row][col]));
                }
            }
        }

        for (int row = 0; row < GRID_SIZE; row++) {
            for (int col = 0; col < GRID_SIZE; col++) {
                if (this.grid[row][col] == 0) {
                    for (int num : this.getRow(row)) {
                        candidates[row][col].remove(num);
                    }
                    for (int num : this.getColumn(col)) {
                        candidates[row][col].remove(num);
                    }
                    for (int num : this.getBox(row, col)) {
                        candidates[row][col].remove(num);
                    }
                }
            }
        }

        return candidates;
    }

    /**
     * Checks if placing a number in a specific cell is valid.
     *
     * @param row the row index of the cell
     * @param col the column index of the cell
     * @param num the number to place in the cell
     * @return true if the placement is valid, false otherwise
     */
    public boolean isValid(int row, int col, int num) {
        if (Arrays.stream(this.getRow(row)).anyMatch(x -> x == num)) {
            return false;
        }
        if (Arrays.stream(this.getColumn(col)).anyMatch(x -> x == num)) {
            return false;
        }
        return Arrays.stream(this.getBox(row, col)).noneMatch(x -> x == num);
    }

    /**
     * Solves the Sudoku puzzle using backtracking.
     *
     * @return true if the puzzle is solved, false otherwise
     */
    public boolean solve() {
        for (int row = 0; row < GRID_SIZE; row++) {
            for (int col = 0; col < GRID_SIZE; col++) {
                if (this.grid[row][col] == 0) {
                    List<Integer> randomNums = new ArrayList<>();
                    for (int i = 1; i <= 9; i++) {
                        randomNums.add(i);
                    }
                    Collections.shuffle(randomNums);

                    for (int num : randomNums) {
                        if (isValid(row, col, num)) {
                            this.grid[row][col] = num;
                            if (solve()) {
                                return true;
                            }
                            this.grid[row][col] = 0;
                        }
                    }
                    return false;
                }
            }
        }
        return true;
    }

    /**
     * Gets one valid random solution for the Sudoku puzzle.
     *
     * @return a 2D array representing the solved Sudoku grid
     * @throws IllegalArgumentException if no solution exists for the given puzzle
     */
    public int[][] getOneRandomAnswer() {
        if (solve()) {
            return this.getGrid();
        } else {
            throw new IllegalArgumentException("No solution exists for the given Sudoku puzzle.");
        }
    }
}