import tkinter as tk


def get_rectangle_coords(rectangle_state):
    x1, y1 = rectangle_state.get('x'), rectangle_state.get('y')
    width, height = rectangle_state.get('width'), rectangle_state.get('height')
    x2, y2 = x1 + width, y1 + height
    return x1, y1, x2, y2


def rectangle_exists(canvas_: tk.Canvas, **rectangle_state) -> bool:
    rectangle_id = rectangle_state.get('id')
    rectangle_exists_ = not canvas_.find_withtag(rectangle_id)
    return rectangle_exists_
