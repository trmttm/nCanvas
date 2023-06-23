from n_canvas.shapes.shape import Shape


class TextBox(Shape):
    @property
    def shape_name(self) -> str:
        return 'text_box'
