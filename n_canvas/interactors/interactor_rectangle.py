from n_canvas import constants as c
from n_canvas import constants as c
from n_canvas import constants as c
from n_canvas import constants as c
from n_canvas import constants as c
from n_canvas import constants as c
from n_canvas.shapes.rectangle import Rectangle
from n_canvas.shapes.rectangle import Rectangle
from n_canvas.shapes.rectangle import Rectangle
from n_canvas.shapes.rectangle import Rectangle
from n_canvas.shapes.rectangle import Rectangle
from n_canvas.shapes.rectangle import Rectangle
from n_canvas.shapes.rectangle import Rectangle
from n_canvas.shapes.rectangle import Rectangle


class RectangleInteractor:
    def __init__(self, create_a_shape, get_any_shape_by_id, notify):
        self._create_a_shape = create_a_shape
        self._shape_type = c.RECTANGLE
        self._get_any_shape_by_id = get_any_shape_by_id
        self._notify = notify

    def add_new_shape(self, **kwargs) -> Rectangle:
        return self._create_a_shape(Rectangle, **kwargs)

    def get_shape_by_id(self, shape_id: str) -> Rectangle:
        shape = self._get_any_shape_by_id(shape_id)
        if shape.shape_name == self._shape_type:
            return shape

    def draw(self, rectangle: Rectangle):
        self._notify(c.DRAW_RECTANGLE, **rectangle.state)

    def set_width(self, rectangle: Rectangle):
        self._notify(c.SET_RECTANGLE_WIDTH, **rectangle.state)

    def set_border_color(self, rectangle: Rectangle):
        self._notify(c.SET_RECTANGLE_BORDER_COLOR, **rectangle.state)

    def set_fill_color(self, rectangle: Rectangle):
        self._notify(c.SET_RECTANGLE_FILL_COLOR, **rectangle.state)

    def set_border_width(self, rectangle: Rectangle):
        self._notify(c.SET_RECTANGLE_BORDER_WIDTH, **rectangle.state)