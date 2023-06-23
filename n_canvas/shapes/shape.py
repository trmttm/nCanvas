from n_memento import Entity

from n_canvas.interfaces import IShape


class Shape(IShape, Entity):
    _key_x = 'x'
    _key_y = 'y'

    def __init__(self):
        initial_state = {
            self._key_x: 0,
            self._key_y: 0,
        }
        super().__init__(initial_state)

    def set_x(self, x: int):
        self.set(self._key_x, x)

    def set_y(self, y: int):
        self.set(self._key_y, y)

    def set_position(self, x: int, y: int):
        self.set_x(x)
        self.set_y(y)

    @property
    def x(self) -> int:
        return self.get(self._key_x)

    @property
    def y(self) -> int:
        return self.get(self._key_y)

    @property
    def position(self) -> tuple[int, int]:
        return self.x, self.y
