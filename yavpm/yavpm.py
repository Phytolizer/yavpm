import os


def yavpm_file():
    pass


def yavpm_update():
    pass


def yavpm_dir():
    if os.name == "nt":
        pass
    else:
        return "~/.vim/plug/yavpm"
