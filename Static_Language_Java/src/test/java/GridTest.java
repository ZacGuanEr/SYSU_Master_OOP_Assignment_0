import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

class GridTest {

    @Test
    void testInitValidInput() {
        Grid grid = new Grid();
        String validInput = "530070000600195000098000060800060003400803001700020006060000280000419005000080079";
        grid.init(validInput);
        assertNotNull(grid.getGrid());
    }

    @Test
    void testInitInvalidInputLength() {
        Grid grid = new Grid();
        String invalidInput = "123";
        Exception exception = assertThrows(IllegalArgumentException.class, () -> grid.init(invalidInput));
        assertEquals("Input string does not have the correct length.", exception.getMessage());
    }

    @Test
    void testInitInvalidInputCharacters() {
        Grid grid = new Grid();
        String invalidInput = "53007000060019500009800006080006000340080300170002000606000028000041900500008007A";
        Exception exception = assertThrows(IllegalArgumentException.class, () -> grid.init(invalidInput));
        assertEquals("Input string contains non-digit characters.", exception.getMessage());
    }

    @Test
    void testGetRow() {
        Grid grid = new Grid();
        String validInput = "530070000600195000098000060800060003400803001700020006060000280000419005000080079";
        grid.init(validInput);
        int[] expectedRow = {5, 3, 0, 0, 7, 0, 0, 0, 0};
        assertArrayEquals(expectedRow, grid.getRow(0));
    }

    @Test
    void testGetColumn() {
        Grid grid = new Grid();
        String validInput = "530070000600195000098000060800060003400803001700020006060000280000419005000080079";
        grid.init(validInput);
        int[] expectedColumn = {5, 6, 0, 8, 4, 7, 0, 0, 0};
        assertArrayEquals(expectedColumn, grid.getColumn(0));
    }

    @Test
    void testGetBox() {
        Grid grid = new Grid();
        String validInput = "530070000600195000098000060800060003400803001700020006060000280000419005000080079";
        grid.init(validInput);
        int[] expectedBox = {5, 3, 0, 6, 0, 0, 0, 9, 8};
        assertArrayEquals(expectedBox, grid.getBox(0, 0));
    }

    @Test
    void testGetGrid() {
        Grid grid = new Grid();
        String validInput = "530070000600195000098000060800060003400803001700020006060000280000419005000080079";
        grid.init(validInput);
        int[][] gridCopy = grid.getGrid();
        assertNotSame(grid.getGrid(), gridCopy);
        assertArrayEquals(grid.getGrid(), gridCopy);
    }
}