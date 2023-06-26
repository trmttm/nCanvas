import abc


class IShape(abc.ABC):
    @property
    @abc.abstractmethod
    def shape_name(self) -> str:
        pass
