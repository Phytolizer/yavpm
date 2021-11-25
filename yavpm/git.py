import os
import subprocess

from yavpm import yavpm


def project_name(url):
    return os.path.basename(url).replace(".git", "")


def clone_dir(url):
    return os.path.join(yavpm.dir(), project_name(url))


def clone(repo):
    try:
        subprocess.run(("git", "clone", repo, clone_dir(repo)), check=True)
    except subprocess.CalledProcessError as e:
        print(f"Failed to run git: {e}")
