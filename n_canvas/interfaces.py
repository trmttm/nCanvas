import abc


class IShape(abc.ABC):
    @abc.abstractmethod
    def set_x(self, x: int):
        pass

    @abc.abstractmethod
    def set_y(self, y: int):
        pass

    @abc.abstractmethod
    def set_position(self, x: int, y: int):
        pass

    @property
    @abc.abstractmethod
    def x(self) -> int:
        pass

    @property
    @abc.abstractmethod
    def y(self) -> int:
        pass

    @property
    @abc.abstractmethod
    def position(self) -> tuple[int, int]:
        pass
