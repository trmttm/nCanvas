from n_canvas import constants as c
from .shape import Shape
from .shapeproperty import ShapeProperty


class Rectangle(Shape):
    width = ShapeProperty()
    height = ShapeProperty()
    border_color = ShapeProperty()

    @property
    def shape_name(self) -> str:
        return c.RECTANGLE
