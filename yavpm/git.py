import os
import subprocess

import yavpm


class Project(yavpm.Project):
    def __init__(self, repo):
        super().__init__()
        self.project_name = self.parse_project_name(repo)

    def parse_project_name(self, url):
        return os.path.basename(url).replace(".git", "")

    def clone_dir(self):
        return os.path.join(yavpm.dir(), self.project_name)

    def clone(self, repo):
        try:
            subprocess.run(("git", "clone", repo, self.clone_dir()), check=True)
        except subprocess.CalledProcessError as e:
            print(f"Failed to run git: {e}")
