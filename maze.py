from graphics import Cell


class Maze:
    def __init__(self, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, win):
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self.win = win

        self._cells = []

    def _create_cells(self):
        # fills _cells with list of cells. Each top-level list is a column of Cell objects.
        # Once the matric is populated it should call its _draw_cell() method on each cell
        # [ [cell, cell, cell], [cell, cell, cell], [cell, cell, cell] ]

        for _row in range(self.num_rows):
            cell_row = []
            for _cell in range(self.num_cols):
                cell_row.append(Cell(self.win))

            self._cells.append(cell_row)

        for row in self._cells:
            for cell in row:
                self._draw_cell()

    def _draw_cell(self, i, j):
        # calc x/y position of the cell based on i, j, cell size, and the x/y  position of the matrix itself

        # once calculated, draw the cell and call the maze's _animate() method
        pass

    def _animate(self):
        pass
