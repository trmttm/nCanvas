import unittest

from gui.canvas.custom_canvas import create_custom_canvas


class MyTestCase(unittest.TestCase):
    def test_high_level_interface(self):
        from n_canvas.interactors.canvas import Canvas
        canvas = Canvas()

        rectangle = canvas.rectangle_interactor.add_new_shape()
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
        state_1 = {c.SHAPES: ({'x': 0, 'y': 0, 'id': '01'},)}
        state_2 = {c.SHAPES: ({'x': 0, 'y': 0, 'id': '01'}, {'x': 0, 'y': 0, 'id': '02'},)}
        state_3 = {c.SHAPES: ({'x': 1, 'y': 0, 'id': '01'}, {'x': 0, 'y': 0, 'id': '02'},)}

        canvas = Canvas()

        # State 0
        self.assertEqual(canvas.state, state_0)

        # State 1
        rectangle = canvas.rectangle_interactor.add_new_shape(id='01')
        canvas.backup()
        self.assertEqual(canvas.state, state_1)

        # State 2
        canvas.rectangle_interactor.add_new_shape(id='02')
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
        rectangle = canvas.rectangle_interactor.add_new_shape(id='rectangle01')
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

        rectangle = n_canvas.rectangle_interactor.add_new_shape(id='rectangle01')
        rectangle.set_position(10, 10)
        rectangle.width = 100
        rectangle.height = 25
        rectangle.border_color = 'blue'
        rectangle.border_width = 2
        rectangle.fill_color = 'pink'

        print(rectangle.state)

        n_canvas.rectangle_interactor.draw(rectangle)

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
            event: tk.Event = kwargs.get(c.EVENT, None)
            x: int = kwargs.get(c.X, None)
            y: int = kwargs.get(c.Y, None)
            shape_id_under_mouse = kwargs.get(c.SHAPE_UNDER_MOUSE, None)

            # implement below based on each App's needs
            print(f'{event} at x={x}, y={y}, shape_id_under_mouse={shape_id_under_mouse}')

            if event == c.Mouse_Motion_At:
                if shape_id_under_mouse is not None:
                    shape_under_mouse = n_canvas.rectangle_interactor.get_shape_by_id(shape_id_under_mouse)
                    n_canvas.mouse_interactor.set_shape_under_mouse(shape_id_under_mouse)

                    if shape_id_under_mouse not in n_canvas.selection_interactor.get_shapes_selected():
                        shape_under_mouse.fill_color = 'yellow'
                        n_canvas.rectangle_interactor.set_fill_color(shape_under_mouse)

                else:
                    uncleared_shape_id = n_canvas.mouse_interactor.get_shape_under_mouse()
                    if uncleared_shape_id is not None:
                        n_canvas.mouse_interactor.clear_shape_under_mouse()
                        shape_to_clear = n_canvas.get_any_shape_by_id(uncleared_shape_id)

                        if uncleared_shape_id not in n_canvas.selection_interactor.get_shapes_selected():
                            shape_to_clear.fill_color = 'pink'
                            n_canvas.rectangle_interactor.set_fill_color(shape_to_clear)

            elif event == c.Left_Click:
                n_canvas.mouse_interactor.set_clicked_position(x, y)
                if shape_id_under_mouse is not None:
                    n_canvas.selection_interactor.select_shapes([shape_id_under_mouse])
                    for shape_id in n_canvas.selection_interactor.get_shapes_selected():
                        shape = n_canvas.rectangle_interactor.get_shape_by_id(shape_id)
                        shape.fill_color = 'orange'
                        n_canvas.rectangle_interactor.set_fill_color(shape)
                else:
                    for shape_id in n_canvas.selection_interactor.get_shapes_selected():
                        shape = n_canvas.rectangle_interactor.get_shape_by_id(shape_id)
                        shape.fill_color = 'pink'
                        n_canvas.rectangle_interactor.set_fill_color(shape)
                    n_canvas.selection_interactor.clear_shapes_selected()

            elif event == c.Left_Click_Drag:
                shape_ids_selected = n_canvas.selection_interactor.get_shapes_selected()
                if shape_ids_selected:
                    x0, y0 = n_canvas.mouse_interactor.get_clicked_position()
                    delta_x = x - x0
                    delta_y = y - y0
                    for shape_id in shape_ids_selected:
                        shape_selected = n_canvas.rectangle_interactor.get_shape_by_id(shape_id)
                        shape_selected.x += delta_x
                        shape_selected.y += delta_y
                        n_canvas.rectangle_interactor.draw(shape_selected)
                    n_canvas.mouse_interactor.set_clicked_position(x,y)

        # [Canvas and Mouse actions]###########################################################
        mouse_handler = canvas.mouse_handler

        def f(e: str, **kwargs):
            kwargs.update({c.EVENT: e})
            mouse_event_handler(**kwargs)

        mouse_handler.mouse_in = lambda kwargs: f(c.Mouse_In, **kwargs)
        mouse_handler.mouse_out = lambda kwargs: f(c.Mouse_Out, **kwargs)
        mouse_handler.mouse_motion = lambda kwargs: f(c.Mouse_Motion_At, **kwargs)

        mouse_handler.left_click = lambda kwargs: f(c.Left_Click, **kwargs)
        mouse_handler.left_click_motion = lambda kwargs: f(c.Left_Click_Drag, **kwargs)
        mouse_handler.left_click_release = lambda kwargs: f(c.Left_Click_Release, **kwargs)

        mouse_handler.right_click = lambda kwargs: f(c.Right_Click, **kwargs)
        mouse_handler.right_click_motion = lambda kwargs: f(c.Right_Click_Drag, **kwargs)
        mouse_handler.right_click_release = lambda kwargs: f(c.Right_Click_Release, **kwargs)

        mouse_handler.middle_click = lambda kwargs: f(c.Middle_Click, **kwargs)
        mouse_handler.middle_click_motion = lambda kwargs: f(c.Middle_Click_Drag, **kwargs)
        mouse_handler.middle_click_release = lambda kwargs: f(c.Middle_Click_Release, **kwargs)

        # Shift
        mouse_handler.left_click_shift = lambda kwargs: f(c.SHIFT_Left_Click, **kwargs)
        mouse_handler.left_click_motion_shift = lambda kwargs: f(c.SHIFT_Left_Click_Drag, **kwargs)
        mouse_handler.left_click_release_shift = lambda kwargs: f(c.SHIFT_Left_Click_Release, **kwargs)

        mouse_handler.right_click_shift = lambda kwargs: f(c.SHIFT_Right_Click, **kwargs)
        mouse_handler.right_click_motion_shift = lambda kwargs: f(c.SHIFT_Right_Click_Drag, **kwargs)
        mouse_handler.right_click_release_shift = lambda kwargs: f(c.SHIFT_Right_Click_Release, **kwargs)

        mouse_handler.middle_click_shift = lambda kwargs: f(c.SHIFT_Middle_Click, **kwargs)
        mouse_handler.middle_click_motion_shift = lambda kwargs: f(c.SHIFT_Middle_Click_Drag, **kwargs)
        mouse_handler.middle_click_release_shift = lambda kwargs: f(c.SHIFT_Middle_Click_Release, **kwargs)

        # Control
        mouse_handler.left_click_control = lambda kwargs: f(c.CONTROL_Left_Click, **kwargs)
        mouse_handler.left_click_motion_control = lambda kwargs: f(c.CONTROL_Left_Click_Drag, **kwargs)
        mouse_handler.left_click_release_control = lambda kwargs: f(c.CONTROL_Left_Click_Release, **kwargs)

        mouse_handler.right_click_control = lambda kwargs: f(c.CONTROL_Right_Click, **kwargs)
        mouse_handler.right_click_motion_control = lambda kwargs: f(c.CONTROL_Right_Click_Drag, **kwargs)
        mouse_handler.right_click_release_control = lambda kwargs: f(c.CONTROL_Right_Click_Release, **kwargs)

        mouse_handler.middle_click_control = lambda kwargs: f(c.CONTROL_Middle_Click, **kwargs)
        mouse_handler.middle_click_motion_control = lambda kwargs: f(c.CONTROL_Middle_Click_Drag, **kwargs)
        mouse_handler.middle_click_release_control = lambda kwargs: f(c.CONTROL_Middle_Click_Release, **kwargs)

        # Command
        mouse_handler.left_click_command = lambda kwargs: f(c.COMMAND_Left_Click, **kwargs)
        mouse_handler.left_click_motion_command = lambda kwargs: f(c.COMMAND_Left_Click_Drag, **kwargs)
        mouse_handler.left_click_release_command = lambda kwargs: f(c.COMMAND_Left_Click_Release, **kwargs)

        mouse_handler.right_click_command = lambda kwargs: f(c.COMMAND_Right_Click, **kwargs)
        mouse_handler.right_click_motion_command = lambda kwargs: f(c.COMMAND_Right_Click_Drag, **kwargs)
        mouse_handler.right_click_release_command = lambda kwargs: f(c.COMMAND_Right_Click_Release, **kwargs)

        mouse_handler.middle_click_command = lambda kwargs: f(c.COMMAND_Middle_Click, **kwargs)
        mouse_handler.middle_click_motion_command = lambda kwargs: f(c.COMMAND_Middle_Click_Drag, **kwargs)
        mouse_handler.middle_click_release_command = lambda kwargs: f(c.COMMAND_Middle_Click_Release, **kwargs)

        # Alt
        mouse_handler.left_click_alt = lambda kwargs: f(c.Alt_Left_Click, **kwargs)
        mouse_handler.left_click_motion_alt = lambda kwargs: f(c.Alt_Left_Click_Drag, **kwargs)
        mouse_handler.left_click_release_alt = lambda kwargs: f(c.Alt_Left_Click_Release, **kwargs)

        mouse_handler.right_click_alt = lambda kwargs: f(c.Alt_Right_Click, **kwargs)
        mouse_handler.right_click_motion_alt = lambda kwargs: f(c.Alt_Right_Click_Drag, **kwargs)
        mouse_handler.right_click_release_alt = lambda kwargs: f(c.Alt_Right_Click_Release, **kwargs)

        mouse_handler.middle_click_alt = lambda kwargs: f(c.Alt_Middle_Click, **kwargs)
        mouse_handler.middle_click_motion_alt = lambda kwargs: f(c.Alt_Middle_Click_Drag, **kwargs)
        mouse_handler.middle_click_release_alt = lambda kwargs: f(c.Alt_Middle_Click_Release, **kwargs)

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
            n_canvas.rectangle_interactor.draw(rectangle)

        def add_width(width: int):
            rectangle.width += width
            n_canvas.rectangle_interactor.set_width(rectangle)

        def change_border_color(color: str):
            rectangle.border_color = color
            n_canvas.rectangle_interactor.set_border_color(rectangle)

        def fill_rectangle_with(color: str):
            rectangle.fill_color = color
            n_canvas.rectangle_interactor.set_fill_color(rectangle)

        def add_rectangle_border_width(width: int):
            rectangle.border_width += width
            n_canvas.rectangle_interactor.set_border_width(rectangle)

        # [Bind commands]###########################################################
        widgets.get('btn_01').configure(command=lambda: change_canvas_color(canvas, 'light yellow'))
        widgets.get('btn_02').configure(command=lambda: set_canvas_border_color(canvas, 'blue'))
        widgets.get('btn_03').configure(command=lambda: move_and_draw(10, 0))
        widgets.get('btn_04').configure(command=lambda: move_and_draw(0, 10))
        widgets.get('btn_05').configure(command=lambda: add_width(10))
        widgets.get('btn_06').configure(command=lambda: change_border_color('red'))
        widgets.get('btn_07').configure(command=lambda: n_canvas.rectangle_interactor.draw(rectangle))
        widgets.get('btn_08').configure(command=lambda: fill_rectangle_with('yellow'))
        widgets.get('btn_09').configure(command=lambda: add_rectangle_border_width(1))

        # [Launch App]###########################################################
        root.mainloop()

    def test_abstract_out_and_define_architecture(self):
        pass


if __name__ == '__main__':
    unittest.main()
