import abc
import os


def file():
    pass


def update():
    pass


def dir():
    if os.name == "nt":
        pass
    else:
        return os.path.expanduser("~") + "/.vim/pack/yavpm/start"


class Project(abc.ABC):
    @abc.abstractmethod
    def clone(self):
        pass
