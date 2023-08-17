import abc
import tkinter as tk


class ICustomCanvas(abc.ABC):
    @abc.abstractmethod
    def get_mouse_state(self, e: tk.Event) -> dict:
        pass