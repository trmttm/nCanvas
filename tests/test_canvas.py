import unittest

from gui.canvas.custom_canvas import create_custom_canvas


class MyTestCase(unittest.TestCase):
    def test_high_level_interface(self):
        from n_canvas.interactors.canvas import Canvas
        canvas = Canvas()

        rectangle = canvas.add_rectangle()
        text_box = canvas.add_text_box()
        text = canvas.add_text()
        line = canvas.add_line()

        rectangle.x = 5
        text_box.x = 5
        text.x = 5
        line.x = 5
        self.assertEqual(rectangle.x, 5)
        self.assertEqual(text_box.x, 5)
        self.assertEqual(text.x, 5)
        self.assertEqual(line.x, 5)

        rectangle.y = 10
        text_box.y = 10
        text.y = 10
        line.y = 10
        self.assertEqual(rectangle.y, 10)
        self.assertEqual(text_box.y, 10)
        self.assertEqual(text.y, 10)
        self.assertEqual(line.y, 10)

        rectangle.set_position(6, 11)
        text_box.set_position(6, 11)
        text.set_position(6, 11)
        line.set_position(6, 11)
        self.assertEqual(rectangle.position, (6, 11))
        self.assertEqual(text_box.position, (6, 11))
        self.assertEqual(text.position, (6, 11))
        self.assertEqual(line.position, (6, 11))

    def test_undo_redo_state_io(self):
        from n_canvas.interactors.canvas import Canvas
        from n_canvas import constants as c
        state_0 = {c.SHAPES: ()}
        state_1 = {c.SHAPES: ({'x': 0, 'y': 0},)}
        state_2 = {c.SHAPES: ({'x': 0, 'y': 0}, {'x': 0, 'y': 0},)}
        state_3 = {c.SHAPES: ({'x': 1, 'y': 0}, {'x': 0, 'y': 0},)}

        canvas = Canvas()

        # State 0
        self.assertEqual(canvas.state, state_0)

        # State 1
        rectangle = canvas.add_rectangle()
        canvas.backup()
        self.assertEqual(canvas.state, state_1)

        # State 2
        canvas.add_rectangle()
        canvas.backup()
        self.assertEqual(canvas.state, state_2)

        # State 3
        rectangle.x = 1
        canvas.backup()
        self.assertEqual(canvas.state, state_3)

        canvas.show_history()
        self.assertEqual(len(canvas.get_history()), 4)  # Check history 01
        for state in (state_3, state_2, state_1, state_0):  # Check Undo and state
            print()
            canvas.undo()
            self.assertEqual(canvas.state, state)
        self.assertEqual(len(canvas.get_history()), 0)  # Check history 02

    def test_shape_with_descriptor(self):
        from n_canvas.interactors.canvas import Canvas
        from n_canvas import constants as c
        canvas = Canvas()
        rectangle = canvas.add_rectangle(id='rectangle01')
        rectangle.x = 1
        rectangle.y = 2
        rectangle.width = 5
        rectangle.height = 10
        canvas.backup()

        self.assertEqual(canvas.state, {c.SHAPES: ({'id': 'rectangle01', 'height': 10, 'width': 5, 'x': 1, 'y': 2},)})
        self.assertEqual(rectangle.width, 5)
        self.assertEqual(rectangle.height, 10)

    def test_text_box(self):
        from n_canvas.shapes.text_box import TextBox
        text_box = TextBox()
        text_box.width = 10
        text_box.font = 'Times New Roman'
        self.assertEqual(text_box.font, 'Times New Roman')
        self.assertEqual(text_box.width, 10)

    def test_gui(self):
        from n_canvas.interactors.canvas import Canvas
        n_canvas = Canvas()

        rectangle = n_canvas.add_rectangle(id='rectangle01')
        rectangle.set_position(10, 10)
        rectangle.width = 100
        rectangle.height = 25
        rectangle.border_color = 'blue'
        rectangle.border_width = 2
        rectangle.fill_color = 'pink'

        print(rectangle.state)

        n_canvas.draw_rectangle(rectangle)

        # [Create Widget Dictionary]###########################################################
        import tkinter as tk
        from tkinter import ttk

        buttons = {
            'btn_01': 'Canvas Color',
            'btn_02': 'Canvas border color blue',
            'btn_03': 'Move Rect X and Draw',
            'btn_04': 'Move Rect Y and Draw',
            'btn_05': '+ Width',
            'btn_06': 'Border color red',
            'btn_07': 'Draw Rect',
            'btn_08': 'Fill rectangle with yellow',
            'btn_09': '+ Border width',
        }
        widgets: dict[[str], tk.Widget] = {}

        # [Place widgets]###########################################################
        root = tk.Tk()
        root.grid_rowconfigure(0, weight=1)
        root.grid_columnconfigure(0, weight=1)
        root.grid_columnconfigure(1, weight=1)

        frame_controller = ttk.Frame(root)
        frame_controller.grid(row=0, column=0, sticky='nsew')

        frame_controller.grid_columnconfigure(0, weight=1)
        frame_controller.grid_rowconfigure(len(buttons), weight=1)
        for n, (button_id, text) in enumerate(buttons.items()):
            button = ttk.Button(frame_controller, text=text)
            button.grid(row=n, column=0, sticky='nsew')
            widgets[button_id] = button

        parent = ttk.Frame(root)
        parent.grid(row=0, column=1, sticky='nsew')

        parent.grid_rowconfigure(0, weight=1)
        parent.grid_columnconfigure(0, weight=1)

        canvas = create_custom_canvas(parent)

        def mouse_event_handler(**kwargs):
            event: tk.Event = kwargs.get('event', None)
            x: int = kwargs.get('x', None)
            y: int = kwargs.get('y', None)
            shape_under_mouse = kwargs.get('shape_under_mouse', None)

            print(f'{event} at x={x}, y={y}, shape_under_mouse={shape_under_mouse}')

        # [Canvas and Mouse actions]###########################################################
        mouse_handler = canvas.mouse_handler
        f = mouse_event_handler
        mouse_handler.mouse_in = lambda kwargs: f(event=c.Mouse_In, **kwargs)
        mouse_handler.mouse_out = lambda kwargs: f(event=c.Mouse_Out, **kwargs)
        mouse_handler.mouse_motion = lambda kwargs: f(event=c.Mouse_Motion_At, **kwargs)

        mouse_handler.left_click = lambda kwargs: f(event=c.Left_Click, **kwargs)
        mouse_handler.left_click_motion = lambda kwargs: f(event=c.Left_Click_Drag, **kwargs)
        mouse_handler.left_click_release = lambda kwargs: f(event=c.Left_Click_Release, **kwargs)

        mouse_handler.right_click = lambda kwargs: f(event=c.Right_Click, **kwargs)
        mouse_handler.right_click_motion = lambda kwargs: f(event=c.Right_Click_Drag, **kwargs)
        mouse_handler.right_click_release = lambda kwargs: f(event=c.Right_Click_Release, **kwargs)

        mouse_handler.middle_click = lambda kwargs: f(event=c.Middle_Click, **kwargs)
        mouse_handler.middle_click_motion = lambda kwargs: f(event=c.Middle_Click_Drag, **kwargs)
        mouse_handler.middle_click_release = lambda kwargs: f(event=c.Middle_Click_Release, **kwargs)

        # Shift
        mouse_handler.left_click_shift = lambda kwargs: f(event=c.SHIFT_Left_Click, **kwargs)
        mouse_handler.left_click_motion_shift = lambda kwargs: f(event=c.SHIFT_Left_Click_Drag, **kwargs)
        mouse_handler.left_click_release_shift = lambda kwargs: f(event=c.SHIFT_Left_Click_Release, **kwargs)

        mouse_handler.right_click_shift = lambda kwargs: f(event=c.SHIFT_Right_Click, **kwargs)
        mouse_handler.right_click_motion_shift = lambda kwargs: f(event=c.SHIFT_Right_Click_Drag, **kwargs)
        mouse_handler.right_click_release_shift = lambda kwargs: f(event=c.SHIFT_Right_Click_Release, **kwargs)

        mouse_handler.middle_click_shift = lambda kwargs: f(event=c.SHIFT_Middle_Click, **kwargs)
        mouse_handler.middle_click_motion_shift = lambda kwargs: f(event=c.SHIFT_Middle_Click_Drag, **kwargs)
        mouse_handler.middle_click_release_shift = lambda kwargs: f(event=c.SHIFT_Middle_Click_Release, **kwargs)

        # Control
        mouse_handler.left_click_control = lambda kwargs: f(event=c.CONTROL_Left_Click, **kwargs)
        mouse_handler.left_click_motion_control = lambda kwargs: f(event=c.CONTROL_Left_Click_Drag, **kwargs)
        mouse_handler.left_click_release_control = lambda kwargs: f(event=c.CONTROL_Left_Click_Release, **kwargs)

        mouse_handler.right_click_control = lambda kwargs: f(event=c.CONTROL_Right_Click, **kwargs)
        mouse_handler.right_click_motion_control = lambda kwargs: f(event=c.CONTROL_Right_Click_Drag, **kwargs)
        mouse_handler.right_click_release_control = lambda kwargs: f(event=c.CONTROL_Right_Click_Release, **kwargs)

        mouse_handler.middle_click_control = lambda kwargs: f(event=c.CONTROL_Middle_Click, **kwargs)
        mouse_handler.middle_click_motion_control = lambda kwargs: f(event=c.CONTROL_Middle_Click_Drag, **kwargs)
        mouse_handler.middle_click_release_control = lambda kwargs: f(event=c.CONTROL_Middle_Click_Release, **kwargs)

        # Command
        mouse_handler.left_click_command = lambda kwargs: f(event=c.COMMAND_Left_Click, **kwargs)
        mouse_handler.left_click_motion_command = lambda kwargs: f(event=c.COMMAND_Left_Click_Drag, **kwargs)
        mouse_handler.left_click_release_command = lambda kwargs: f(event=c.COMMAND_Left_Click_Release, **kwargs)

        mouse_handler.right_click_command = lambda kwargs: f(event=c.COMMAND_Right_Click, **kwargs)
        mouse_handler.right_click_motion_command = lambda kwargs: f(event=c.COMMAND_Right_Click_Drag, **kwargs)
        mouse_handler.right_click_release_command = lambda kwargs: f(event=c.COMMAND_Right_Click_Release, **kwargs)

        mouse_handler.middle_click_command = lambda kwargs: f(event=c.COMMAND_Middle_Click, **kwargs)
        mouse_handler.middle_click_motion_command = lambda kwargs: f(event=c.COMMAND_Middle_Click_Drag, **kwargs)
        mouse_handler.middle_click_release_command = lambda kwargs: f(event=c.COMMAND_Middle_Click_Release, **kwargs)

        # Alt
        mouse_handler.left_click_alt = lambda kwargs: f(event=c.Alt_Left_Click, **kwargs)
        mouse_handler.left_click_motion_alt = lambda kwargs: f(event=c.Alt_Left_Click_Drag, **kwargs)
        mouse_handler.left_click_release_alt = lambda kwargs: f(event=c.Alt_Left_Click_Release, **kwargs)

        mouse_handler.right_click_alt = lambda kwargs: f(event=c.Alt_Right_Click, **kwargs)
        mouse_handler.right_click_motion_alt = lambda kwargs: f(event=c.Alt_Right_Click_Drag, **kwargs)
        mouse_handler.right_click_release_alt = lambda kwargs: f(event=c.Alt_Right_Click_Release, **kwargs)

        mouse_handler.middle_click_alt = lambda kwargs: f(event=c.Alt_Middle_Click, **kwargs)
        mouse_handler.middle_click_motion_alt = lambda kwargs: f(event=c.Alt_Middle_Click_Drag, **kwargs)
        mouse_handler.middle_click_release_alt = lambda kwargs: f(event=c.Alt_Middle_Click_Release, **kwargs)

        # [Define object interaction]###########################################################
        from n_canvas import constants as c
        from gui.canvas.rectangle.draw_rectangle import move_or_draw_rectangle
        from gui.canvas.rectangle.set_properties import set_border_color
        from gui.canvas.rectangle.set_properties import fill
        from gui.canvas.rectangle.set_properties import set_border_width
        from gui.canvas.rectangle.set_properties import set_rectangle_width
        n_canvas.subscribe(c.DRAW_RECTANGLE, lambda **data: move_or_draw_rectangle(canvas, **data))
        n_canvas.subscribe(c.SET_RECTANGLE_WIDTH, lambda **data: set_rectangle_width(canvas, **data))
        n_canvas.subscribe(c.SET_RECTANGLE_BORDER_COLOR, lambda **data: set_border_color(canvas, **data))
        n_canvas.subscribe(c.SET_RECTANGLE_FILL_COLOR, lambda **data: fill(canvas, **data))
        n_canvas.subscribe(c.SET_RECTANGLE_BORDER_WIDTH, lambda **data: set_border_width(canvas, **data))

        # [Define commands]###########################################################

        def change_canvas_color(c: tk.Canvas, color):
            c.configure(bg=color)

        def set_canvas_border_color(c: tk.Canvas, color):
            c.config(highlightbackground=color)

        def move_and_draw(x: int, y: int):
            rectangle.x += x
            rectangle.y += y
            n_canvas.draw_rectangle(rectangle)

        def add_width(width: int):
            rectangle.width += width
            n_canvas.set_rectangle_width(rectangle)

        def change_border_color(color: str):
            rectangle.border_color = color
            n_canvas.set_rectangle_border_color(rectangle)

        def fill_rectangle_with(color: str):
            rectangle.fill_color = color
            n_canvas.set_rectangle_fill_color(rectangle)

        def add_rectangle_border_width(width: int):
            rectangle.border_width += width
            n_canvas.set_rectangle_border_width(rectangle)

        # [Bind commands]###########################################################
        widgets.get('btn_01').configure(command=lambda: change_canvas_color(canvas, 'light yellow'))
        widgets.get('btn_02').configure(command=lambda: set_canvas_border_color(canvas, 'blue'))
        widgets.get('btn_03').configure(command=lambda: move_and_draw(10, 0))
        widgets.get('btn_04').configure(command=lambda: move_and_draw(0, 10))
        widgets.get('btn_05').configure(command=lambda: add_width(10))
        widgets.get('btn_06').configure(command=lambda: change_border_color('red'))
        widgets.get('btn_07').configure(command=lambda: n_canvas.draw_rectangle(rectangle))
        widgets.get('btn_08').configure(command=lambda: fill_rectangle_with('yellow'))
        widgets.get('btn_09').configure(command=lambda: add_rectangle_border_width(1))

        # [Launch App]###########################################################
        root.mainloop()

    def test_abstract_out_and_define_architecture(self):
        pass


if __name__ == '__main__':
    unittest.main()
