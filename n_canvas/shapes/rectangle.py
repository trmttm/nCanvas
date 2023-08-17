from n_canvas import constants as c
from .shape import Shape
from .shapeproperty import ShapeProperty


class Rectangle(Shape):
    width = ShapeProperty()
    height = ShapeProperty()
    border_color = ShapeProperty()
    fill_color = ShapeProperty()
    border_width = ShapeProperty()

    @property
    def shape_name(self) -> str:
        return c.RECTANGLE

    def is_within_coordinates(self, x1: int, y1: int, x2: int, y2: int) -> bool:
        coords_selector = x1, y1, x2, y2
        coords_shape = self.x, self.y, self.x + self.width, self.y + self.height
        return coordinates_overlap(coords_selector, coords_shape)


def coordinates_overlap(coords1, coords2) -> bool:
    x11, x12 = min(coords1[0], coords1[2]), max(coords1[0], coords1[2]),
    y11, y12 = min(coords1[1], coords1[3]), max(coords1[1], coords1[3]),
    x21, x22 = min(coords2[0], coords2[2]), max(coords2[0], coords2[2]),
    y21, y22 = min(coords2[1], coords2[3]), max(coords2[1], coords2[3]),

    # If one rectangle is on left side of other
    if x11 >= x22 or x21 >= x12:
        return False

    # If one rectangle is above other
    if y12 <= y21 or y22 <= y11:
        return False

    return True
