from git import Git

git_url = "https://github.com/preservim/nerdcommenter.git"


def main():
    # test
    git_obj = Git(git_url)
    print(git_obj.project_name)


main()
