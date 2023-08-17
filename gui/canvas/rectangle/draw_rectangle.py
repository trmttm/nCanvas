import tkinter as tk

from .set_properties import set_rectangle_fill_border_color_and_border_width
from .set_properties import set_rectangle_width_height
from .utility import get_rectangle_coords
from .utility import rectangle_exists


def move_or_draw_rectangle(canvas_: tk.Canvas, **rectangle_state):
    if rectangle_exists(canvas_, **rectangle_state):
        add_new_rectangle(canvas_, **rectangle_state)
    else:
        move_rectangle(canvas_, **rectangle_state)


def add_new_rectangle(canvas_: tk.Canvas, **rectangle_state):
    rectangle_id = rectangle_state.get('id')
    x1, y1, x2, y2 = get_rectangle_coords(rectangle_state)
    canvas_.create_rectangle(x1, y1, x2, y2, tags=(rectangle_id,))
    set_rectangle_fill_border_color_and_border_width(canvas_, **rectangle_state)


def move_rectangle(canvas_: tk.Canvas, **rectangle_state):
    rectangle_id = rectangle_state.get('id')
    x_current, y_current = canvas_.coords(rectangle_id)[:2]
    x, y = rectangle_state.get('x'), rectangle_state.get('y')
    delta_x, delta_y = x - x_current, y - y_current
    canvas_.move(rectangle_id, delta_x, delta_y)
    set_rectangle_width_height(canvas_, **rectangle_state)
