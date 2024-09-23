import unittest
from maze import Maze


class Tests(unittest.TestCase):
    def test_maze_create_cells(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(len(m1._cells), num_rows)
        self.assertEqual(len(m1._cells[0]), num_cols)

    def test_maze_create_cells_large(self):
        num_cols = 20
        num_rows = 15
        m1 = Maze(0, 0, num_rows, num_cols, 20, 20)
        self.assertEqual(len(m1._cells), num_rows)
        self.assertEqual(len(m1._cells[0]), num_cols)

    def test_break_entrance_and_exit(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(m1._cells[0][0].has_left_wall, False)
        self.assertEqual(m1._cells[-1][-1].has_right_wall, False)

    def test_reset_cell_visited(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)

        # visited cells should be set to false again
        for row in m1._cells:
            for cell in row:
                self.assertEqual(cell.visited, False)


if __name__ == "__main__":
    unittest.main()
