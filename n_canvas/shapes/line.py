from .shape import Shape


class Line(Shape):
    @property
    def shape_name(self) -> str:
        return 'line'
