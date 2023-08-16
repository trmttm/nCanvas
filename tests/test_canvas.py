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
        state_0 = {'shapes': ()}
        state_1 = {'shapes': ({'x': 0, 'y': 0},)}
        state_2 = {'shapes': ({'x': 0, 'y': 0}, {'x': 0, 'y': 0},)}
        state_3 = {'shapes': ({'x': 1, 'y': 0}, {'x': 0, 'y': 0},)}

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
        canvas = Canvas()
        rectangle = canvas.add_rectangle(id='rectangle01')
        rectangle.x = 1
        rectangle.y = 2
        rectangle.width = 5
        rectangle.height = 10
        canvas.backup()

        self.assertEqual(canvas.state, {'shapes': ({'id': 'rectangle01', 'height': 10, 'width': 5, 'x': 1, 'y': 2},)})
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

        # [Define commands]###########################################################

        import tkinter as tk
        from tkinter import ttk

        def change_canvas_color(c: tk.Canvas, color):
            c.configure(bg=color)

        buttons = {
            'btn_01': 'Canvas Color',
            'btn_02': 'Draw Rect',
            'btn_03': 'Move Rect X',
            'btn_04': 'Move Rect Y',
            'btn_05': 'Move Rect X and Draw',
            'btn_06': 'Move Rect Y and Draw',
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
        canvas.mouse_handler.mouse_in = lambda x, y: print('Mouse In', x, y)
        canvas.mouse_handler.mouse_out = lambda x, y: print('Mouse Out', x, y)

        canvas.mouse_handler.left_click = lambda x, y: print('Left Click', x, y)
        canvas.mouse_handler.left_click_motion = lambda x, y: print('Left Click Drag', x, y)
        canvas.mouse_handler.left_click_release = lambda x, y: print('Left Click Release', x, y)

        canvas.mouse_handler.right_click = lambda x, y: print('Right Click', x, y)
        canvas.mouse_handler.right_click_motion = lambda x, y: print('Right Click Drag', x, y)
        canvas.mouse_handler.right_click_release = lambda x, y: print('Right Click Release', x, y)

        canvas.mouse_handler.middle_click = lambda x, y: print('Middle Click', x, y)
        canvas.mouse_handler.middle_click_motion = lambda x, y: print('Middle Click Drag', x, y)
        canvas.mouse_handler.middle_click_release = lambda x, y: print('Middle Click Release', x, y)

        # Shift
        canvas.mouse_handler.left_click_shift = lambda x, y: print('SHIFT Left Click', x, y)
        canvas.mouse_handler.left_click_motion_shift = lambda x, y: print('SHIFT Left Click Drag', x, y)
        canvas.mouse_handler.left_click_release_shift = lambda x, y: print('SHIFT Left Click Release', x, y)

        canvas.mouse_handler.right_click_shift = lambda x, y: print('SHIFT Right Click', x, y)
        canvas.mouse_handler.right_click_motion_shift = lambda x, y: print('SHIFT Right Click Drag', x, y)
        canvas.mouse_handler.right_click_release_shift = lambda x, y: print('SHIFT Right Click Release', x, y)

        canvas.mouse_handler.middle_click_shift = lambda x, y: print('SHIFT Middle Click', x, y)
        canvas.mouse_handler.middle_click_motion_shift = lambda x, y: print('SHIFT Middle Click Drag', x, y)
        canvas.mouse_handler.middle_click_release_shift = lambda x, y: print('SHIFT Middle Click Release', x, y)

        # Control
        canvas.mouse_handler.left_click_control = lambda x, y: print('CONTROL Left Click', x, y)
        canvas.mouse_handler.left_click_motion_control = lambda x, y: print('CONTROL Left Click Drag', x, y)
        canvas.mouse_handler.left_click_release_control = lambda x, y: print('CONTROL Left Click Release', x, y)

        canvas.mouse_handler.right_click_control = lambda x, y: print('CONTROL Right Click', x, y)
        canvas.mouse_handler.right_click_motion_control = lambda x, y: print('CONTROL Right Click Drag', x, y)
        canvas.mouse_handler.right_click_release_control = lambda x, y: print('CONTROL Right Click Release', x, y)

        canvas.mouse_handler.middle_click_control = lambda x, y: print('CONTROL Middle Click', x, y)
        canvas.mouse_handler.middle_click_motion_control = lambda x, y: print('CONTROL Middle Click Drag', x, y)
        canvas.mouse_handler.middle_click_release_control = lambda x, y: print('CONTROL Middle Click Release', x, y)

        # Command
        canvas.mouse_handler.left_click_command = lambda x, y: print('COMMAND Left Click', x, y)
        canvas.mouse_handler.left_click_motion_command = lambda x, y: print('COMMAND Left Click Drag', x, y)
        canvas.mouse_handler.left_click_release_command = lambda x, y: print('COMMAND Left Click Release', x, y)

        canvas.mouse_handler.right_click_command = lambda x, y: print('COMMAND Right Click', x, y)
        canvas.mouse_handler.right_click_motion_command = lambda x, y: print('COMMAND Right Click Drag', x, y)
        canvas.mouse_handler.right_click_release_command = lambda x, y: print('COMMAND Right Click Release', x, y)

        canvas.mouse_handler.middle_click_command = lambda x, y: print('COMMAND Middle Click', x, y)
        canvas.mouse_handler.middle_click_motion_command = lambda x, y: print('COMMAND Middle Click Drag', x, y)
        canvas.mouse_handler.middle_click_release_command = lambda x, y: print('COMMAND Middle Click Release', x, y)

        # Alt
        canvas.mouse_handler.left_click_alt = lambda x, y: print('Alt Left Click', x, y)
        canvas.mouse_handler.left_click_motion_alt = lambda x, y: print('Alt Left Click Drag', x, y)
        canvas.mouse_handler.left_click_release_alt = lambda x, y: print('Alt Left Click Release', x, y)

        canvas.mouse_handler.right_click_alt = lambda x, y: print('Alt Right Click', x, y)
        canvas.mouse_handler.right_click_motion_alt = lambda x, y: print('Alt Right Click Drag', x, y)
        canvas.mouse_handler.right_click_release_alt = lambda x, y: print('Alt Right Click Release', x, y)

        canvas.mouse_handler.middle_click_alt = lambda x, y: print('Alt Middle Click', x, y)
        canvas.mouse_handler.middle_click_motion_alt = lambda x, y: print('Alt Middle Click Drag', x, y)
        canvas.mouse_handler.middle_click_release_alt = lambda x, y: print('Alt Middle Click Release', x, y)

        # [Define object interaction]###########################################################
        from n_canvas import constants as c
        from gui.canvas.rectangle.draw_rectangle import draw_rectangle
        n_canvas.subscribe(c.DRAW_RECTANGLE, lambda **data: draw_rectangle(canvas, **data))

        # [Bind commands]###########################################################
        def move_and_draw(x: int, y: int):
            n_canvas.set_position(rectangle, rectangle.x + x, rectangle.y + y)
            n_canvas.draw_rectangle(rectangle)

        widgets.get('btn_01').configure(command=lambda: change_canvas_color(canvas, 'light yellow'))
        widgets.get('btn_02').configure(command=lambda: n_canvas.draw_rectangle(rectangle))
        widgets.get('btn_03').configure(command=lambda: n_canvas.set_position(rectangle, rectangle.x + 10, rectangle.y))
        widgets.get('btn_04').configure(command=lambda: n_canvas.set_position(rectangle, rectangle.x, rectangle.y + 10))
        widgets.get('btn_05').configure(command=lambda: move_and_draw(10, 0))
        widgets.get('btn_06').configure(command=lambda: move_and_draw(0, 10))

        # [Launch App]###########################################################
        root.mainloop()


if __name__ == '__main__':
    unittest.main()
