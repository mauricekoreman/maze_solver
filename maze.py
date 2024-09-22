from cell import Cell
import time


class Maze:

    def __init__(self, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, win=None):
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self.win = win
        self._cells = []

        self._create_cells()

    def _create_cells(self):
        # fills _cells with list of cells. Each top-level list is a column of Cell objects.
        # Once the matric is populated it should call its _draw_cell() method on each cell
        # [ [cell, cell, cell], [cell, cell, cell], [cell, cell, cell] ]

        for _row in range(self.num_rows):
            cell_row = []
            for _cell in range(self.num_cols):
                cell_row.append(Cell(self.win))

            self._cells.append(cell_row)

        for i, row in enumerate(self._cells):
            for j, cell in enumerate(row):
                self._draw_cell(i, j)

    def _draw_cell(self, i, j):
        if self.win is None:
            return

        # calc x/y position of the cell based on i, j, cell size, and the x/y  position of the matrix itself
        # once calculated, draw the cell and call the maze's _animate() method

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
