from .shape import Shape


class Text(Shape):
    @property
    def shape_name(self) -> str:
        return 'text'
