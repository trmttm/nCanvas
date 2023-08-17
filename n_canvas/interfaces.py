import abc


class IShape(abc.ABC):
    @property
    @abc.abstractmethod
    def shape_name(self) -> str:
        pass

    @abc.abstractmethod
    def set_position(self, x: int, y: int):
        pass

    @property
    @abc.abstractmethod
    def id(self) -> str:
        pass

    @abc.abstractmethod
    def is_within_coordinates(self, x1: int, y1: int, x2: int, y2: int) -> bool:
        pass
