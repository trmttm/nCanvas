import sys
import tkinter as tk
from typing import Callable

tk_shift = 'Shift'
tk_control = 'Control'
tk_command = 'Command'
tk_option = 'Option'
tk_alt = 'Alt'


def bind_canvas(callback: Callable[[dict], None], canvas: tk.Canvas):
    if sys.platform == 'darwin':
        bind_mouse_mac(callback, canvas)
    else:
        bind_mouse_windows_or_unix(callback, canvas)
    bind_mouse_enter_and_leave(callback, canvas)


def bind_mouse_windows_or_unix(callback, widget):
    left = 'LEFT'
    right = 'RIGHT'
    middle = 'MIDDLE'
    modifiers = [tk_shift, tk_control, tk_alt]
    bind_mouse_actions(1, left, callback, widget, modifiers)
    bind_mouse_actions(3, right, callback, widget, modifiers)
    bind_mouse_actions(2, middle, callback, widget, modifiers)


def bind_mouse_mac(callback, widget):
    left = 'LEFT'
    right = 'RIGHT'
    middle = 'MIDDLE'
    modifiers = [tk_shift, tk_control, tk_command, tk_option]
    bind_mouse_actions(1, left, callback, widget, modifiers)
    bind_mouse_actions(2, right, callback, widget, modifiers)
    bind_mouse_actions(3, middle, callback, widget, modifiers)


def bind_mouse_enter_and_leave(callback, widget):
    mouse_in = 'MOUSE_IN'
    mouse_out = 'MOUSE_OUT'
    cb = callback
    widget.bind('<Enter>', lambda event: cb(x=widget.canvasx(event.x), y=widget.canvasy(event.y), io=mouse_in))
    widget.bind('<Leave>', lambda event: cb(x=widget.canvasx(event.x), y=widget.canvasy(event.y), io=mouse_out))


def bind_change_canvas_size(callback: Callable, canvas: tk.Canvas):
    canvas.bind("<Configure>", callback)


def get_mouse_canvas_coordinates(canvas: tk.Canvas) -> tuple:
    x = canvas.winfo_pointerx() - canvas.winfo_rootx()
    y = canvas.winfo_pointery() - canvas.winfo_rooty()
    return canvas.canvasx(x), canvas.canvasx(y)


def bind_mouse_actions(button_no, button: str, callback: Callable, widget: tk.Canvas, modifiers=None):
    click = 'CLICK'
    drag = 'CLICK_MOTION'
    release = 'CLICK_RELEASE'
    mouse_wheel = 'MOUSE_WHEEL'
    modifiers_mapper = {
        tk_shift: 'Shift',
        tk_control: 'Control',
        tk_command: 'Command',
        tk_option: 'Alt_Option',
        tk_alt: 'Alt_Option',
        None: None
    }

    def f(event, button_, modifier_, gesture_, **kwargs):
        """
        event.x, event.y are screen x, y
        canvasx, canvasy are canvas x, y
        """
        x = widget.canvasx(event.x)
        y = widget.canvasy(event.y)
        callback(x=x, y=y, click_type=button_, modifiers=modifiers_mapper[modifier_], getsture=gesture_, **kwargs)

    def kw(event) -> dict:
        scroll_x = 0 if event.state == 0 else event.delta
        scroll_y = 0 if event.state == 1 else event.delta
        return {'scroll_x': scroll_x, 'scroll_y': scroll_y, }

    widget.bind(f'<Button-{button_no}>', lambda event: f(event, button, None, click))
    widget.bind(f'<B{button_no}-Motion>', lambda event: f(event, button, None, drag))
    widget.bind(f'<ButtonRelease-{button_no}>', lambda event: f(event, button, None, release))
    widget.bind(f'<MouseWheel>', lambda event: f(event, None, None, mouse_wheel, **kw(event)))

    for modifier in (modifiers or []):
        widget.bind(f'<{modifier}-Button-{button_no}>', lambda event, m=modifier: f(event, button, m, click))
        widget.bind(f'<{modifier}-B{button_no}-Motion>', lambda event, m=modifier: f(event, button, m, drag))
        widget.bind(f'<{modifier}-ButtonRelease-{button_no}>', lambda event, m=modifier: f(event, button, m, release))

        """
        Disabling below because, for unknown reason, modifier + mousewheel is invoked instead of MouseWheel...
        """
        # widget.bind(f'<{modifier}-MouseWheel>', lambda event, m=modifier: f(event, None, m, mouse_wheel, **kw(event)))
