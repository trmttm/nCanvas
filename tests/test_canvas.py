import unittest

from n_canvas.interactors.canvas import Canvas


class MyTestCase(unittest.TestCase):
    def test_high_level_interface(self):
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
        state_0 = {'shapes': ()}
        state_1 = {'shapes': ({'x': 0, 'y': 0},)}
        state_2 = {'shapes': ({'x': 0, 'y': 0}, {'x': 0, 'y': 0},)}
        state_3 = {'shapes': ({'x': 1, 'y': 0}, {'x': 0, 'y': 0},)}

        canvas = Canvas()
        self.assertEqual(canvas.state, state_0)

        rectangle = canvas.add_rectangle()
        canvas.backup()
        self.assertEqual(canvas.state, state_1)

        canvas.add_rectangle()
        canvas.backup()
        self.assertEqual(canvas.state, state_2)

        rectangle.set_x(1)
        canvas.backup()
        self.assertEqual(canvas.state, state_3)

        canvas.show_history()

        canvas.undo()
        self.assertEqual(canvas.state, state_3)
        canvas.undo()
        self.assertEqual(canvas.state, state_2)
        canvas.undo()
        self.assertEqual(canvas.state, state_1)
        canvas.undo()
        self.assertEqual(canvas.state, state_0)

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

        # canvas.undo()
        # self.assertEqual(canvas.state, {})


if __name__ == '__main__':
    unittest.main()
