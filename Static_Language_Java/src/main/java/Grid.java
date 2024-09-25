/**
 * Grid class for Sudoku Solver in Java.
 */
public class Grid {

    final int GRID_SIZE = 9;
    final int BOX_SIZE = 3;
    int[][] grid;

    /**
     * Constructor for the Grid class.
     * Initializes the grid to null.
     */
    public Grid() {
        this.grid = null;
    }

    /**
     * Initializes the grid from a string input.
     *
     * @param gridStr the string representation of the grid
     * @throws IllegalArgumentException if the input string is invalid
     */
    public void init(String gridStr) throws IllegalArgumentException {
        parseInput(gridStr);
    }

    /**
     * Checks if the input string is valid.
     *
     * @param gridStr the string representation of the grid
     * @throws IllegalArgumentException if the input string does not have the correct length,
     *                                  contains non-digit characters, or contains out-of-range digits
     */
    public void checkInput(String gridStr) throws IllegalArgumentException {
        if (gridStr.length() != GRID_SIZE * GRID_SIZE) {
            throw new IllegalArgumentException("Input string does not have the correct length.");
        }
        for (char ch : gridStr.toCharArray()) {
            if (!Character.isDigit(ch)) {
                throw new IllegalArgumentException("Input string contains non-digit characters.");
            }
            int digit = Character.getNumericValue(ch);
            if (digit < 0 || digit > 9) {
                throw new IllegalArgumentException("Input string contains out-of-range digits.");
            }
        }
    }

    /**
     * Parses the input string to a 2D grid.
     *
     * @param inputString the string representation of the grid
     * @throws IllegalArgumentException if the input string is invalid
     */
    public void parseInput(String inputString) throws IllegalArgumentException {
        checkInput(inputString);
        grid = new int[GRID_SIZE][GRID_SIZE];
        for (int i = 0; i < GRID_SIZE; i++) {
            for (int j = 0; j < GRID_SIZE; j++) {
                grid[i][j] = Character.getNumericValue(inputString.charAt(i * GRID_SIZE + j));
            }
        }
    }

    /**
     * Gets a specific row from the grid.
     *
     * @param row the index of the row to retrieve
     * @return an array representing the row
     */
    public int[] getRow(int row) {
        return grid[row];
    }

    /**
     * Gets a specific column from the grid.
     *
     * @param col the index of the column to retrieve
     * @return an array representing the column
     */
    public int[] getColumn(int col) {
        int[] column = new int[GRID_SIZE];
        for (int row = 0; row < GRID_SIZE; row++) {
            column[row] = grid[row][col];
        }
        return column;
    }

    /**
     * Gets a specific box (3x3 sub-grid) from the grid.
     *
     * @param row the row index of the top-left cell of the box
     * @param col the column index of the top-left cell of the box
     * @return an array representing the box
     */
    public int[] getBox(int row, int col) {
        int[] box = new int[BOX_SIZE * BOX_SIZE];
        int startRow = (row / BOX_SIZE) * BOX_SIZE;
        int startCol = (col / BOX_SIZE) * BOX_SIZE;
        int index = 0;
        for (int r = startRow; r < startRow + BOX_SIZE; r++) {
            for (int c = startCol; c < startCol + BOX_SIZE; c++) {
                box[index++] = grid[r][c];
            }
        }
        return box;
    }

    /**
     * Gets a copy of the grid.
     *
     * @return a 2D array representing the grid
     */
    public int[][] getGrid() {
        int[][] gridCopy = new int[GRID_SIZE][GRID_SIZE];
        for (int i = 0; i < GRID_SIZE; i++) {
            gridCopy[i] = grid[i].clone();
        }
        return gridCopy;
    }

    /**
     * Gets an iterator to iterate over the grid.
     *
     * @return a 2D array representing the grid
     */
    public int[][] getGridIterator() {
        return grid;
    }
}