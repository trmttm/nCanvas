from .shape import Shape


class Rectangle(Shape):
    @property
    def shape_name(self) -> str:
        return 'rectangle'
