import os
import shlex
import subprocess


def run(command: str):
    """Execute a shell command as a subprocess.

    Args:
        command (str): Shell command to be executed.
    """
    print("+ " + command)
    subprocess.run(shlex.split(command))


def remove_line_from_file(file_path: str, target_string: str):
    """Remove lines containing a specific target string from a text file.

    Args:
        file_path (str): Text file path from which lines should be removed.
        target_string (str): String to identify lines to be removed.
    """
    # Read the file and filter out lines containing the target string
    with open(file_path) as f:
        lines = f.readlines()
        filtered_lines = [line for line in lines if target_string not in line]

        assert len(filtered_lines) == len(lines) - 1

    # Write the filtered content back to the file
    with open(file_path, "w") as f:
        f.writelines(filtered_lines)


run(
    "poetry add flake8 flake8-bugbear flake8-comprehensions flake8-simplify pep8-naming"
    " black pre-commit pytest pytest-cov poethepoet --group dev"
)

USE_NOTEBOOKS = "{{ cookiecutter.use_notebooks}}"
if USE_NOTEBOOKS == "yes":
    os.mkdir("notebooks")

    run('poetry add black[jupyter] ipykernel "ipywidgets>=7.0,<8.0" --group dev')

USE_DATA_SCIENCE = "{{ cookiecutter.use_data_science}}"
if USE_DATA_SCIENCE == "yes":
    os.mkdir("data")
    with open("data/.gitkeep", "w") as file:
        pass
    with open(".gitignore", "a") as f:
        f.write("data/*\n")

    run("poetry add numpy pandas matplotlib seaborn scikit-learn")

USE_TORCH = "{{ cookiecutter.use_torch}}"
if USE_TORCH == "yes":
    run("poetry add numpy torch")

with open(".gitignore", "a") as f:
    f.write("\n")
    f.write("!.gitkeep\n")

ADD_TEST_CI = "{{ cookiecutter.add_test_ci }}"
if ADD_TEST_CI == "no":
    os.remove(".github/workflows/main.yml")
    remove_line_from_file("README.md", "workflows/main.yml")

ADD_CODECOV_CI = "{{ cookiecutter.add_codecov_ci }}"
if ADD_CODECOV_CI == "no":
    os.remove(".github/workflows/codecov.yml")
    remove_line_from_file("README.md", "codecov.io")

run("git init")
run("git add .")

run("poetry run pre-commit install")
run("poetry run pre-commit run -a")

run("git add .")
run('git commit -m ":tada: Initial commit"')
