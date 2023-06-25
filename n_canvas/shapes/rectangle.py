from n_canvas import constants as c
from .shape import Shape


class Rectangle(Shape):
    _width = c.WIDTH
    _height = c.HEIGHT
    _border_color = c.COLOR_BORDER

    @property
    def shape_name(self) -> str:
        return c.RECTANGLE

    def set_width(self, width: int):
        self.set(self._width, width)

    def set_height(self, height: int):
        self.set(self._height, height)

    def set_border_color(self, color: str):
        self.set(self._border_color, color)
