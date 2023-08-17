from n_canvas import constants as c
from .shape import Shape

from .shapeproperty import ShapeProperty


class Line(Shape):
    width = ShapeProperty()
    color = ShapeProperty()
    start_arrow = ShapeProperty()
    end_arrow = ShapeProperty()

    @property
    def shape_name(self) -> str:
        return c.LINE

    def is_within_coordinates(self, x1: int, y1: int, x2: int, y2: int) -> bool:
        return False
