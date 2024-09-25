from cell import Cell
import time
import random


class Maze:

    def __init__(
        self, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, win=None, seed=None
    ):
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self.win = win

        self._cells = []

        if seed:
            random.seed(seed)

        self._create_cells()
        self._break_entrance_and_exit()
        self._break_walls_r(0, 0)
        self._reset_cell_visited()

    def _create_cells(self):
        # fills _cells with list of cells. Each top-level list is a column of Cell objects.
        # Once the matric is populated it should call its _draw_cell() method on each cell
        # [ [cell, cell, cell], [cell, cell, cell], [cell, cell, cell] ]

        for _ in range(self.num_rows):
            cell_row = []
            for _ in range(self.num_cols):
                cell_row.append(Cell(self.win))

            self._cells.append(cell_row)

        for i, row in enumerate(self._cells):
            for j, cell in enumerate(row):
                self._draw_cell(i, j)

    def _draw_cell(self, i, j):
        if self.win is None:
            return

        # top-left corner
        x1 = (j * self.cell_size_x) + self.x1
        y1 = (i * self.cell_size_y) + self.y1

        # bottom-right corner
        x2 = ((j + 1) * self.cell_size_x) + self.x1
        y2 = ((i + 1) * self.cell_size_y) + self.y1

        self._cells[i][j].draw(x1, y1, x2, y2)
        self._animate()

    def _animate(self):
        if self.win is None:
            return
        self.win.redraw()
        time.sleep(0.05)

    def _break_entrance_and_exit(self):
        self._cells[0][0].has_left_wall = False
        self._draw_cell(0, 0)

        self._cells[-1][-1].has_right_wall = False
        self._draw_cell(len(self._cells) - 1, len(self._cells[0]) - 1)

    def _break_walls_r(self, i, j):
        # DFS through cells
        self._cells[i][j].visited = True

        while True:
            to_visit = []

            # above
            if i > 0 and not self._cells[i - 1][j].visited:
                to_visit.append((i - 1, j))
            # below
            if i < self.num_rows - 1 and not self._cells[i + 1][j].visited:
                to_visit.append((i + 1, j))
            # left
            if j > 0 and not self._cells[i][j - 1].visited:
                to_visit.append((i, j - 1))
            # right
            if j < self.num_cols - 1 and not self._cells[i][j + 1].visited:
                to_visit.append((i, j + 1))

            #  if there's where to move from current cell, break out
            if len(to_visit) == 0:
                self._draw_cell(i, j)
                return

            next_idx = to_visit[random.randrange(len(to_visit))]

            # above
            if next_idx[0] == i - 1:
                self._cells[i][j].has_top_wall = False
                self._cells[i - 1][j].has_bottom_wall = False
            # below
            if next_idx[0] == i + 1:
                self._cells[i][j].has_bottom_wall = False
                self._cells[i + 1][j].has_top_wall = False
            # left
            if next_idx[1] == j - 1:
                self._cells[i][j].has_left_wall = False
                self._cells[i][j - 1].has_right_wall = False
            # right
            if next_idx[1] == j + 1:
                self._cells[i][j].has_right_wall = False
                self._cells[i][j + 1].has_left_wall = False

            # visit next cell
            self._break_walls_r(next_idx[0], next_idx[1])

    def _reset_cell_visited(self):
        for row in self._cells:
            for cell in row:
                cell.visited = False

    def solve(self):
        return self._solve_r(0, 0)

    def _solve_r(self, i, j):
        # DFS trough cells
        self._animate()
        cur_cell = self._cells[i][j]
        cur_cell.visited = True

        # end cell index
        if i == self.num_rows - 1 and j == self.num_cols - 1:
            return True

        # above
        if i > 0 and not cur_cell.has_top_wall and not self._cells[i - 1][j].visited:
            cur_cell.draw_move(self._cells[i - 1][j])
            res = self._solve_r(i - 1, j)

            if res == True:
                return True
            else:
                cur_cell.draw_move(self._cells[i - 1][j], True)

        # below
        if (
            i < self.num_rows - 1
            and not cur_cell.has_bottom_wall
            and not self._cells[i + 1][j].visited
        ):
            cur_cell.draw_move(self._cells[i + 1][j])
            res = self._solve_r(i + 1, j)

            if res == True:
                return True
            else:
                cur_cell.draw_move(self._cells[i + 1][j], True)

        # left
        if j > 0 and not cur_cell.has_left_wall and not self._cells[i][j - 1].visited:
            cur_cell.draw_move(self._cells[i][j - 1])
            res = self._solve_r(i, j - 1)

            if res == True:
                return True
            else:
                cur_cell.draw_move(self._cells[i][j - 1], True)

        # right
        if (
            j < self.num_cols - 1
            and not cur_cell.has_right_wall
            and not self._cells[i][j + 1].visited
        ):
            cur_cell.draw_move(self._cells[i][j + 1])
            res = self._solve_r(i, j + 1)

            if res == True:
                return True
            else:
                cur_cell.draw_move(self._cells[i][j + 1], True)

        # if none of the conditions above worked out
        return False
