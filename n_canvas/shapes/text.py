from n_canvas import constants as c
from .shape import Shape

from .shapeproperty import ShapeProperty


class Text(Shape):
    size = ShapeProperty()
    color = ShapeProperty()
    font = ShapeProperty()

    @property
    def shape_name(self) -> str:
        return c.TEXT

    def is_within_coordinates(self, x1: int, y1: int, x2: int, y2: int) -> bool:
        return False
