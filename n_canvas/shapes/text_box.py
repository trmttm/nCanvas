from n_canvas import constants as c
from .rectangle import Rectangle
from .text import Text


class TextBox(Rectangle, Text):
    @property
    def shape_name(self) -> str:
        return c.TEXT_BOX
