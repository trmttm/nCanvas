import tkinter as tk


def draw_rectangle(canvas_: tk.Canvas, **rectangle_state):
    if rectangle_exists(canvas_, **rectangle_state):
        add_new_rectangle(canvas_, **rectangle_state)
    else:
        move_rectangle(canvas_, **rectangle_state)


def add_new_rectangle(canvas_: tk.Canvas, **rectangle_state):
    rectangle_id = rectangle_state.get('id')
    x1, y1 = rectangle_state.get('x'), rectangle_state.get('y')
    width, height = rectangle_state.get('width'), rectangle_state.get('height')
    x2, y2 = x1 + width, y1 + height
    canvas_.create_rectangle(x1, y1, x2, y2, tags=(rectangle_id,))


def move_rectangle(canvas_: tk.Canvas, **rectangle_state):
    rectangle_id = rectangle_state.get('id')
    x_current, y_current = canvas_.coords(rectangle_id)[:2]
    x, y = rectangle_state.get('x'), rectangle_state.get('y')
    delta_x, delta_y = x - x_current, y - y_current
    canvas_.move(rectangle_id, delta_x, delta_y)


def rectangle_exists(canvas_: tk.Canvas, **rectangle_state) -> bool:
    rectangle_id = rectangle_state.get('id')
    rectangle_exists_ = not canvas_.find_withtag(rectangle_id)
    return rectangle_exists_
