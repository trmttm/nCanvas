from n_canvas import constants as c
from n_canvas.shapes.shape import Shape


class TextBox(Shape):
    @property
    def shape_name(self) -> str:
        return c.TEXT_BOX
