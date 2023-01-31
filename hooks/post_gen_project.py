import os
import shlex
import subprocess


def run(command):
    print("+ " + command)
    subprocess.run(shlex.split(command))


run("poetry add flake8 black pre-commit pytest pytest-cov poethepoet --group dev")

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

run("git init")
run("git add .")

run("poetry run pre-commit install")
run("poetry run pre-commit run -a")

run("git add .")
run('git commit -m ":tada: Initial commit"')
