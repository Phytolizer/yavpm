import os


def file():
    pass


def update():
    pass


def dir():
    if os.name == "nt":
        pass
    else:
        return os.path.expanduser('~') + '/.vim/plug/yavpm'
