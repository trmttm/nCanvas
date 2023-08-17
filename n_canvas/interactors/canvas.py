from typing import Union

from n_memento import Entity

from n_canvas import constants as c
from n_canvas.interfaces import IShape
from n_canvas.shapes.line import Line
from n_canvas.shapes.text import Text
from n_canvas.shapes.text_box import TextBox
from .interactor_mouse import MouseInteractor
from .interactor_rectangle import RectangleInteractor
from .interactor_selection import SelectionInteractor


class Canvas(Entity):

    def __init__(self):
        super().__init__()
        self._shapes: dict[str, Union[IShape, Entity]] = {}
        self.backup()
        self._subscribers: dict[[str], list] = {}
        self._rectangle_interactor = RectangleInteractor(self.create_a_shape, self.get_any_shape_by_id, self._notify)
        self._mouse_interactor = MouseInteractor(self.set, self.get)
        self._selection_interactor = SelectionInteractor(self.set, self.get)

    def undo(self):
        for shape in self._shapes.values():
            shape.undo()
        super().undo()

    def backup(self):
        for shape in self._shapes.values():
            shape.backup()
        self.set(c.SHAPES, tuple(s.state for s in self._shapes.values()))
        super().backup()

    def get_any_shape_by_id(self, shape_id: str) -> IShape:
        return self._shapes.get(shape_id, None)

    def add_text_box(self, **kwargs) -> TextBox:
        return self.create_a_shape(TextBox, **kwargs)

    def add_text(self, **kwargs) -> Text:
        return self.create_a_shape(Text, **kwargs)

    def add_line(self, **kwargs) -> Line:
        return self.create_a_shape(Line, **kwargs)

    def create_a_shape(self, shape_class, **kwargs):
        new_shape = shape_class(**kwargs)
        self._shapes[new_shape.id] = new_shape
        return new_shape

    def subscribe(self, key: str, subscriber):
        if key in self._subscribers:
            if subscriber not in self._subscribers.get(key):
                self._subscribers.get(key).append(subscriber)
        else:
            self._subscribers[key] = [subscriber]

    def _notify(self, key, **kwargs):
        if key in self._subscribers:
            for subscriber in self._subscribers.get(key):
                subscriber(**kwargs)

    @property
    def selection_interactor(self) -> SelectionInteractor:
        return self._selection_interactor

    @property
    def mouse_interactor(self) -> MouseInteractor:
        return self._mouse_interactor

    @property
    def rectangle_interactor(self) -> RectangleInteractor:
        return self._rectangle_interactor
