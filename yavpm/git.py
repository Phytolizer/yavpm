import os
import subprocess

from yavpm import yavpm


class Project(yavpm.Project):
    def __init__(self, repo):
        self.url = repo
        self.project_name = self.parse_project_name(repo)

    def parse_project_name(self, url):
        return os.path.basename(url).replace(".git", "")

    def clone_dir(self):
        return os.path.join(yavpm.dir() + "/start", self.project_name)

    def clone(self):
        try:
            subprocess.run(("git", "clone", self.url, self.clone_dir()), check=True)
        except subprocess.CalledProcessError as e:
            print(f"Failed to run git: {e}")
