from typing import Callable


class Command:
    def __set_name__(self, owner, name):
        self._name = name

    def __set__(self, instance, command: Callable):
        self._command = command

    def __get__(self, instance, owner):
        return self._command
