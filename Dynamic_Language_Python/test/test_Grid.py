import unittest
from Dynamic_Language_Python.src.Grid import Grid

class TestGrid(unittest.TestCase):

    def setUp(self):
        self.grid_instance = Grid()

    def test_init(self):
        self.assertEqual(self.grid_instance.GRID_SIZE, 9)
        self.assertEqual(self.grid_instance.BOX_SIZE, 3)
        self.assertIsNone(self.grid_instance.grid)

    def test_check_input_valid(self):
        valid_grid_str = "017903600000080000900000507072010430000402070064370250701000065000030000005601720"
        try:
            self.grid_instance.check_input(valid_grid_str)
        except ValueError:
            self.fail("check_input() raised ValueError unexpectedly for valid input.")

    def test_check_input_invalid_length(self):
        invalid_length_grid_str = "01790360000008000090000050707201043000040207006437025070100006500003000000560172"
        with self.assertRaises(ValueError, msg="Input string does not have the correct length."):
            self.grid_instance.check_input(invalid_length_grid_str)

    def test_check_input_invalid_characters(self):
        invalid_char_grid_str = "01790360000008000090000050707201043000040207006437025070100006500003000000560172A"
        with self.assertRaises(ValueError, msg="Input string contains non-digit characters."):
            self.grid_instance.check_input(invalid_char_grid_str)

    def test_check_input_out_of_range_digits(self):
        invalid_digit_grid_str = "0179036000000800009000005070720104300004020700643702507010000650000300000056017233"
        with self.assertRaises(ValueError, msg="Input string contains out-of-range digits."):
            self.grid_instance.check_input(invalid_digit_grid_str)

    def test_parse_input(self):
        grid_str = "017903600000080000900000507072010430000402070064370250701000065000030000005601720"
        self.grid_instance.parse_input(grid_str)
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
        self.assertEqual(self.grid_instance.grid, expected_grid)

    def test_get_row(self):
        grid_str = "017903600000080000900000507072010430000402070064370250701000065000030000005601720"
        self.grid_instance.parse_input(grid_str)
        self.assertEqual(self.grid_instance.get_row(0), [0, 1, 7, 9, 0, 3, 6, 0, 0])

    def test_get_column(self):
        grid_str = "017903600000080000900000507072010430000402070064370250701000065000030000005601720"
        self.grid_instance.parse_input(grid_str)
        self.assertEqual(self.grid_instance.get_column(0), [0, 0, 9, 0, 0, 0, 7, 0, 0])

    def test_get_box(self):
        grid_str = "017903600000080000900000507072010430000402070064370250701000065000030000005601720"
        self.grid_instance.parse_input(grid_str)
        self.assertEqual(self.grid_instance.get_box(0, 0), [0, 1, 7, 0, 0, 0, 9, 0, 0])

    def test_get_grid(self):
        grid_str = "017903600000080000900000507072010430000402070064370250701000065000030000005601720"
        self.grid_instance.parse_input(grid_str)
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
        self.assertEqual(self.grid_instance.get_grid(), expected_grid)

if __name__ == '__main__':
    unittest.main()