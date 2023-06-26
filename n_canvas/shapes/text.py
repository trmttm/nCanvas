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
