from n_canvas.interfaces import IShape
from n_canvas.shapes.line import Line
from n_canvas.shapes.rectangle import Rectangle
from n_canvas.shapes.text import Text
from n_canvas.shapes.text_box import TextBox


class Canvas:
    def add_rectangle(self) -> IShape:
        return Rectangle()

    def add_text_box(self) -> IShape:
        return TextBox()

    def add_text(self) -> IShape:
        return Text()

    def add_line(self) -> IShape:
        return Line()
