from yavpm import fs, git

TEST_URL = "https://github.com/preservim/nerdcommenter.git"

test_proj = git.Project(TEST_URL)
test_fs = fs.Project(test_proj.project_name)
if test_fs.already_installed:
    print(test_proj.project_name + " is already installed")
else:
    test_proj.clone()
    test_fs.write_file()
