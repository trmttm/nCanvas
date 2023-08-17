import tkinter as tk

from .utility import get_rectangle_coords


def set_rectangle_width_height(canvas_: tk.Canvas, **rectangle_state):
    rectangle_id = rectangle_state.get('id')
    x0, y0, x1, y1 = get_rectangle_coords(rectangle_state)
    canvas_.coords(rectangle_id, x0, y0, x1, y1)


def set_border_color(canvas_: tk.Canvas, **rectangle_state):
    set_rectangle_fill_border_color_and_border_width(canvas_, **rectangle_state)


def fill(canvas_: tk.Canvas, **rectangle_state):
    set_rectangle_fill_border_color_and_border_width(canvas_, **rectangle_state)


def set_border_width(canvas_: tk.Canvas, **rectangle_state):
    set_rectangle_fill_border_color_and_border_width(canvas_, **rectangle_state)


def set_rectangle_fill_border_color_and_border_width(canvas_: tk.Canvas, **rectangle_state):
    rectangle_id = rectangle_state.get('id')
    border_color = rectangle_state.get('border_color', None)
    fill_color = rectangle_state.get('fill_color', None)
    border_width = rectangle_state.get('border_width', None)
    rectangle_property = {}
    if border_color:
        rectangle_property.update({'outline': border_color})
    if fill_color:
        rectangle_property.update({'fill': fill_color})
    if border_width:
        rectangle_property.update({'width': border_width})
    canvas_.itemconfigure(rectangle_id, rectangle_property)
