import unittest


class MyTestCase(unittest.TestCase):
    def test_high_level_interface(self):
        from n_canvas.interactors.canvas import Canvas
        canvas = Canvas()

        rectangle = canvas.add_rectangle()
        text_box = canvas.add_text_box()
        text = canvas.add_text()
        line = canvas.add_line()

        rectangle.set_x(5)
        text_box.set_x(5)
        text.set_x(5)
        line.set_x(5)
        self.assertEqual(rectangle.x, 5)
        self.assertEqual(text_box.x, 5)
        self.assertEqual(text.x, 5)
        self.assertEqual(line.x, 5)

        rectangle.set_y(10)
        text_box.set_y(10)
        text.set_y(10)
        line.set_y(10)
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
        rectangle.set_x(1)
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
        rectangle.set_x(1)
        rectangle.set_y(2)
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


if __name__ == '__main__':
    unittest.main()
