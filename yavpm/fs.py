import os

from yavpm import yavpm


class Project(yavpm.Project):
    def __init__(self, project_name):
        self.project_name = project_name
        self.already_installed = self.check_installed()

    def check_installed(self):
        dir = yavpm.dir()
        ##make sure that directory exists
        if os.path.exists(dir):
            with open(self.install_file(), "r") as file:
                lines = file.readlines()
            for line in lines:
                if line == self.project_name:
                    return True
            return False
        else:
            os.makedirs(dir)

    def install_file(self):
        return os.path.join(yavpm.dir(), "installed")

    def write_file(self):
        open(self.install_file(), "+w").write(self.project_name)

    def clone():
        pass
