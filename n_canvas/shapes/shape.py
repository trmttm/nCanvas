from n_memento import Entity

from n_canvas import constants as c
from n_canvas.interfaces import IShape


class Shape(IShape, Entity):
    _key_id = c.ID
    _key_x = c.X
    _key_y = c.Y

    def __init__(self, **kwargs):
        initial_state = {self._key_x: 0, self._key_y: 0}
        self.set_initial_state(initial_state, self._key_id, **kwargs)
        self.set_initial_state(initial_state, self._key_x, **kwargs)
        self.set_initial_state(initial_state, self._key_y, **kwargs)

        super().__init__(initial_state)

    def set_initial_state(self, initial_state, key, **kwargs):
        if kwargs.get(key):
            initial_state.update({self._key_id: kwargs.get(key)})

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
