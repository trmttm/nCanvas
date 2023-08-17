from n_memento import Entity

from n_canvas.interfaces import IShape
from .shapeproperty import ShapeProperty


class Shape(IShape, Entity):
    id = ShapeProperty()
    x = ShapeProperty()
    y = ShapeProperty()

    def __init__(self, **kwargs):
        super().__init__()
        if 'id' in kwargs:
            self.id = kwargs.get('id')

        self.x = kwargs.get('x', 0)
        self.y = kwargs.get('y', 0)

    def set_position(self, x: int, y: int):
        self.x = x
        self.y = y

    @property
    def position(self) -> tuple[int, int]:
        return self.x, self.y
