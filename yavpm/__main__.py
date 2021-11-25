import git

TEST_URL = "https://github.com/preservim/nerdcommenter.git"


test_proj = git.Project(TEST_URL)
print(test_proj.project_name)
