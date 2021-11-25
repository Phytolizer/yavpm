##causes error 'import git' works
##from yavpm import git
from git import git
git_url = "https://github.com/preservim/nerdcommenter.git"


def main():
    # test
    git_obj = git(git_url)
    print(git_obj.project_name)
    #git_obj.clone(git_url)


main()
