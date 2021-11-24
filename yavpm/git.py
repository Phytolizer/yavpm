import os
import subprocess


def clone_dir(url):
    return os.path.join(yavpm_dir(), os.path.basename(url).replace(".git", ""))


def clone(repo):
    try:
        subprocess.run(("git", "clone", repo, clone_dir(repo)), check=True)
    except subprocess.CalledProcessError as e:
        print(f"Failed to run git: {e}")
