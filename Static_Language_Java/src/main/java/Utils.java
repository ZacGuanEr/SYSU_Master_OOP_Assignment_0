/**
 * Utility class for printing Sudoku grids.
 */
public class Utils {

    /**
     * Prints the Sudoku solution to the console with a formatted box.
     *
     * @param ans A 2D array representing the solved Sudoku grid.
     */
    public static void paintAns(int[][] ans) {
        for (int r = 0; r < ans.length; r++) {
            if (r % 3 == 0) {
                System.out.println("-------------------------");
            }
            for (int c = 0; c < ans[r].length; c++) {
                if (c % 3 == 0) {
                    System.out.print("| ");
                }
                System.out.print(ans[r][c] != 0 ? ans[r][c] + " " : "  ");
            }
            System.out.println("|");
        }
        System.out.println("-------------------------");
    }

    /**
     * Prints the Sudoku problem grid to the console with a formatted layout.
     *
     * @param gridInstance An instance of the Grid class containing the Sudoku problem.
     */
    public static void paintProblem(Grid gridInstance) {
        int[][] grid = gridInstance.getGrid();
        paintAns(grid);
    }
}