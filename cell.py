from graphics import Window, Point, Line


class Cell:

    def __init__(self, win: Window = None):
        self.win = win

        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self.visited = False

        self._x1 = None
        self._y1 = None
        self._x2 = None
        self._y2 = None

    def draw(self, x1, y1, x2, y2):
        self._x1 = x1
        self._y1 = y1
        self._x2 = x2
        self._y2 = y2

        top_left = Point(x1, y1)
        top_right = Point(x2, y1)
        bottom_left = Point(x1, y2)
        bottom_right = Point(x2, y2)

        left_wall = Line(top_left, bottom_left)
        right_wall = Line(top_right, bottom_right)
        top_wall = Line(top_left, top_right)
        bottom_wall = Line(bottom_left, bottom_right)

        if self.has_left_wall:
            self.win.draw_line(left_wall)
        else:
            self.win.draw_line(left_wall, "white")

        if self.has_right_wall:
            self.win.draw_line(right_wall)
        else:
            self.win.draw_line(right_wall, "white")

        if self.has_top_wall:
            self.win.draw_line(top_wall)
        else:
            self.win.draw_line(top_wall, "white")

        if self.has_bottom_wall:
            self.win.draw_line(bottom_wall)
        else:
            self.win.draw_line(bottom_wall, "white")

    def draw_move(self, to_cell, undo=False):
        # draw from the center of itself, to the center of another cell
        own_center_point = Point(
            abs(self._x1 + self._x2) // 2, abs(self._y1 + self._y2) // 2
        )
        to_center_point = Point(
            abs(to_cell._x1 + to_cell._x2) // 2, abs(to_cell._y1 + to_cell._y2) // 2
        )

        fill_color = "red"
        if undo == True:
            fill_color = "gray"

        # draw the line
        self.win.draw_line(Line(own_center_point, to_center_point), fill_color)
