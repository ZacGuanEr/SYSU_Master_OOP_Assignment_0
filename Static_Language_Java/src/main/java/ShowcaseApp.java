public class ShowcaseApp {

    public static void main(String[] args) {
        // Create a Sudoku instance and parse a grid string
        Sudoku sudokuInstance = new Sudoku();
        String gridStr = "020000300900075002000900500008000003010000060705060900007003000600720001002000040";
        sudokuInstance.parse(gridStr);

        // Use the utility class to print the Sudoku grid
        System.out.println("Sudoku Problem:");
        Utils.paintProblem(sudokuInstance);

        // Solve the Sudoku puzzle and get one valid solution
        int[][] solution = sudokuInstance.getOneRandomAnswer();

        // Use the utility class to print the Sudoku solution
        System.out.println("\nSudoku Solution:");
        Utils.paintAns(solution);
    }
}