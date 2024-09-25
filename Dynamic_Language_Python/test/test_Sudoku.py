import unittest
from Dynamic_Language_Python.src.Sudoku import Sudoku

class TestSudoku(unittest.TestCase):

    def setUp(self):
        self.sudoku_instance = Sudoku()
        grid_str = "017903600000080000900000507072010430000402070064370250701000065000030000005601720"
        self.sudoku_instance.parse(grid_str)

    def test_parse_valid(self):
        grid_str = "017903600000080000900000507072010430000402070064370250701000065000030000005601720"
        self.sudoku_instance.parse(grid_str)
        expected_grid = [
            [0, 1, 7, 9, 0, 3, 6, 0, 0],
            [0, 0, 0, 0, 8, 0, 0, 0, 0],
            [9, 0, 0, 0, 0, 0, 5, 0, 7],
            [0, 7, 2, 0, 1, 0, 4, 3, 0],
            [0, 0, 0, 4, 0, 2, 0, 7, 0],
            [0, 6, 4, 3, 7, 0, 2, 5, 0],
            [7, 0, 1, 0, 0, 0, 0, 6, 5],
            [0, 0, 0, 0, 3, 0, 0, 0, 0],
            [0, 0, 5, 6, 0, 1, 7, 2, 0]
        ]
        self.assertEqual(self.sudoku_instance.grid, expected_grid)

    def test_parse_invalid(self):
        invalid_grid_str = "01790360000008000090000050707201043000040207006437025070100006500003000000560172"
        with self.assertRaises(ValueError):
            self.sudoku_instance.parse(invalid_grid_str)

    def test_get_inference(self):
        grid_str = "017903600000080000900000507072010430000402070064370250701000065000030000005601720"
        self.sudoku_instance.parse(grid_str)
        candidates = self.sudoku_instance.get_inference()
        self.assertIsInstance(candidates, list)
        self.assertEqual(len(candidates), 9)
        self.assertEqual(len(candidates[0]), 9)
        self.assertIsInstance(candidates[0][0], set)

    def test_is_valid(self):
        # Test valid placements
        self.assertTrue(self.sudoku_instance.is_valid(0, 0, 5))
        self.assertTrue(self.sudoku_instance.is_valid(1, 1, 3))

        # Test invalid placements
        self.assertFalse(self.sudoku_instance.is_valid(0, 0, 1))  # 1 is already in the row
        self.assertFalse(self.sudoku_instance.is_valid(0, 0, 9))  # 9 is already in the column
        self.assertFalse(self.sudoku_instance.is_valid(0, 0, 7))  # 7 is already in the 3x3 box

    def test_solve(self):
        self.assertTrue(self.sudoku_instance.solve())
        solution = self.sudoku_instance.grid
        self.assertIsInstance(solution, list)
        self.assertEqual(len(solution), 9)
        for row in solution:
            self.assertEqual(len(row), 9)
            for num in row:
                self.assertIn(num, range(1, 10))

    def test_get_one_random_answer(self):
        solution = self.sudoku_instance.get_one_random_answer()
        self.assertIsInstance(solution, list)
        self.assertEqual(len(solution), 9)
        for row in solution:
            self.assertEqual(len(row), 9)
            for num in row:
                self.assertIn(num, range(1, 10))

if __name__ == '__main__':
    unittest.main()