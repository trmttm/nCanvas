import abc


class IShape(abc.ABC):
    @property
    @abc.abstractmethod
    def shape_name(self) -> str:
        pass

    @abc.abstractmethod
    def set_position(self, x: int, y: int):
        pass
