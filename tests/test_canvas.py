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


if __name__ == '__main__':
    unittest.main()
