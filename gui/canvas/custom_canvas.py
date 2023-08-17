import tkinter as tk

from gui.canvas.interface import ICustomCanvas
from n_canvas import constants as c
from .mouse import MouseHandler

tk_shift = 'Shift'
tk_control = 'Control'
tk_command = 'Command'
tk_option = 'Option'
tk_alt = 'Alt'

modifiers_mapper = {
    tk_shift: 'Shift',
    tk_control: 'Control',
    tk_command: 'Command',
    tk_option: 'Alt_Option',
    tk_alt: 'Alt_Option',
    None: None
}


class CustomCanvas(ICustomCanvas, tk.Canvas):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.mouse_handler = MouseHandler(self)

    def get_mouse_state(self, e: tk.Event) -> dict:
        try:
            shape_under_mouse = e.widget.itemconfigure('current')['tags'][-1].split(' ')[0]
        except KeyError:
            shape_under_mouse = None
        return {c.X: self.canvasx(e.x), c.Y: self.canvasy(e.y), c.SHAPE_UNDER_MOUSE: shape_under_mouse}

    def erase_shape(self, **kwargs):
        self.delete(kwargs.get('id'))


def create_custom_canvas(parent) -> CustomCanvas:
    canvas = CustomCanvas(parent)
    canvas.grid(row=0, column=0, sticky='nsew')

    return canvas
