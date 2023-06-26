from .shape import Shape


# https://docs.python.org/3/howto/descriptor.html
class ShapeProperty:

    def __set_name__(self, owner, key):
        self._key = key

    def __get__(self, shape: Shape, owner):
        return shape.get(self._key)

    def __set__(self, shape: Shape, value):
        shape.set(self._key, value)
