from n_memento import Entity


# https://docs.python.org/3/howto/descriptor.html
class ShapeProperty:

    def __set_name__(self, owner, key):
        self._key = key

    def __get__(self, shape: Entity, owner):
        return shape.get(self._key)

    def __set__(self, shape: Entity, value):
        shape.set(self._key, value)
