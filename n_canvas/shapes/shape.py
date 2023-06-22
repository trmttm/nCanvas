from n_canvas.interfaces import IShape


class Shape(IShape):
    def __init__(self):
        self._data = {
            'x': 0,
            'y': 0,
        }

    def set_x(self, x: int):
        self._data['x'] = x

    def set_y(self, y: int):
        self._data['y'] = y

    def set_position(self, x: int, y: int):
        self.set_x(x)
        self.set_y(y)

    @property
    def x(self) -> int:
        return self._data.get('x', 0)

    @property
    def y(self) -> int:
        return self._data.get('y', 0)

    @property
    def position(self) -> tuple[int, int]:
        return self.x, self.y
