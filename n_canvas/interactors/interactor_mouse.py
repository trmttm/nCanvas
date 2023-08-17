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

    def set_previous_position(self, x: int, y: int):
        self._set(c.PREVIOUS_POSITION, (x, y))

    def get_previous_position(self) -> str:
        return self._get(c.PREVIOUS_POSITION)

    def clear_previous_position(self):
        self._set(c.PREVIOUS_POSITION, None)

    def set_clicked_position(self, x: int, y: int):
        self._set(c.CLICKED_POSITION, (x, y))

    def get_clicked_position(self) -> str:
        return self._get(c.CLICKED_POSITION)

    def clear_clicked_position(self):
        self._set(c.CLICKED_POSITION, None)

    def turn_on_dragging_mode(self):
        self._set(c.DRAGGING_MODE, True)

    def turn_off_dragging_mode(self):
        self._set(c.DRAGGING_MODE, False)

    def is_dragging_mode(self) -> bool:
        return self._get(c.DRAGGING_MODE)
