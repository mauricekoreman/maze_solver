from tkinter import Tk, BOTH, Canvas


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Line:
    def __init__(self, p1: Point, p2: Point):
        self.__p1 = p1
        self.__p2 = p2

    def draw(self, canvas: Canvas, fill_color="black"):
        canvas.create_line(
            self.__p1.x, self.__p1.y, self.__p2.x, self.__p2.y, fill=fill_color, width=2
        )


class Window:
    def __init__(self, width: int, height: int):
        self.__root = Tk()
        self.__root.title = "Maze Solver"
        self.__root.protocol("WM_DELETE_WINDOW", self.close())
        self.__canvas = Canvas(self.__root, bg="white", width=width, height=height)
        self.__canvas.pack(fill=BOTH, expand=1)
        self.__is_window_running = False

    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()

    def wait_for_close(self):
        self.__is_window_running = True
        while self.__is_window_running == True:
            self.redraw()
        print("Window closed...")

    def close(self):
        self.__is_window_running = False

    def draw_line(self, line: Line, fill_color="black"):
        line.draw(self.__canvas, fill_color)


class Cell:
    def __init__(self, win: Window):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True

        self._x1 = None
        self._y1 = None
        self._x2 = None
        self._y2 = None

        self.win = win

    def draw(self, x1, y1, x2, y2):
        self._x1 = x1
        self._y1 = y1
        self._x2 = x2
        self._y2 = y2

        top_left = Point(x1, y1)
        top_right = Point(x2, y1)
        bottom_left = Point(x1, y2)
        bottom_right = Point(x2, y2)

        if self.has_left_wall:
            line = Line(top_left, bottom_left)
            self.win.draw_line(line)
        if self.has_top_wall:
            line = Line(top_left, top_right)
            self.win.draw_line(line)
        if self.has_right_wall:
            line = Line(top_right, bottom_right)
            self.win.draw_line(line)
        if self.has_bottom_wall:
            line = Line(bottom_left, bottom_right)
            self.win.draw_line(line)

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
