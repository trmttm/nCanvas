from typing import Union

from n_memento import Entity

from n_canvas.interfaces import IShape
from n_canvas.shapes.line import Line
from n_canvas.shapes.rectangle import Rectangle
from n_canvas.shapes.text import Text
from n_canvas.shapes.text_box import TextBox


class Canvas(Entity):

    def __init__(self):
        super().__init__()
        self._shapes: list[Union[IShape, Entity]] = []
        self.backup()

    def undo(self):
        for shape in self._shapes:
            shape.undo()
        super().undo()

    def backup(self):
        for shape in self._shapes:
            shape.backup()
        self.set('shapes', tuple(shape.state for shape in self._shapes))
        super().backup()

    def add_rectangle(self, **kwargs) -> Rectangle:
        return self.create_a_shape(Rectangle, **kwargs)

    def add_text_box(self, **kwargs) -> TextBox:
        return self.create_a_shape(TextBox, **kwargs)

    def add_text(self, **kwargs) -> Text:
        return self.create_a_shape(Text, **kwargs)

    def add_line(self, **kwargs) -> Line:
        return self.create_a_shape(Line, **kwargs)

    def create_a_shape(self, shape_class, **kwargs):
        new_shape = shape_class(**kwargs)
        self._shapes.append(new_shape)
        return new_shape
