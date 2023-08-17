from n_canvas import constants as c


class MouseInteractor:
    def __init__(self, set, get):
        self._set = set
        self._get = get

    def set_shape_under_mouse(self, shape_id: str):
        self._set(c.SHAPE_UNDER_MOUSE, shape_id)

    def get_shape_under_mouse(self) -> str:
        return self._get(c.SHAPE_UNDER_MOUSE)

    def clear_shape_under_mouse(self):
        self._set(c.SHAPE_UNDER_MOUSE, None)
