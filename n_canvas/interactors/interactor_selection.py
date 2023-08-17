from n_canvas import constants as c


class SelectionInteractor:
    def __init__(self, set, get):
        self._set = set
        self._get = get

    def select_shapes(self, shape_ids: list):
        self._set(c.SHAPES_SELECTED, shape_ids)

    def get_shapes_selected(self) -> tuple:
        shape_ids_selected = self._get(c.SHAPES_SELECTED)
        if shape_ids_selected is not None:
            return tuple(shape_ids_selected)
        else:
            return ()

    def clear_shapes_selected(self):
        self._set(c.SHAPES_SELECTED, [])
