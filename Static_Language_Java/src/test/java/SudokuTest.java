// Unit test for Sudoku.java
import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;
import java.util.Set;

class SudokuTest {

    @Test
    void testParseValidInput() {
        Sudoku sudoku = new Sudoku();
        String validInput = "530070000600195000098000060800060003400803001700020006060000280000419005000080079";
        sudoku.parse(validInput);
        assertNotNull(sudoku.getGrid());
    }

    @Test
    void testParseInvalidInput() {
        Sudoku sudoku = new Sudoku();
        String invalidInput = "123";
        Exception exception = assertThrows(IllegalArgumentException.class, () -> sudoku.parse(invalidInput));
        assertEquals("Input string does not have the correct length.", exception.getMessage());
    }

    @Test
    void testIsValid() {
        Sudoku sudoku = new Sudoku();
        String validInput = "530070000600195000098000060800060003400803001700020006060000280000419005000080079";
        sudoku.parse(validInput);
        assertTrue(sudoku.isValid(0, 2, 4));
        assertFalse(sudoku.isValid(0, 2, 5));
    }

    @Test
    void testSolve() {
        Sudoku sudoku = new Sudoku();
        String validInput = "530070000600195000098000060800060003400803001700020006060000280000419005000080079";
        sudoku.parse(validInput);
        assertTrue(sudoku.solve());
        int[][] solvedGrid = sudoku.getGrid();
        assertNotNull(solvedGrid);
        assertEquals(9, solvedGrid[8][8]);
    }

    @Test
    void testGetInference() {
        Sudoku sudoku = new Sudoku();
        String validInput = "530070000600195000098000060800060003400803001700020006060000280000419005000080079";
        sudoku.parse(validInput);
        Set<Integer>[][] inferences = sudoku.getInference();

        assertNotNull(inferences);

        // Check some specific cells for expected inferences
        assertTrue(inferences[0][2].contains(1));
        assertTrue(inferences[0][2].contains(2));
        assertTrue(inferences[0][2].contains(4));

        // Check a cell that should have no inferences (already filled)
        assertEquals(1, inferences[0][1].size());
        assertTrue(inferences[0][1].contains(3));
    }

    @Test
    void testGetOneRandomAnswer() {
        Sudoku sudoku = new Sudoku();
        String validInput = "530070000600195000098000060800060003400803001700020006060000280000419005000080079";
        sudoku.parse(validInput);
        int[][] randomAnswer = sudoku.getOneRandomAnswer();
        assertNotNull(randomAnswer);
        assertEquals(9, randomAnswer[8][8]);
    }
}