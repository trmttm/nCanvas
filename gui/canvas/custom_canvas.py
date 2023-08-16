import tkinter as tk

from gui.canvas.interface import ICustomCanvas
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

    def get_xy(self, e: tk.Event) -> tuple[int, int]:
        return self.canvasx(e.x), self.canvasy(e.y)


def create_custom_canvas(parent) -> CustomCanvas:
    canvas = CustomCanvas(parent)
    canvas.grid(row=0, column=0, sticky='nsew')

    return canvas
