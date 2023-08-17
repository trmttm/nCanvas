import tkinter
from typing import Union

from .command import Command
from .interface import ICustomCanvas

tk_shift = 'Shift'
tk_control = 'Control'
tk_command = 'Command'
tk_option = 'Option'
tk_alt = 'Alt'


class MouseHandler:
    mouse_in = Command()
    mouse_motion = Command()
    mouse_out = Command()

    left_click = Command()
    right_click = Command()
    middle_click = Command()

    left_click_motion = Command()
    right_click_motion = Command()
    middle_click_motion = Command()

    left_click_release = Command()
    right_click_release = Command()
    middle_click_release = Command()

    # Shift
    left_click_shift = Command()
    right_click_shift = Command()
    middle_click_shift = Command()

    left_click_motion_shift = Command()
    right_click_motion_shift = Command()
    middle_click_motion_shift = Command()

    left_click_release_shift = Command()
    right_click_release_shift = Command()
    middle_click_release_shift = Command()

    # Control
    left_click_control = Command()
    right_click_control = Command()
    middle_click_control = Command()

    left_click_motion_control = Command()
    right_click_motion_control = Command()
    middle_click_motion_control = Command()

    left_click_release_control = Command()
    right_click_release_control = Command()
    middle_click_release_control = Command()

    # Command
    left_click_command = Command()
    right_click_command = Command()
    middle_click_command = Command()

    left_click_motion_command = Command()
    right_click_motion_command = Command()
    middle_click_motion_command = Command()

    left_click_release_command = Command()
    right_click_release_command = Command()
    middle_click_release_command = Command()

    # Alt
    left_click_alt = Command()
    right_click_alt = Command()
    middle_click_alt = Command()

    left_click_motion_alt = Command()
    right_click_motion_alt = Command()
    middle_click_motion_alt = Command()

    left_click_release_alt = Command()
    right_click_release_alt = Command()
    middle_click_release_alt = Command()

    def __init__(self, widget: Union[ICustomCanvas, tkinter.Canvas]):
        self._bind_enter_leave(widget)

        no_left = 1
        no_right = 2
        no_middle = 3

        tk_shift = 'Shift'
        tk_control = 'Control'
        tk_command = 'Command'
        tk_option = 'Option'
        tk_alt = 'Alt'

        self._bind_left_button(no_left, widget)
        self._bind_right_button(no_right, widget)
        self._bind_middle_button(no_middle, widget)

        self._bind_left_shift(no_left, tk_shift, widget)
        self._bind_left_control(no_left, tk_control, widget)
        self._bind_left_command(no_left, tk_command, widget)
        self._bind_left_option(no_left, tk_option, widget)
        self._bind_left_alt(no_left, tk_alt, widget)

        self._bind_right_shift(no_right, tk_shift, widget)
        self._bind_right_control(no_right, tk_control, widget)
        self._bind_right_command(no_right, tk_command, widget)
        self._bind_right_option(no_right, tk_option, widget)
        self._bind_right_alt(no_right, tk_alt, widget)

        self._bind_middle_shift(no_middle, tk_shift, widget)
        self._bind_middle_control(no_middle, tk_control, widget)
        self._bind_middle_command(no_middle, tk_command, widget)
        self._bind_middle_option(no_middle, tk_option, widget)
        self._bind_middle_alt(no_middle, tk_alt, widget)

    def _bind_middle_alt(self, no_middle, tk_alt, widget):
        button_no = no_middle
        modifier = tk_alt
        widget.bind(f'<{modifier}-Button-{button_no}>', lambda e: self.middle_click_alt(*widget.get_xy(e)))
        widget.bind(f'<{modifier}-B{button_no}-Motion>', lambda e: self.middle_click_motion_alt(*widget.get_xy(e)))
        widget.bind(f'<{modifier}-ButtonRelease-{button_no}>',
                    lambda e: self.middle_click_release_alt(*widget.get_xy(e)))

    def _bind_middle_option(self, no_middle, tk_option, widget):
        button_no = no_middle
        modifier = tk_option
        widget.bind(f'<{modifier}-Button-{button_no}>', lambda e: self.middle_click_alt(*widget.get_xy(e)))
        widget.bind(f'<{modifier}-B{button_no}-Motion>', lambda e: self.middle_click_motion_alt(*widget.get_xy(e)))
        widget.bind(f'<{modifier}-ButtonRelease-{button_no}>',
                    lambda e: self.middle_click_release_alt(*widget.get_xy(e)))

    def _bind_middle_command(self, no_middle, tk_command, widget):
        button_no = no_middle
        modifier = tk_command
        widget.bind(f'<{modifier}-Button-{button_no}>', lambda e: self.middle_click_command(*widget.get_xy(e)))
        widget.bind(f'<{modifier}-B{button_no}-Motion>', lambda e: self.middle_click_motion_command(*widget.get_xy(e)))
        widget.bind(f'<{modifier}-ButtonRelease-{button_no}>',
                    lambda e: self.middle_click_release_command(*widget.get_xy(e)))

    def _bind_middle_control(self, no_middle, tk_control, widget):
        button_no = no_middle
        modifier = tk_control
        widget.bind(f'<{modifier}-Button-{button_no}>', lambda e: self.middle_click_control(*widget.get_xy(e)))
        widget.bind(f'<{modifier}-B{button_no}-Motion>', lambda e: self.middle_click_motion_control(*widget.get_xy(e)))
        widget.bind(f'<{modifier}-ButtonRelease-{button_no}>',
                    lambda e: self.middle_click_release_control(*widget.get_xy(e)))

    def _bind_middle_shift(self, no_middle, tk_shift, widget):
        button_no = no_middle
        modifier = tk_shift
        widget.bind(f'<{modifier}-Button-{button_no}>', lambda e: self.middle_click_shift(*widget.get_xy(e)))
        widget.bind(f'<{modifier}-B{button_no}-Motion>', lambda e: self.middle_click_motion_shift(*widget.get_xy(e)))
        widget.bind(f'<{modifier}-ButtonRelease-{button_no}>',
                    lambda e: self.middle_click_release_shift(*widget.get_xy(e)))

    def _bind_left_alt(self, no_left, tk_alt, widget):
        button_no = no_left
        modifier = tk_alt
        widget.bind(f'<{modifier}-Button-{button_no}>', lambda e: self.left_click_alt(*widget.get_xy(e)))
        widget.bind(f'<{modifier}-B{button_no}-Motion>', lambda e: self.left_click_motion_alt(*widget.get_xy(e)))
        widget.bind(f'<{modifier}-ButtonRelease-{button_no}>',
                    lambda e: self.left_click_release_alt(*widget.get_xy(e)))

    def _bind_left_option(self, no_left, tk_option, widget):
        button_no = no_left
        modifier = tk_option
        widget.bind(f'<{modifier}-Button-{button_no}>', lambda e: self.left_click_alt(*widget.get_xy(e)))
        widget.bind(f'<{modifier}-B{button_no}-Motion>', lambda e: self.left_click_motion_alt(*widget.get_xy(e)))
        widget.bind(f'<{modifier}-ButtonRelease-{button_no}>',
                    lambda e: self.left_click_release_alt(*widget.get_xy(e)))

    def _bind_left_command(self, no_left, tk_command, widget):
        button_no = no_left
        modifier = tk_command
        widget.bind(f'<{modifier}-Button-{button_no}>', lambda e: self.left_click_command(*widget.get_xy(e)))
        widget.bind(f'<{modifier}-B{button_no}-Motion>', lambda e: self.left_click_motion_command(*widget.get_xy(e)))
        widget.bind(f'<{modifier}-ButtonRelease-{button_no}>',
                    lambda e: self.left_click_release_command(*widget.get_xy(e)))

    def _bind_left_control(self, no_left, tk_control, widget):
        button_no = no_left
        modifier = tk_control
        widget.bind(f'<{modifier}-Button-{button_no}>', lambda e: self.left_click_control(*widget.get_xy(e)))
        widget.bind(f'<{modifier}-B{button_no}-Motion>', lambda e: self.left_click_motion_control(*widget.get_xy(e)))
        widget.bind(f'<{modifier}-ButtonRelease-{button_no}>',
                    lambda e: self.left_click_release_control(*widget.get_xy(e)))

    def _bind_left_shift(self, no_left, tk_shift, widget):
        button_no = no_left
        modifier = tk_shift
        widget.bind(f'<{modifier}-Button-{button_no}>', lambda e: self.left_click_shift(*widget.get_xy(e)))
        widget.bind(f'<{modifier}-B{button_no}-Motion>', lambda e: self.left_click_motion_shift(*widget.get_xy(e)))
        widget.bind(f'<{modifier}-ButtonRelease-{button_no}>',
                    lambda e: self.left_click_release_shift(*widget.get_xy(e)))

    def _bind_right_alt(self, no_right, tk_alt, widget):
        button_no = no_right
        modifier = tk_alt
        widget.bind(f'<{modifier}-Button-{button_no}>', lambda e: self.right_click_alt(*widget.get_xy(e)))
        widget.bind(f'<{modifier}-B{button_no}-Motion>', lambda e: self.right_click_motion_alt(*widget.get_xy(e)))
        widget.bind(f'<{modifier}-ButtonRelease-{button_no}>',
                    lambda e: self.right_click_release_alt(*widget.get_xy(e)))

    def _bind_right_option(self, no_right, tk_option, widget):
        button_no = no_right
        modifier = tk_option
        widget.bind(f'<{modifier}-Button-{button_no}>', lambda e: self.right_click_alt(*widget.get_xy(e)))
        widget.bind(f'<{modifier}-B{button_no}-Motion>', lambda e: self.right_click_motion_alt(*widget.get_xy(e)))
        widget.bind(f'<{modifier}-ButtonRelease-{button_no}>',
                    lambda e: self.right_click_release_alt(*widget.get_xy(e)))

    def _bind_right_command(self, no_right, tk_command, widget):
        button_no = no_right
        modifier = tk_command
        widget.bind(f'<{modifier}-Button-{button_no}>', lambda e: self.right_click_command(*widget.get_xy(e)))
        widget.bind(f'<{modifier}-B{button_no}-Motion>', lambda e: self.right_click_motion_command(*widget.get_xy(e)))
        widget.bind(f'<{modifier}-ButtonRelease-{button_no}>',
                    lambda e: self.right_click_release_command(*widget.get_xy(e)))

    def _bind_right_control(self, no_right, tk_control, widget):
        button_no = no_right
        modifier = tk_control
        widget.bind(f'<{modifier}-Button-{button_no}>', lambda e: self.right_click_control(*widget.get_xy(e)))
        widget.bind(f'<{modifier}-B{button_no}-Motion>', lambda e: self.right_click_motion_control(*widget.get_xy(e)))
        widget.bind(f'<{modifier}-ButtonRelease-{button_no}>',
                    lambda e: self.right_click_release_control(*widget.get_xy(e)))

    def _bind_right_shift(self, no_right, tk_shift, widget):
        button_no = no_right
        modifier = tk_shift
        widget.bind(f'<{modifier}-Button-{button_no}>', lambda e: self.right_click_shift(*widget.get_xy(e)))
        widget.bind(f'<{modifier}-B{button_no}-Motion>', lambda e: self.right_click_motion_shift(*widget.get_xy(e)))
        widget.bind(f'<{modifier}-ButtonRelease-{button_no}>',
                    lambda e: self.right_click_release_shift(*widget.get_xy(e)))

    def _bind_middle_button(self, no_middle, widget):
        button_no = no_middle
        widget.bind(f'<Button-{button_no}>', lambda e: self.middle_click(*widget.get_xy(e)))
        widget.bind(f'<B{button_no}-Motion>', lambda e: self.middle_click_motion(*widget.get_xy(e)))
        widget.bind(f'<ButtonRelease-{button_no}>', lambda e: self.middle_click_release(*widget.get_xy(e)))

    def _bind_right_button(self, no_right, widget):
        button_no = no_right
        widget.bind(f'<Button-{button_no}>', lambda e: self.right_click(*widget.get_xy(e)))
        widget.bind(f'<B{button_no}-Motion>', lambda e: self.right_click_motion(*widget.get_xy(e)))
        widget.bind(f'<ButtonRelease-{button_no}>', lambda e: self.right_click_release(*widget.get_xy(e)))

    def _bind_left_button(self, no_left, widget):
        button_no = no_left
        widget.bind(f'<Button-{button_no}>', lambda e: self.left_click(*widget.get_xy(e)))
        widget.bind(f'<B{button_no}-Motion>', lambda e: self.left_click_motion(*widget.get_xy(e)))
        widget.bind(f'<ButtonRelease-{button_no}>', lambda e: self.left_click_release(*widget.get_xy(e)))

    def _bind_enter_leave(self, widget):
        widget.bind('<Enter>', lambda e: self.mouse_in(*widget.get_xy(e)))
        widget.bind('<Leave>', lambda e: self.mouse_out(*widget.get_xy(e)))
        widget.bind("<Motion>", lambda e: self.mouse_motion(e))
