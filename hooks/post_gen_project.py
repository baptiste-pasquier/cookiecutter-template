import shlex
import subprocess
from pathlib import Path


def run(command: str) -> None:
    """Execute a shell command as a subprocess.

    Args:
        command (str): Shell command to be executed.
    """
    print("+ " + command)
    subprocess.run(shlex.split(command))


def remove_line_from_file(file_path: str, target_string: str) -> None:
    """Remove lines containing a specific target string from a text file.

    Args:
        file_path (str): Text file path from which lines should be removed.
        target_string (str): String to identify lines to be removed.
    """
    # Read the file and filter out lines containing the target string
    with Path(file_path).open() as f:
        lines = f.readlines()
        filtered_lines = [line for line in lines if target_string not in line]

        assert len(filtered_lines) == len(lines) - 1

    # Write the filtered content back to the file
    with Path(file_path).open("w") as f:
        f.writelines(filtered_lines)


run("poetry add poethepoet pre-commit pytest pytest-cov ruff --group dev")

USE_NOTEBOOKS = "{{ cookiecutter.use_notebooks}}"
if USE_NOTEBOOKS == "yes":
    Path("notebooks").mkdir()

    run("poetry add ipykernel ipywidgets --group dev")

USE_DATA_SCIENCE = "{{ cookiecutter.use_data_science}}"
if USE_DATA_SCIENCE == "yes":
    Path("data").mkdir()
    with Path("data/.gitkeep").open("w") as file:
        pass
    with Path(".gitignore").open("a") as f:
        f.write("data/*\n")

    run("poetry add numpy pandas matplotlib seaborn scikit-learn")

USE_TORCH = "{{ cookiecutter.use_torch}}"
if USE_TORCH == "yes":
    run("poetry add numpy torch")

with Path(".gitignore").open("a") as f:
    f.write("\n")
    f.write("!.gitkeep\n")

ADD_TEST_CI = "{{ cookiecutter.add_test_ci }}"
if ADD_TEST_CI == "no":
    Path(".github/workflows/main.yml").unlink()
    remove_line_from_file("README.md", "workflows/main.yml")

ADD_CODECOV_CI = "{{ cookiecutter.add_codecov_ci }}"
if ADD_CODECOV_CI == "no":
    Path(".github/workflows/codecov.yml").unlink()
    remove_line_from_file("README.md", "codecov.io")

run("git init")
run("git add .")

run("poetry run pre-commit install")
run("poetry run pre-commit run -a")

run("git add .")
run('git commit -m ":tada: Initial commit"')
