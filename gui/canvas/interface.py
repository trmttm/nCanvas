import abc
import tkinter as tk


class ICustomCanvas(abc.ABC):
    @abc.abstractmethod
    def get_xy(self, e: tk.Event) -> tuple[int, int]:
        pass