from n_canvas import constants as c
from .shape import Shape


class Line(Shape):
    @property
    def shape_name(self) -> str:
        return c.LINE
